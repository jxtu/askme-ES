from elasticsearch_dsl import Search  # type: ignore
from elasticsearch_dsl.query import Match, MatchAll, Ids, Query  # type: ignore
from elasticsearch_dsl.connections import connections  # type: ignore


def search(index: str, query: Query) -> None:
    s = Search(using="default", index=index).query(query)[
        :5
    ]  # initialize a query and return top five results
    response = s.execute()
    for hit in response:
        print(
            hit.meta.id, hit.meta.score, hit.title, sep="\t"
        )  # print the document id that is assigned by ES index, score and title


if __name__ == "__main__":
    connections.create_connection(hosts=["localhost"], timeout=100, alias="default")

    q_match_all = MatchAll()  # a query that matches all documents
    q_basic = Match(
        title={"query": "clinical"}
    )  # a query that matches "clinical" in the title field of the index, using BM25 as default
    q_match_ids = Ids(values=[0, 1, 2])  # a query that matches ids

    search(
        "test_askme_cord", q_basic
    )  # search, change the query object to see different results
