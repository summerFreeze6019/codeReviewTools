# GERTY

This repo is a test repo for me to get familiar with Langchain and LLM type workflows. The purpose of this repo is to show how one might use Llama 2 to do Retrieval Augmented Generation. 

### RAG

RAG is the process of augmenting text generation by using a vector store of document embeddings. During generation time, we take the prompt and encode it into some embedding. We then perform a fast vector search in our document store and find the "nearest neighbours". Those neighbours are then inserted into the final prompt for generation. 

RAG enables us to maintain some level of lucidity in our model generation text and enables us to reference direct textual information in our generation. 


### Instructions on how to run

***TODO: Update readme with instructions on how to run***

### NOTE

This does not necessarily mean that you can trust the model more. Models are still able to hallucinate and return false answer. Caution is advised in accepting model answers. As they say "Trust but verify.".
