

import pytest

from osp.citations.utils import get_min_freq, tokenize_field


def test_queries(add_text):

    """
    Text#queries should generate a set of Elasticsearch queries.
    """

    text = add_text(title='Anna Karenina', authors=['David William McClure'])

    queries = text.queries

    for q in [
        'anna karenina david william mcclure',
        'anna karenina david',
        'anna karenina william',
        'anna karenina mcclure',
    ]:

        assert (q, get_min_freq(tokenize_field(q))) in queries
