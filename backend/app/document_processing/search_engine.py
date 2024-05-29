from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser

def create_index(index_dir):
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
    index = create_in(index_dir, schema)
    return index

def add_document(index, title, path, content):
    writer = index.writer()
    writer.add_document(title=title, path=path, content=content)
    writer.commit()

def search_index(index, query_str):
    with index.searcher() as searcher:
        query = QueryParser("content", index.schema).parse(query_str)
        results = searcher.search(query)
        return results
