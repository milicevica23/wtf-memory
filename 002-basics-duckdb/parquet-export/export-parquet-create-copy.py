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

conn.sql("CREATE OR REPLACE TABLE test AS SELECT * FROM lineitem")

time.sleep(2)
conn.sql("COPY test TO './test1.parquet' (FORMAT PARQUET);")
