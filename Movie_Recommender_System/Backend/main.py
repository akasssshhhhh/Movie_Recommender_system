from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import uvicorn

app = FastAPI()

df = pd.read_pickle('data/finalmovies.pkl') 

def normalize_title(title):
    return title.strip().lower().replace(".", "").replace(":", "").replace("-", "")

class MovieRequest(BaseModel):
    title: str
    top_n: int = 5

@app.post("/recommend")
def recommend_movies(data: MovieRequest):
    normalized_query_title = normalize_title(data.title)
    query_idx = df[df['normalized_title'] == normalized_query_title].index

    if query_idx.empty:
        return {"error": "Movie not found."}

    query_idx = query_idx[0]
    query_embedding = np.array(df['embeddings'][query_idx]).reshape(1, -1).astype('float32')
    similarities = cosine_similarity(query_embedding, np.array(df['embeddings'].tolist()))
    top_indices = np.argsort(similarities[0])[::-1][1:data.top_n + 1]

    similar_movies = [
        {
            "title": df.iloc[i]["title"],
            "poster": df.iloc[i]["poster_path"] 
        }
        for i in top_indices
    ]

    return {"recommendations": similar_movies}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)