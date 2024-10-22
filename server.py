from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, SystemMessage

import os
import dotenv
from dotenv import load_dotenv, find_dotenv


_ = load_dotenv(find_dotenv())


groq_api_key = os.environ.get("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set. Please provide it in the environment.")

app = FastAPI()



class ChatRequest(BaseModel):
    user_input: str
    language: str 


model = ChatGroq(model="llama3-8b-8192", api_key=groq_api_key)

# Define the prompt template
prompt_template = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a translator. Translate the following text into {language}."),
    HumanMessage(content="{user_input}")
])

# Initialize the output parser
parser = StrOutputParser()

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        
        messages = [
            SystemMessage(content=f"Translate the following from English into {request.language}."),
            HumanMessage(content=request.user_input)
        ]

        result = model.invoke(messages)
        parsed_result = parser.parse(result)

        return {"result": parsed_result.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
         
         
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
