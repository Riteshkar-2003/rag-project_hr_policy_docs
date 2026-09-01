from langchain_core.prompts import ChatPromptTemplate

def get_prompt():
    prompt=ChatPromptTemplate.from_template("""
    You are a helpful AI assistant.

    Answer the question using only the provided context.

    If the answer is not available in the context,
    say "I don't know based on the provided documents."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    )

    return prompt
    