from fastapi import FastAPI
from config import connection

app = FastAPI()


@app.get("/")
def hello():
    return {"response": "Hello!"}


@app.post("/")
def post_hello(message: int):

    return {"response": f"{message}!!!"}


post_hello("hello")


@app.get("/db")
def connect_db_test():
    cursor = connection.cursor()

    query = "SELECT * FROM users"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    return {"message": result}
