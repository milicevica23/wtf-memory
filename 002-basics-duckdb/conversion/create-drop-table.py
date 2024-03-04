# import duckdb


import duckdb
import time

conn = duckdb.connect(":memory:")
time.sleep(1)
conn.sql(
    """
CREATE TABLE test AS SELECT * FROM read_parquet('/home/aleks/git/my-projects/wtf-memory/002-generate-tpch-data-with-duckdb/customer.parquet');
"""
)
time.sleep(1)
conn.sql(
    """
DROP TABLE test
"""
)
time.sleep(1)
