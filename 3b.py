# import pandas as pd
#
# def replace_out_of_bounds(df, lower_bound=0, upper_bound=15):
#     df.replace("", pd.NA, inplace=True)
#     for column in df.columns[:-1]:
#         try:
#             df[column] = pd.to_numeric(df[column], errors='coerce')
#             cleaned_column = df[column].dropna()
#             replacement_value = cleaned_column[cleaned_column.between(lower_bound, upper_bound)].median()
#             df[column] = df[column].apply(
#                 lambda x: replacement_value if (pd.isna(x) or x < lower_bound or x > upper_bound) else x
#             )
#         except ValueError:
#             continue
#
#     return df
#
# iris_data = pd.read_csv("iris_with_errors_default.csv")
# corrected_dataset = replace_out_of_bounds(iris_data)
# corrected_dataset.to_csv("iris_with_errors_values_out_of_bound.csv", index=False)
# # print(corrected_dataset.values)
# missing_values = corrected_dataset.isnull().sum() + (corrected_dataset == "").sum()
# print("Missing values for each column:")
# print(missing_values)
# total_missing = missing_values.sum()
# print(f"\nTotal missing values in the dataset: {total_missing}")
# data_statistics = corrected_dataset.describe(include='all')
# print("\nIris dataset with errors statistics:")
# print(data_statistics)
