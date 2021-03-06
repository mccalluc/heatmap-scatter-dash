import re

# from whoosh.fields import NGRAMWORDS, TEXT, Schema
# from whoosh.filedb.filestore import RamStorage
# from whoosh.qparser import OrGroup, QueryParser
# from whoosh.query import Every


class SimpleIndex():
    '''
    Right now we're just doing substring search because indexing
    made startup too slow, but making sure it is done through
    this interface makes it easier for us to plug in something better,
    at some point.
    '''

    def __init__(self):
        self._index = {}

    def add_document(self, doc_id, document):
        self._index[doc_id] = document

    def search(self, substrings):
        if substrings:
            matches = []
            for substring in re.split('\s+', substrings.strip()):
                matches.extend([
                    id for (id, document) in self._index.items()
                    if substring in document
                ])
            return matches
        else:
            return self._index.copy()


# commented out in requirements.txt:

# class WhooshIndex():
#     # Search might be fast, but indexing is too slow to be useful.
#
#     def __init__(self):
#         storage = RamStorage()
#         schema = Schema(gene_id=TEXT(stored=True),
#                         gene_tokens=NGRAMWORDS(stored=False, minsize=1))
#         self._index = storage.create_index(schema)
#
#     def add(self, *gene_ids):
#         writer = self._index.writer()
#         for gene_id in gene_ids:
#             writer.add_document(gene_id=gene_id,
#                                 gene_tokens=gene_id)
#         writer.commit()
#
#     def search(self, substrings):
#         with self._index.searcher() as searcher:
#             parser = QueryParser('gene_tokens', self._index.schema,
#                                  group=OrGroup)
#             query = parser.parse(substrings) if substrings else Every()
#             results = searcher.search(query)
#             return [result['gene_id'] for result in results]
