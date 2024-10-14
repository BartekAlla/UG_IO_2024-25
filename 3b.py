# import pandas as pd
#
# def replace_out_of_bounds(ds, lower_bound=0, upper_bound=15):
#     ds.replace("", pd.NA, inplace=True)
#     for column in ds.columns[:-1]:
#         try:
#             ds[column] = pd.to_numeric(ds[column], errors='coerce')
#             cleaned_column = ds[column].dropna()
#             replacement_value = cleaned_column[cleaned_column.between(lower_bound, upper_bound)].median()
#             ds[column] = ds[column].apply(
#                 lambda x: replacement_value if (pd.isna(x) or x < lower_bound or x > upper_bound) else x
#             )
#         except ValueError:
#             continue
#
#     return ds
#
# iris_data = pd.read_csv("iris_with_errors.csv")
# corrected_dataset = replace_out_of_bounds(iris_data)
# print(corrected_dataset.values)
# missing_values = corrected_dataset.isnull().sum() + (corrected_dataset == "").sum()
# print("Missing values for each column:")
# print(missing_values)
# total_missing = missing_values.sum()
# print(f"\nTotal missing values in the dataset: {total_missing}")
# data_statistics = corrected_dataset.describe(include='all')
# print("\nIris dataset with corrected numerical values statistics:")
# print(data_statistics)
