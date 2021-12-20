from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

all_posts = [
    {"id":1, "title": "My first", "content": "This is the very first post using fast api, pydantic, postman etc.", "author": "Ibrahim", "published": False},
    {"id":2, "title": "Postiscus", "content": "Post no 2 should be the most entertaining and exciting due to a number of irreconciliable factors", "author": "admin", "published": True }
]


# class Post(BaseModel):
#     id: int
#     title: str
#     content: str
#     author: str = "Admin"
#     published: bool = True
#     # rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/greet")
def greet_ibrahim():
    return {"greetings": "Hello there!, Ibrahim!!!"}


@app.get("/posts")
def get_posts():
    return {
        "data": all_posts
    }


@app.post("/posts")
def create_post(payload: dict = Body(...)):
    print("post payload", payload)
    return {"data": payload}