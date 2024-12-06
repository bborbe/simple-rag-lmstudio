from langchain.embeddings import HuggingFaceBgeEmbeddings

from langchain.vectorstores import Chroma
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from torch import torch

data_directory = "./content"
embedding_directory = "./content/chroma_db"

embedding_db = None


def embed():

    print("\nCalculating Embeddings\n")

    # Load the text from the data directory
    loader = DirectoryLoader(data_directory,
                             glob="*.txt",
                             loader_cls=TextLoader)

    documents = loader.load()

    # Split the data into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                                   chunk_overlap=50)

    chunks = text_splitter.split_documents(documents)

    # Load the huggingface embedding model
    model_name = "BAAI/bge-base-en"
    # set True to compute cosine similarity
    encode_kwargs = {'normalize_embeddings': True}

    device = torch.device(
        "mps") if torch.backends.mps.is_available() else torch.device("cpu")
    print(f"Using device: {device}")

    embedding_model = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs={'device':  str(device)},
        # model_kwargs={'device': 'cuda'},
        encode_kwargs=encode_kwargs
    )

    embedding_db = Chroma.from_documents(
        chunks, embedding_model, persist_directory=embedding_directory)

    print("Embeddings completed")
