

import sys
import re
import numpy as np
import hashlib

from osp.common.config import config
from osp.common.utils import query_bar
from osp.common.models.base import BaseModel
from osp.citations.hlom_corpus import HLOM_Corpus
from osp.citations.utils import tokenize_query
from pymarc import Record
from clint.textui.progress import bar

from peewee import CharField


class Text(BaseModel):


    title       = CharField()
    author      = CharField()
    publisher   = CharField(null=True)
    date        = CharField(null=True)
    journal     = CharField(null=True)


    class Meta:
        database = config.get_table_db('text')


    @classmethod
    def ingest_hlom(cls, page_size=10000):

        """
        Ingest HLOM MARC records.

        Args:
            page_size (int): Batch-insert page size.
        """

        pass


    @classmethod
    def ingest_jstor(cls, page_size=10000):

        """
        Ingest JSTOR records.

        Args:
            page_size (int): Batch-insert page size.
        """

        pass


    @property
    def hash(self):

        """
        Create a hash that tries to merge together differently-formatted
        editions of the same text.

        Returns:
            str: The deduping hash.
        """

        tokens = tokenize_query(self.title, self.author)

        # Hash the tokens.
        sha1 = hashlib.sha1()
        sha1.update(' '.join(tokens).encode('ascii', 'ignore'))
        return sha1.hexdigest()


    @property
    def query(self):

        """
        Build an Elasticsearch query string.

        Returns:
            str|None: "[title] [author]", or None if invalid.
        """

        tokens = tokenize_query(self.title, self.author)

        return ' '.join(tokens)
