from langchain_google_genai import GoogleGenerativeAI

def create_gemini():
    """Create a Gemini model instance."""
    return GoogleGenerativeAI(
        model_name="gemini-2.0-flash",
        temperature=0.3,
    )