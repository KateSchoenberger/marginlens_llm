from app.core.faiss_engine import FaissEngine
from app.core.openai_engine import OpenAIEngine
from app.models.response_schemas import QueryResponse, ResultItem

class MarginService:
    def __init__(self, faiss_engine: FaissEngine, openai_engine: OpenAIEngine):
        self.faiss_engine = faiss_engine
        self.openai_engine = openai_engine

    def get_margin_insights(self, query_text: str, top_k: int = 5) -> QueryResponse:
        # Step 1: Retrieve relevant docs from FAISS
        docs = self.faiss_engine.search(query_text, top_k=top_k)

        # Step 2: Optionally process or summarize with OpenAI
        enriched_docs = []
        for doc in docs:
            summary = self.openai_engine.summarize(doc['content'])
            enriched_docs.append(ResultItem(
                document_id=doc['id'],
                content=summary,
                score=doc['score']
            ))

        return QueryResponse(query_text=query_text, results=enriched_docs)
