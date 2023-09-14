# NextSteps
Learn anything from ONE WORD! This app only needs to know what skill you want to master, then using OpenAI's GPT API, LangChain, and some light web scraping, it will give you the resources
you need to put you in the right direction in your learning journey.

## Introduction

For this project, I was learning how to use LangChain as a way to interact with different APIs and create a pipeline with GPT for a seamless user experience.
We've all used ChatGPT to ask detailed questions and follow up questions to learn new skills, but the finer details in the output can sometimes be partly or fully hallucinated.
The approach in this project is to ask GPT about which basics, fundamentals, principles, and first steps we would need to take to learn a skill,
then by utilizing web scraping, we can leave the high level details to GPT-3.5 while searching the web for real-life related resources created by people on how to actually learn these skills.
This way, the user can input just one word and receive many resources to point them in the right direction!

This project leverages StreamLit as the front end for creating an interactive web application, while utilizing LangChain and OpenAI's GPT-3.5 API for natural language generation.
In the future, I plan to incorporate Weaviate or Pinecone to enable efficient vector storage and retrieval of data.

## Features

- StreamLit-based web application for the front end.
- GPT integrated with LangChain for advanced language processing and generation.
- Planned integration with Weaviate or Pinecone for Vector Stores.

### Prerequisites

- Python 3.x
- StreamLit
- LangChain
- OpenAI GPT API
- Wikipedia API

### Demo
Online demo coming soon!

### To install locally
1. Install prerequisites using ```pip install streamlit langchain openai wikipedia```
2. Add your OpenAI API key to ```apikey.py``` as ```apikey_GPT="your API Key Here"```
