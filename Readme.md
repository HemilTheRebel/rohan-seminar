# One time setup

1. Check python version: `python -V`. It should be greater than 3.6. If it is python 2, try `python3 -V`. If both python and python3 dont work, install python
2. `pip install virtualenv`. If you get pip command not found, google how to install pop
3. 
    a. If you have `python -V` printed `python 3.x.x`, type `virtualenv venv`
    b. Else `virtualenv python3`

4. `source venv/bin/activate` (Always run this before running the script)
5. `pip install -r requirements.txt` 
6. `python server.py` should start the server


# Running the server 
1. Check if your terminal row starts with `(venv)`. If not, run `source venv/bin/activate`
2. `python server.py` should start the server