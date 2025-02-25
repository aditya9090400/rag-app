from sklearn.feature_extraction.text import TfidfVectorizer
from rank_bm25 import BM25Okapi
import json

def retrieve_documents(query: str, docs):
    # Prepare BM25 model
    tokenized_corpus = [doc["content"].split() for doc in docs]
    bm25 = BM25Okapi(tokenized_corpus)
    
    # Tokenize the query
    tokenized_query = query.split()
    scores = bm25.get_scores(tokenized_query)

    # Rank documents
    ranked_docs = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
    return ranked_docs[:3]  # Return top 3
