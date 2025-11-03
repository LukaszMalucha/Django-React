import pandas as pd
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


from db_manager.data_validation import dataset_check


@user_passes_test(lambda u: u.is_superuser)
def db_manager(request):
    """Basic DB Manager dashboard"""

    return render(request, "db-manager.html")


@user_passes_test(lambda u: u.is_superuser)
def db_upload(request):
    """DB Manager for uploads"""

    return render(request, "db-upload.html")


@user_passes_test(lambda u: u.is_superuser)
def db_download(request):
    """DB Manager for downloads"""

    return render(request, "db-download.html")


@user_passes_test(lambda u: u.is_superuser)
def dataset_upload(request, dataset_type):
    """Bulk dataset upload to database"""
    meta = []
    dataset_errors = []
    report = dict()

    # To check if foreign key field exists before uploading
    CATEGORIES = set(list(CategoryModel.objects.all().values_list('category', flat=True)))

    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        filename = csv_file.name
        if not csv_file.name.endswith('.csv'):
            critical_error = "Incorrect file format. Please upload CSV file"
            return render(request, "upload.html",
                {"critical_error": critical_error, })
        data = pd.read_csv(csv_file, encoding="utf-8-sig")

        # Generate meta and error report
        meta, dataset_errors = dataset_check(data, dataset_type,
            categories=CATEGORIES
        )

        if len(meta) < 10:
            meta_1 = meta[:4]
            meta_2 = meta[4:8]
            meta_3 = meta[8:]
        else:
            meta_1 = meta[:8]
            meta_2 = meta[8:16]
            meta_3 = meta[16:]

        # No error has been found
        if len(dataset_errors) == 0:
            # try:
            # if dataset_type == "categories":
            #     report = data_upload.dataset_category_upload(data)

            # except:
            #     critical_error = "Dataset upload wasn't successful due to error"
            #     return render(request, "upload.html",
            #                   {"critical_error": critical_error, })

            upload_report = report
            return render(request, "upload.html",
                {"meta_1": meta_1, "meta_2": meta_2, "meta_3": meta_3, "upload_report": upload_report, "filename": filename,
                 "d_type": dataset_type})

        else:
            return render(request, "upload.html",
                {"meta_1": meta_1, "meta_2": meta_2, "meta_3": meta_3,
                 "dataset_errors": dataset_errors,
                 "filename": filename, "d_type": dataset_type})

    return render(request, "upload.html", {"d_type": dataset_type})
