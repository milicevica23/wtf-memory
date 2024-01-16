import duckdb
import time

# conn = duckdb.connect("duckd.db")
conn = duckdb.connect(":memory:")
conn.sql(
    """
INSTALL tpch;
LOAD tpch;
CALL dbgen(sf = 1);
"""
)
time.sleep(1)
arrow_df = conn.sql("SELECT * FROM lineitem").arrow()
print(type(arrow_df))

# time.sleep(1)

# arrow_df2 = conn.execute("SELECT * FROM lineitem").fetch_arrow_table()
# print(type(arrow_df2))
# time.sleep(1)

from deltalake import DeltaTabel, write_deltalake

path = "../data/table_1"
write_deltalake(path, arrow_df, mode="overwrite")
