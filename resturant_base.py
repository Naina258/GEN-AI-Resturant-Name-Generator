from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
from secret_key import open_ai_secret_key

import os
os.environ['OPENAI_API_KEY']= open_ai_secret_key

llm = ChatOpenAI(temperature=0.8)

def generate_resturant_name_and_items(cuisine):
    #Chain 1: Resturant name
    prompt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template= "I want to open a resturant for {cuisine}. Suggest one name."
)

    new_chain =LLMChain(llm=llm, prompt=prompt_template_name,output_key="resturant_name")

    #Chain 2: Menu Items
    prompt_template_food = PromptTemplate(
        input_variables=['resturant_name'],
        template= "Suggest Items for {resturant_name}. Separate them with a comma."
    )
    food_items_chain =LLMChain(llm=llm, prompt=prompt_template_food,output_key="menu_items")

    chain = SequentialChain(
        chains=[new_chain, food_items_chain],
        input_variables =['cuisine'],
        output_variables=['resturant_name', 'menu_items']
      )

    
    response = chain({'cuisine':cuisine}) 

    return response

