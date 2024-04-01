# Document Summary

**Motivation**

This is project related to our bachelor thesis. As a part of our project, we are to create summaries for tender competitions. These competitions come with a varying amount of documents, with varying length, file format and quality.

This project will be preparatory work for our bachelor project. We wish to explore different ways to summarize text using commercially available LLMs (Large Language Models). Since we do not know the documents we are to summarize, no specific cleaning or preprocessing can be done, everything has to be generic.

## Setup

You will need:
- Python 3.10 or higher
- An OpenAI API key, which can be aquired [here](https://openai.com/blog/openai-api). You will also need credits on your account.
- A .env file in the root of the project, containing your OpenAI API key. See [.env.example](.env.example).

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
