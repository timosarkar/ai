from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi3",
    temperature=0
)

messages = [
    ("human", "hello, how are you?"),
]

run = llm.invoke(messages)
print(run.content)