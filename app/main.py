from fastapi import FastAPI
from app.routers import margin_insights

app = FastAPI(title="MarginLens API")

app.include_router(margin_insights.router)

@app.get("/")
def root():
    return {"message": "Welcome to MarginLens API"}