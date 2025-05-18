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
    path        = "/api/v1/embed_documents/{model_name:path}",
    status_code = status.HTTP_200_OK,
    tags        = ["api", "v1", "embed_documents"]
)
async def embed_documents(request: Request) -> Response:
    payload: dict       = await request.json()
    embedder: Embedder  = request.app.state.embedder
    model_name: str     = request.path_params["model_name"]

    # validate payload
    if "inputs" not in payload:
        return Response(content="inputs field is required", status_code=status.HTTP_400_BAD_REQUEST)
    if model_name != embedder.model_name:
        return Response(content="invalid model name", status_code=status.HTTP_400_BAD_REQUEST)

    texts = payload["inputs"]

    embeddings = embedder.embed_documents(texts)

    return embeddings
