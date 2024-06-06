from fastapi import FastAPI, Query
from wisphper_from_HF import transcibe

app = FastAPI()

@app.get("/" )
async def root(link: str ):
    temp = transcibe(link)
    return {"answer" :temp[0] , "Original Len":temp[1], "Summarized  len":temp[2] }