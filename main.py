from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def read_root():
    return {'hello':'world'}
@app.post("/items/")
def create_item(name: str, price: float):
    return{'name':name, 'price': price}
