from fastapi import FastAPI
app=FastAPI()
@app.get("/user/{item_name}")
def read_user(item_name:str):
    return{"user_id":item_name}