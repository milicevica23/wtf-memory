# wtf-memory
A repository to learn and understand more about memory usage in data applications

For memory profiling is [memray](https://github.com/bloomberg/memray) used. 

## Structure:
Each folder is a use case and contains:
    - a notebook for playing around
    - a python script to define the script


- 001-hello-world-setup
- 002-generate-tpch-data-with-duckdb


## To create the environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## To start the script with mamray
```bash
memray --native <script>
```

look into the logs and create an html page with the provided command

## How to track a notebook process:

### notebook extension
- [extension](https://bloomberg.github.io/memray/jupyter_magic.html)
- results would be in the memray-results 
- you can install live server extension in VS code to be able to open them with right click
- it is important to undestand [graph representations](https://bloomberg.github.io/memray/flamegraph.html)

### live tracking with pid
- understand the pid of the process
import os
pid = os.getpid()
print(pid)

- attach live to that process with memray
    - start terminal as root 
    - activate virtual environment with memray
    - execute memray attach <pid>


# Concepts 
Some material to understand core concepts

- [a program memory overview](https://www.youtube.com/watch?v=5OJRqkYbK-4)
- [MIT lecture threads](https://youtu.be/gA4YXUJX7t8?t=281)
- [memray creators podcast about memray](https://www.youtube.com/watch?v=wn_2e33KaYQ)



