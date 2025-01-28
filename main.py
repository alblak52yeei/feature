from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/items")
def get_items():
    return {"items": ["item1", "item2", "item3"]}


@app.get("/item_by_id")
def get_item_by_id(id):
    return {id: "items"}
