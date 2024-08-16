from langchain.chains.summarize import load_summarize_chain
from langchain_community.llms.ollama import Ollama
from langchain.schema import Document
from requests.exceptions import RequestException
# Load the language model
llm = Ollama(model="qwen2:1.5b")


def invoke(document):
    
    paragraph_docs = Document(page_content= document)
    print(paragraph_docs) 
    docs = [paragraph_docs]
    chain_refine = load_summarize_chain(llm, chain_type = "stuff")
    result_refine = chain_refine.invoke(docs)
    try:
        result_refine = chain_refine.invoke(docs)
        return result_refine['output_text']
    except RequestException as e:
        # Log the error or handle it as necessary
        return f"An error occurred: {str(e)}"
   

# result = invoke(small_paragraph)
# print(result)



