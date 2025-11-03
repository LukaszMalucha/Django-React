from db_manager import utils_columns, utils_checks
from db_manager.utils import describe_column


def validate_dataset(dataset, dataset_type, columns, categories=None):
    errors = []

    required_columns = columns
    dataset_columns = set(dataset.columns.values)
    errors, col_difference = utils_checks.columns_check(errors, dataset_columns, required_columns)
    print(required_columns)

    if len(col_difference) == 0:

        if categories:
            errors = utils_checks.get_missing_elements(errors, dataset, categories, "category")

    return errors


def dataset_check(dataset, dataset_type, categories):
    """Compile validations before dataset upload"""
    columns = list(dataset.columns)

    columns_metadata = []
    for column in columns:
        dict_col = describe_column(dataset, column)
        columns_metadata.append(dict_col)

    if dataset_type == "dataset_type":
        validation_errors = validate_dataset(dataset, dataset_type, utils_columns.columns_dict[dataset_type])



    return columns_metadata, validation_errors
