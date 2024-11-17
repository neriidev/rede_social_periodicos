from scrapper import get_text_from_url
from langchain_core.massages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

def get_response_from_openai(message):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    response = llm.invoke(message)

def documentation_tool(url: str, question: str) -> str:
    context = get_text_from_url(url)

    messages = [
        SystemMessage(content="Qualquer problema consulte a documentação"),
        HumanMessage(content=f"Documentação: {context} \n\n {question}")
    ]

    response = get_response_from_openai(message)

    return response

    