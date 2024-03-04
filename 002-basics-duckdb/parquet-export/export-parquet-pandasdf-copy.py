import time

import duckdb

conn = duckdb.connect(":memory:")
conn.sql(
    """
INSTALL tpch;
LOAD tpch;
CALL dbgen(sf = 0.3);
"""
)

time.sleep(2)

df = conn.sql("SELECT * FROM lineitem").df()

time.sleep(2)

conn.sql("COPY (SELECT * FROM df) TO './test2.parquet' (FORMAT PARQUET);")
