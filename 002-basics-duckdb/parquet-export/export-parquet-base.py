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

conn.sql(
    "COPY (SELECT * FROM (SELECT * FROM lineitem)) TO './test0.parquet' (FORMAT PARQUET);"
)
