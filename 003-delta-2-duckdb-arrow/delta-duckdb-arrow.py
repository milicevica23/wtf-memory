import time

import duckdb
from deltalake import write_deltalake

conn = duckdb.connect(":memory:")
conn.sql(
    """
INSTALL tpch;
LOAD tpch;
CALL dbgen(sf = 1);
"""
)
time.sleep(2)
arrow_df = conn.execute("SELECT * FROM lineitem").fetch_record_batch()
time.sleep(2)
path = "../data/table_1"
write_deltalake(path, arrow_df, mode="overwrite")

arrow_df = conn.sql("SELECT * FROM lineitem").arrow()

#print(type(arrow_df))

# time.sleep(1)


# time.sleep(1)

