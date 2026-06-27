# =========================================================
# MULTITHREADING IN PYTHON
# =========================================================

# Multithreading = Running multiple tasks (threads)
# at the same time inside a single process.

# Thread = Smallest unit of execution

# Main advantage:
# Improves performance when tasks wait for I/O
# like API calls, file reading, database operations
# Suppose we have multiple tables
# and same PySpark ETL logic needs to run for all tables

# To use multithreading we import threading module


    
import time
import random
from concurrent.futures import ThreadPoolExecutor
tables = ["orders", "products", "customers", "reviews", "cancel"]

def myfunction(i):
    wait = random.randint(1, 10)
    time.sleep(3)
    print(f"I am {i}. I took {3} second")
# for i in tables:
#     myfunction(i)

# lets see if we have 100 of table we need to wait
# I wanted to process all the table in parallel

# loop are slow -> we will use multithreading

# using this it will run parallely
with ThreadPoolExecutor(max_workers=len(tables)) as executor:
    futures  = executor.map(myfunction,tables)
    
