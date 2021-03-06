

from osp.corpus.models import Document_Text
from osp.fields.models import Subfield
from osp.fields.models import Subfield_Document
from osp.fields.utils import crunch


def doc_to_fields(doc_id, radius=100):

    """
    Search for field / department codes in a document.

    Args:
        doc_id (int)
        radius (int)
    """

    doc_text = Document_Text.get(Document_Text.document==doc_id)

    # Search for each field.
    for subfield in Subfield.select():

        match = subfield.search(doc_text.text)

        # If found, link field -> doc.
        if match:

            # Slice out the snippet.
            i1 = max(match.start() - radius, 0)
            i2 = min(match.end() + radius, len(doc_text.text))
            snippet = doc_text.text[i1:i2]

            Subfield_Document.create(
                subfield=subfield,
                document=doc_text.document,
                offset=match.start(),
                snippet=crunch(snippet),
            )
