from fastapi import APIRouter, status, Request, Response

from huggingface import Embedder

router = APIRouter()

@router.get(
    path        = "/api/health",
    status_code = status.HTTP_200_OK,
    tags        = ['api', 'health'],
)
async def health():
    return "OK"


@router.post(
    path        = "/api/v1/embed_documents",
    status_code = status.HTTP_200_OK,
    tags        = ["api", "v1", "embed_documents"]
)
async def embed_documents(request: Request) -> Response:
    payload: dict = await request.json()

    texts = payload["texts"]

    embedder: Embedder = request.app.state.embedder
    embeddings = embedder.embed_documents(texts)

    return embeddings
