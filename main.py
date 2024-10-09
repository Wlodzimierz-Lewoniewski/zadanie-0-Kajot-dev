import re
from typing import NamedTuple

number_pattern = re.compile(r"\d+")
character_normalizer = re.compile(r"[^\w\s]*")
whitespace_selector = re.compile(r"\s+")


class QueryInput(NamedTuple):
    parsed_documents: list[list[str]]
    queries: list[str]


def parse_input_1() -> QueryInput | None:

    number_of_documents: int = int(input())
    
    if number_of_documents <= 0:
        return None

    documents = []
    
    for i in range(number_of_documents):
        documents.append(input())
    
    normalized_documents = []
    
    for doc in documents:
        # remove illegal characters, strip and lower
        normalized = character_normalizer.sub("", doc).strip().lower()
        # remove repeated whitespace
        normalized = whitespace_selector.sub(" ", normalized)
        normalized_documents.append(
            normalized
        )
    
    parsed_documents = []
    
    for doc in normalized_documents:
        parsed_documents.append(doc.split())
    
    number_of_queries = int(input())
    
    queries = []
    
    for i in range(number_of_queries):
        queries.append(input())
    
    queries = [query.strip().lower() for query in queries]
    
    return QueryInput(
        parsed_documents=parsed_documents,
        queries=queries
    )


def zadanie_1():
    
    input_data = parse_input_1()
    
    query_ranking = {}
    
    for query in input_data.queries:
        
        query_counts = []
        
        for doc in input_data.parsed_documents:
            query_hits = doc.count(query)
            query_counts.append(query_hits)

        # remove items with 0 hits
        sortable_query_counts = list(filter(lambda d: d[1] != 0, enumerate(query_counts)))
        # sort by number of hits
        sorted_query_counts = sorted(sortable_query_counts, key=lambda d: d[1], reverse=True)
        # extract indexes of documents
        indexed_query_results = list(map(lambda d: d[0], sorted_query_counts))
    
        query_ranking[query] = indexed_query_results
    
    for query in input_data.queries:
        print(query_ranking[query])
    
    
def main():
    zadanie_1()


if __name__ == '__main__':
    main()