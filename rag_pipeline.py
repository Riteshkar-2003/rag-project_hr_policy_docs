from document_loader import loader_documents
from text_splitter import split_documents
from embedding import get_embeddings
from vector_store import create_vector_store
from retriever import get_retriever
from llm import get_llm
from prompt import get_prompt


class RAG_Pipeline:

    def __init__(self):
        documents = loader_documents("documents/USA_Employee_Handbook-Freely_Available.pdf")
        chunks = split_documents(documents)
        embeddings = get_embeddings()
        vectorstore = create_vector_store(
            chunks,
            embeddings
        )
        self.retriever = get_retriever(
            vectorstore
        )
        self.llm = get_llm()
        self.prompt = get_prompt()


    def ask(self, question):
        docs = self.retriever.invoke(question)
        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )
        messages = self.prompt.invoke({
            "context": context,
            "question": question
        })
        response = self.llm.invoke(messages)
        return response.content