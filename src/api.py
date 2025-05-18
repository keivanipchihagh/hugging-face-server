from fastapi import APIRouter, status, Request, Response

from huggingface import Embedder

router = APIRouter()

@router.get(
    path        = "/health",
    status_code = status.HTTP_200_OK,
    tags        = ['health'],
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

    if "inputs" not in payload:
        return Response(
            content = "inputs field is required",
            status_code = status.HTTP_400_BAD_REQUEST,
        )

    texts = payload["inputs"]

    embedder: Embedder = request.app.state.embedder
    embeddings = embedder.embed_documents(texts)

    return embeddings
