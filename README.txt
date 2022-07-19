step 1: 1st, i do the installation in localhost (pip install fastapi) after that i install the uvicorn (pip install uvicorn) lib and also install in sqlite for database purpose remain lib common  like HTTPException, and Depends

step 2 : (Process)
 1. create a one python file (assinment.py) and connect to the fast api like (from fastapi import FastAPI) after that take a one veriable (app) and store the value of Fastapi (app = FastAPI() ) and write a one decorate function  like (  @app.post("/mainapp")  ).
2. now, which method do want, that method write in a function like (post, put, get, delete like curd operation)

step 3 : (Database)
1. first create a one model.py file, in that which field do you want like column write a code
2. now, i used latt and long float fields. you use decimal field also
3. after that create a one file like database,py  write your connection code

Note :- in my browser default setting are there, so i mention mainapp in function . pls remove mainapp in function. write "/"
