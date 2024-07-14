from langchain_community.vectorstores import Qdrant
from langflow.base.vectorstores.model import LCVectorStoreComponent
from langflow.field_typing import VectorStore
from langflow.io import (
    HandleInput,
    StrInput,
    SecretStrInput,
    DataInput,
)
from langflow.schema import Data
from langchain.embeddings.base import Embeddings


class QdrantVectorStoreComponent(LCVectorStoreComponent):
    display_name = "Qdrant"
    description = "Qdrant Vector Store with search capabilities"
    documentation = "https://python.langchain.com/docs/modules/data_connection/vectorstores/integrations/qdrant"
    icon = "Qdrant"

    inputs = [
        StrInput(
            name="collection_name",
            display_name="Collection Name", 
            required=True
        ),
        SecretStrInput(name="api_key", display_name="API Key", advanced=True),
        StrInput(
            name="url",
            display_name="URL",
            value="http://localhost:6333",
            advanced=True,
            required=True
        ),
        StrInput(
            name="content_payload_key", 
            display_name="Content Payload Key",
            value="page_content", 
            advanced=True
        ),
        StrInput(name="metadata_payload_key",
                 display_name="Metadata Payload Key", value="metadata", advanced=True),
        DataInput(
            name="ingest_data",
            display_name="Ingest Data",
            is_list=True,
        ),
        HandleInput(name="embedding", display_name="Embedding",
                    input_types=["Embeddings"]),
    ]

    def build_vector_store(self) -> VectorStore:
        return self._build_qdrant()

    def _build_qdrant(self) -> Qdrant:
        qdrant_kwargs = {
            "collection_name": self.collection_name,
            "content_payload_key": self.content_payload_key,
            "metadata_payload_key": self.metadata_payload_key,
        }

        server_kwargs = {
            "api_key": self.api_key if self.api_key else None,
            "url": self.url if self.url else None,
        }

        server_kwargs = {k: v for k,
                         v in server_kwargs.items() if v is not None}
        
        documents = []

        for _input in self.ingest_data or []:
            if isinstance(_input, Data):
                documents.append(_input.to_lc_document())
            else:
                documents.append(_input)
        
        if not isinstance(self.embedding, Embeddings):
            raise ValueError("Invalid embedding object")

        if documents:
            qdrant = Qdrant.from_documents(
                documents, embedding=self.embedding, prefer_grpc=False, **qdrant_kwargs, **server_kwargs)
            return qdrant

        else:
            raise ValueError("No documents")