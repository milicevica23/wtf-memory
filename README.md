# wtf-memory
A repository to learn and understand more about memory usage in data applications

For memory profiling is [memray](https://github.com/bloomberg/memray) used. 

## Structure:
Each folder is a use case and contains:
    - a notebook for playing around
    - a python script to define the program
    - visualization 


- [ ] 001-hello-world-setup
- [ ] 002-generate-tpch-data-with-duckdb


## To create the environment:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


## How to track a notebook process:

### notebook extension
- [extension](https://bloomberg.github.io/memray/jupyter_magic.html)

### live tracking with pid
- understand the pid of the process
import os
pid = os.getpid()
print(pid)

- attach live to that process with memray
    - start terminal as root 
    - activate virtual environment with memray
    - execute memray attach <pid>




