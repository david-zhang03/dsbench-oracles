import pandas as pd

data_path = '/home/ddzhang/DSBench/colab_tasks/dsbench_da_00000032/environment/data/MO14-Round-1-Dealing-With-Data-Workbook.xlsx'

usage = pd.read_excel(data_path, sheet_name='Usage')
contracts = pd.read_excel(data_path, sheet_name='Contracts')

print("=== USAGE SHEET ===")
print("Shape:", usage.shape)
print("Columns:", usage.columns.tolist())
print("Dtypes:")
print(usage.dtypes)
print("\nFirst 20 rows:")
print(usage.head(20).to_string())
print("\nLast 5 rows:")
print(usage.tail(5).to_string())

print("\n\n=== CONTRACTS SHEET ===")
print("Shape:", contracts.shape)
print("Columns:", contracts.columns.tolist())
print("Dtypes:")
print(contracts.dtypes)
print("\nFull contracts data:")
print(contracts.to_string())
