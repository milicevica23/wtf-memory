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
##your code
time.sleep(2)
conn.sql(
    """
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS lineitem;
DROP TABLE IF EXISTS nation;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS part;
DROP TABLE IF EXISTS partsupp;
DROP TABLE IF EXISTS region;
DROP TABLE IF EXISTS supplier;
"""
)
time.sleep(1)
