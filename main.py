from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import StreamingStdOutCallbackHandler
from services.recommender import CareerRecommendationSystem

def main():
    llm = LlamaCpp(
        model_path="/home/mohammed/.cache/huggingface/hub/models--TheBloke--Mistral-7B-Instruct-v0.2-GGUF/snapshots/3a6fbf4a41a1d52e415a4958cde6856d34b2db93/mistral-7b-instruct-v0.2.Q5_K_M.gguf",
        temperature=0.3,
        max_tokens=500,
        n_ctx=2048,
        callbacks=[StreamingStdOutCallbackHandler()],
        n_gpu_layers=16,
        verbose=False,
    )
    
    career_system = CareerRecommendationSystem(llm)
    
    sample_conversation = """
    User: I’m not really sure what I want to do, but I guess I like working with people.  
    Counselor: Okay, can you tell me about any hobbies or skills you have?  
    User: Not much really... I just hang out with friends and watch movies.  
    Counselor: Any school subjects or activities you enjoy?  
    User: I don’t know... nothing in particular.  
    """
    
    result = career_system.full_recommendation_pipeline(sample_conversation)
    
    if result["status"] == "needs_clarification":
        # print("Need more information. Questions to ask:")
        # print(result["questions"])
        pass
    else:
        print("Career Recommendations:")
        for explanation in result["explanations"]:
            print(f"\n--- {explanation['career_path']} ---")
            print(f"Why it matches: {explanation['match_reason']}")
            print(f"Explanation: {explanation['explanation']}")

if __name__ == "__main__":
    main()