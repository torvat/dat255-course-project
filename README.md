# Doucment Summary

**Motivation**

This is project related to our bachelor theises. As a subtask, we are to create summaies for tender competitions.

So, for this project, we are exploring the summarzation problem with llms.

## Setup

All you need, is python 3.10 or higher, and an openai account with credits. You will need to create a .env file in to root of the project, and add it to a variable named OPENAI_API_KEY.

You may copy from .env.example

## Document Summaries with langchain

&nbsp; In this project we have been attacking the summarization problem with llms

**What is the problem?**

&nbsp; Most commercial llms have an token limit. This token limit gives an restriction on how much input you can give the llm, and how much output you can expect back.

Here is where the problem with summarzaion comes in. What do you do if you want to summarize a large document with 500 or 700 pages, or maybe you have several documents to combine and summarize? This overexceeds the token limit scale if you want to do this in one single call to the llm.

This means we need a way to divide the documents into smaller pieces, summarize each piece, and merge them together in the end to create one summary. For this approch we can use the langchain.

### Stuff documents chain

Stuff document chain is a method used for smaller chain problems. Typecally you will give the llm some context, and prompt the llm for the content. This can also be used for summarization. How ever this is not good approch if you have large texts, because the stuff documents only query the api, with one api call, and dont divide it into pieces.

![img](./assets/stuff_chain.jpg)

### Map reduce documents chain

Map reduce documents chain is another common approch for summarizing documents, and is more suited for this task. Remember that the solution for the summarzaiton problem is to divide the document into smaller pieces, or chunks, then summarize each chunk, combine them into one summary that the token limit can handle, and return that. That is exactly what MapReduceDocumentChain achives.

![img](./assets/map_reduce_chain.webp)

## K-clustering

TBA
