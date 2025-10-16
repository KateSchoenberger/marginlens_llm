from pydantic import BaseModel
from typing import List

class ResultItem(BaseModel):
    document_id: str
    content: str
    score: float

class QueryResponse(BaseModel):
    query_text: str
    results: List[ResultItem]
    message: str = "Success"
