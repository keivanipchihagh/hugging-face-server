from typing import List
from sentence_transformers import SentenceTransformer


class Embedder:

    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
        self.model      = SentenceTransformer(model_name, trust_remote_code=True)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        arrays = self.model.encode(texts)
        return arrays.tolist()
