
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv(override=True)
def get_model_inference():
  chat = ChatGroq(temperature=0, groq_api_key=os.environ["GROQ_API_KEY"], model_name="mixtral-8x7b-32768")
  system = "You are a helpful assistant."
  human = "{text}"
  prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
  chain = prompt | chat
  result=chain.invoke({"text": "What is Generative AI,explain in two lines?."})
  print(result)

if __name__=="__main__":
    print("<<<START OF TEXT GENERATION>>>>")
    print("<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>")
    get_model_inference()
    print("<<<END OF TEXT GENERATION>>>>")
    print("<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>")