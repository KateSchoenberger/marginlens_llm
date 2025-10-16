from fastapi import APIRouter, Query
from app.core.faiss_engine import retrieve_context
from app.core.openai_engine import generate_response

router = APIRouter(prefix="/query", tags=["Margin Insights"])

@router.get("/")
async def get_margin_insight(query: str = Query(..., description="Enter a financial question")):
    context = retrieve_context(query)
    response = generate_response(query, context)
    return {"query": query, "response": response}
