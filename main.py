from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

app = FastAPI()
client = MongoClient('localhost', 27017)
db = client['socialmedia_db']
processed_collection = db['processed_data']

@app.get("/")
def read_root():
    return {"message": "Welcome to the Social Media Data API"}

@app.get("/data/{data_type}")
def read_data(data_type: str):
    data = list(processed_collection.find({'type': data_type}))
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
