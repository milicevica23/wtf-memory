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

# conn.sql("CREATE TABLE test as SELECT * FROM lineitem")
# time.sleep(1)

conn.close()

time.sleep(1)
