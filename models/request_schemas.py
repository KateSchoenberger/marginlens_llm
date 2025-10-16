from pydantic import BaseModel, Field
from typing import List, Optional

class QueryRequest(BaseModel):
    query_text: str = Field(..., description="User input for margin insights")
    top_k: Optional[int] = Field(5, description="Number of top results to return")
    user_id: Optional[str] = Field(None, description="Optional user identifier")
