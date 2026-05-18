from fastapi import APIRouter 

from app.models.schemas import QueryRequest, QueryResponse
from app.services.rag_service import ask_question

router = APIRouter()

@router.post("/query", response_model = QueryResponse)

def query_rag(request: QueryRequest):

    answer = ask_question(request.question)

    return QueryResponse(answer=answer)