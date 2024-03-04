import time

import duckdb
import numpy as np

repetitions = 5

conn = duckdb.connect(":memory:")
conn.sql(
    """
INSTALL tpch;
LOAD tpch;
CALL dbgen(sf = 5);
"""
)

statements = [
    """
    SELECT * FROM lineitem
    """
]

for statement_sql in statements:
    first = []
    second = []
    for _ in range(0, repetitions):
        t = time.process_time()

        df = conn.sql(statement_sql)
        conn.sql("COPY (SELECT * FROM df) TO './test1.parquet' (FORMAT PARQUET);")

        elapsed_time = time.process_time() - t
        first.append(elapsed_time)

        t = time.process_time()

        conn.sql(f"CREATE OR REPLACE TABLE test AS {statement_sql}")
        conn.sql("COPY test TO './test.parquet' (FORMAT PARQUET);")

        elapsed_time = time.process_time() - t
        second.append(elapsed_time)

    print("QUERY")

    # print(statement_sql)
    print(np.average(first))
    print(np.average(second))
