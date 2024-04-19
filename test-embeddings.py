from gerty.vectorstore import FAISS_NORM
from gerty.embedding import get_embeddings

embedding_model = get_embeddings()
test_db = FAISS_NORM.load_local('./test-db/', embedding_model)

test_close = "Who is sony?"

out = test_db.similarity_search_with_score(
    test_close
)

out = [ j for (_,j) in out ]
print(out)
