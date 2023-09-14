import os
from apikey import apikey_GPT

from googlesearch import search

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory

os.environ['OPENAI_API_KEY'] = apikey_GPT

st.title('NextSteps')
prompt = st.text_input('Enter in a skill and we can tell you the first steps and topics you\'ll need to learn it!')

# Prompt template
skills_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'What are some beginner skills needed to learn {topic} in order of importance and principles? Answer in a comma seperated list'
)

plan_template = PromptTemplate(
    input_variables = ['skills', 'topic'],
    template = 'In the context of learning {topic}, write me short paragraph summary of how to learn these topics: {skills}. Make sure to mention the links to resources at the bottom'
)

# Memory
skills_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
plan_memory = ConversationBufferMemory(input_key='skills', memory_key='chat_history')

# LLMs
llm = OpenAI(temperature=0.9)
skills_chain = LLMChain(llm=llm, prompt=skills_template, output_key='skills', memory=skills_memory)
plan_chain = LLMChain(llm=llm, prompt=plan_template, output_key='plan', memory=plan_memory)

if prompt:

    skills = skills_chain.run(prompt)
    plan = plan_chain.run(skills=skills, topic=prompt)
    skill_list = skills.split(",")

    url_dict = {}

    for skill in skill_list:
        query = prompt + " how to get started with " + skill
        url_dict[skill] = search(query, tld="com", num=3, stop=3, pause=2)

    st.write(plan)

    for key, value in url_dict.items():
        st.write(key.capitalize())
        result = ""

        for i in value:
            result += "- " + i + "\n"

        st.markdown(result)

    with st.expander('Skills History'):
        st.info(skills_memory.buffer)

    with st.expander('Plan History'):
        st.info(plan_memory.buffer)