#! /usr/bin/env python

import click
from elasticsearch_dsl import Search  # type: ignore
from elasticsearch_dsl.query import Match, MatchAll, Ids, Query, MultiMatch  # type: ignore
from elasticsearch_dsl.connections import connections  # type: ignore


def search(index: str, query: Query, top_k: int = 5) -> None:
    s = Search(using="default", index=index).query(query)[
        :top_k
    ]  # initialize a query and return top k results
    response = s.execute()
    print("ID", "SCORE", "PMC", "TITLE", sep="\t")
    for hit in response:
        print(hit.meta.id, round(hit.meta.score, 2), hit.pmc, hit.title, sep="\t")


@click.command()
@click.argument("query", type=click.STRING)
@click.argument("index", type=click.STRING, default="cord_askme_idx")
def main(query: str, index: str):
    connections.create_connection(hosts=["localhost"], timeout=100, alias="default")
    q_multi = MultiMatch(query=query, fields=["title", "abstract"])
    search(index, q_multi)


if __name__ == "__main__":
    main()
