# import pandas as pd
#
# iris_data = pd.read_csv("iris_with_errors.csv")
#
# missing_values = iris_data.isnull().sum() + (iris_data == "").sum()
# print("Missing values for each column:")
# print(missing_values)
# total_missing = missing_values.sum()
# print(f"\nTotal missing values in the dataset: {total_missing}")
# data_statistics = iris_data.describe(include='all')
# print("\nIris dataset with errors statistics:")
# print(data_statistics)