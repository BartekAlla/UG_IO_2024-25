import pandas as pd
from difflib import get_close_matches


def replace_out_of_bounds(ds, lower_bound=0, upper_bound=15):
    ds.replace("", pd.NA, inplace=True)
    for column in ds.columns[:-1]:
        try:
            ds[column] = pd.to_numeric(ds[column], errors='coerce')
            cleaned_column = ds[column].dropna()
            replacement_value = cleaned_column[cleaned_column.between(lower_bound, upper_bound)].median()
            ds[column] = ds[column].apply(
                lambda x: replacement_value if (pd.isna(x) or x < lower_bound or x > upper_bound) else x
            )
        except ValueError:
            continue

    return ds


def check_species(ds):
    expected_varieties = {"Setosa", "Versicolor", "Virginica"}
    incorrect_varieties = ds["variety"][~ds["variety"].isin(expected_varieties)]
    if not incorrect_varieties.empty:
        print("Incorrect varieties found:")
        print(incorrect_varieties.unique())
        ds["variety"] = ds["variety"].apply(
            lambda x: get_close_matches(x, expected_varieties, n=1, cutoff=0.6)[0] if x not in expected_varieties else x
        )

    return ds


iris_data = pd.read_csv("iris_with_errors.csv")
corrected_dataset = replace_out_of_bounds(iris_data)
corrected_dataset = check_species(corrected_dataset)
print(corrected_dataset.values)

