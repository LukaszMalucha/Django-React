def columns_check(errors, dataset_columns, required_columns):
    columns_count = len(required_columns)
    dataset_columns_count = len(dataset_columns)
    if dataset_columns_count != columns_count:
        error_column = f"Dataset should have {columns_count} columns"
        errors.append(error_column)

    col_difference_1 = required_columns - dataset_columns
    col_difference_2 = dataset_columns - required_columns
    col_difference = set.union(col_difference_1, col_difference_2)
    col_difference = ", ".join(col_difference)
    if len(col_difference) > 0:
        error_column = f"Invalid columns in dataset: {col_difference}"
        errors.append(error_column)

    return errors, col_difference

def na_check(errors, dataset):
    check_na = dataset.isnull().values.any()
    if check_na:
        error_check_na = f"NaN present in dataset"
        errors.append(error_check_na)
    return errors


def get_missing_elements(errors, dataset, db_collection, column):
    """Check for incorrect/missing"""
    db_collection = db_collection
    column_checked = set(list(dataset[column].unique()))
    difference = column_checked - db_collection
    difference = ", ".join(difference)
    if len(difference) > 0:
        errors.append(f"{column} not found in DB: {difference}")
    return errors
