from langchain_openai import ChatOpenAI

def create_chatgpt() -> ChatOpenAI:
    """Create a ChatGPT model instance."""
    return ChatOpenAI(
        model_name="gpt-4o",
        temperature=0.3,
        max_tokens=500,
    )