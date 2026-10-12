from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class PostRequest(BaseModel):
    title:str
    content:str


@app.post("/post/{post_id}")
def checkPost(
    post_id:int,
    data:PostRequest,
    notify:bool = False
):
    return{"post_id":post_id,
           "title":data.title,
           "content":data.content,
           "notify":notify}

    


