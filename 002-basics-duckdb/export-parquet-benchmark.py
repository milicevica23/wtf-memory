import time

import duckdb
import numpy as np

repetitions = 3
SF = 5
conn = duckdb.connect(":memory:")
conn.sql(
    f"""
INSTALL tpch;
LOAD tpch;
CALL dbgen(sf = {SF});
"""
)

statements = [
    """
    SELECT * FROM lineitem
    """
]

for statement_sql in statements:
    a = []
    b = []
    c = []
    d = []
    e = []
    for _ in range(0, repetitions):
        t = time.process_time()

        conn.sql(
            "COPY (SELECT * FROM (SELECT * FROM lineitem)) TO './test0.parquet' (FORMAT PARQUET);"
        )

        elapsed_time = time.process_time() - t
        a.append(elapsed_time)

        t = time.process_time()

        conn.sql(f"CREATE OR REPLACE TABLE test AS {statement_sql}")
        conn.sql("COPY test TO './test1.parquet' (FORMAT PARQUET);")

        elapsed_time = time.process_time() - t
        b.append(elapsed_time)

        t = time.process_time()

        df = conn.sql(statement_sql)
        conn.sql("COPY (SELECT * FROM df) TO './test2.parquet' (FORMAT PARQUET);")

        elapsed_time = time.process_time() - t
        c.append(elapsed_time)

        t = time.process_time()

        df = conn.sql(statement_sql).df()
        conn.sql("COPY (SELECT * FROM df) TO './test3.parquet' (FORMAT PARQUET);")

        elapsed_time = time.process_time() - t
        d.append(elapsed_time)

        t = time.process_time()

        df = conn.sql(statement_sql).arrow()
        conn.sql("COPY (SELECT * FROM df) TO './test4.parquet' (FORMAT PARQUET);")

        elapsed_time = time.process_time() - t
        e.append(elapsed_time)

    print("QUERY")
    print(statement_sql)
    print(f"repetition: {repetitions}")
    print(f"SF: {repetitions}")
    print(f"a : {np.average(a)}")
    print(f"b : {np.average(b)}")
    print(f"c : {np.average(c)}")
    print(f"d : {np.average(d)}")
    print(f"d : {np.average(e)}")
