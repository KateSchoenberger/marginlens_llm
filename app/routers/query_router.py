from fastapi import APIRouter
from core.retrieval import retrieve_and_generate

router = APIRouter(prefix="/query", tags=["Query"])

@router.post("/")
def query_financial_data(request: dict):
    query = request.get("query", "")
    if not query:
        return {"error": "No query provided."}
    response = retrieve_and_generate(query)
    return {"response": response}
