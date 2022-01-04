from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from typing import Optional

app = FastAPI()

all_posts = [
    {"id":1, "title": "My first", "content": "This is the very first post using fast api, pydantic, postman etc.", "author": "Ibrahim", "published": False},
    {"id":2, "title": "Postiscus", "content": "Post no 2 should be the most entertaining and exciting due to a number of irreconciliable factors", "author": "admin", "published": True }
]

def find_post(id):
    return [i for i in all_posts if int(id) == i["id"]]


class Post(BaseModel):
    title: str
    content: str
    author: str = "Admin"
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/greet")
def greet_ibrahim():
    return {"greetings": "Hello there!, Ibrahim!!!"}


# get all posts
@app.get("/posts")
def get_posts():
    return {
        "data": all_posts
    }


# Create a single post
@app.post("/posts")
def create_post(payload: Post):
    # payload["id"] = randrange(1, 500)
    payload_dict = payload.dict()
    payload_dict["id"] = randrange(1, 500)
    all_posts.append(payload_dict)
    return {"all_posts": all_posts}


# Get a single post
@app.get("/posts/{id}")
def get_single_post(id: int):
    data = find_post(id)
    return {"data": data}