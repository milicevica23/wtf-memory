from deltalake import DeltaTable
import time

path = "../data/table_1"
dlt = DeltaTable(path)

print(type(dlt))

time.sleep(1)

arrow_df1 = dlt.to_pyarrow_dataset()

time.sleep(1)

# arrow_df2 = dlt.to_pyarrow_table()

# time.sleep(1)
