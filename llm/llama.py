from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import StreamingStdOutCallbackHandler

def create_llama(model_path: str) -> LlamaCpp:
    return LlamaCpp(
        model_path=model_path,
        temperature=0.3,
        max_tokens=500,
        n_ctx=32000,
        callbacks=[StreamingStdOutCallbackHandler()],
        verbose=False,

        # Uncomment the following line if you want to use GPU acceleration
        # n_gpu_layers=16,
    )