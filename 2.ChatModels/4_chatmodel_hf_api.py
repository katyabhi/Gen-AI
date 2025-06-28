from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id=""tiiuae/falcon-7b-instruct"",
    task="text-generation"
    #huggingfacehub_api_token=os.getenv("KEY ")
)

model=ChatHuggingFace(llm=llm)

result=model.invoke("What is the capital of India")

print(result)