import ast
import pandas as pd

def get_longest_string(dataset, column):
    """Find longest string in the column"""
    values_list = list(dataset[column].unique())
    try:
        longest = max(values_list, key=len)
    except Exception as e:
        longest = "N/A"
    return longest


def get_shortest_string(dataset, column):
    """Find shortest string in the column"""
    values_list = list(dataset[column].unique())
    try:
        shortest = min(values_list, key=len)
    except Exception as e:
        shortest = "N/A"
    return shortest


def get_na_count(dataset, column):
    """Count 'Not Specified' in column"""
    na_count = len(dataset[dataset[column] == "Not Specified"])
    return na_count


def describe_column(dataset, column):
    """Compile all the checks above"""
    column_dict = {}
    col_name = column.replace("_", " ")
    col_name = col_name.title()
    column_dict["name"] = col_name
    column_dict["Longest String"] = get_longest_string(dataset, column)
    column_dict["Shortest String"] = get_shortest_string(dataset, column)
    column_dict["Not Specified"] = get_na_count(dataset, column)

    return column_dict


def characters_difference(string_1, string_2):
    """Simple char difference function for validation"""
    result = 0
    dict_1 = ast.literal_eval(string_1)
    dict_2 = ast.literal_eval(string_2)
    for key in dict_1:
        if dict_1[key] != dict_2[key]:
            result += (abs(dict_1[key] - dict_2[key]))
    return result



def fix_date_format(df, column_name):
    df[column_name] = pd.to_datetime(df[column_name], format='%d/%m/%Y', errors='coerce').dt.strftime('%Y-%m-%d')
    return df



