from langchain_community.llms import LlamaCpp
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please work everything out in a step by step way to be sure we have the right answer."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}"),
    ]
)

n_gpu_layers = 16

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

llm = LlamaCpp(
    model_path="/home/mohammed/.cache/huggingface/hub/models--TheBloke--Mistral-7B-Instruct-v0.2-GGUF/snapshots/3a6fbf4a41a1d52e415a4958cde6856d34b2db93/mistral-7b-instruct-v0.2.Q5_K_M.gguf",
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    callback_manager=callback_manager,
    n_gpu_layers=n_gpu_layers,
    verbose=True,
)

llm_chain = prompt | llm

chain_with_history = RunnableWithMessageHistory(
    llm_chain,
    lambda session_id: SQLChatMessageHistory(
        session_id=session_id,
        connection="sqlite:///chat_history.db"
    ),
    input_messages_key="question",
    history_messages_key="history"
)

config = {"configurable": {"session_id": "test_session_002"}}

response = chain_with_history.invoke(
    {"question": "What was my previous question?"}, 
    config=config
)

print(response)