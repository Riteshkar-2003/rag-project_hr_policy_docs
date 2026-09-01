from rag_pipeline import RAG_Pipeline


rag = RAG_Pipeline()
while True:

    question = input("\n Ask a question: ")

    if question.lower()=="exit":
        print("Good Byee!")
        break

    try:
        answer = rag.ask(question)
        print("\n Answer:")
        print(answer)

    except Exception as e:
        print("Error:", e)