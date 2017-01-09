from .element import Element

class TableRow(Element):
    """Implements <tr> tag"""

    html_tag = 'tr'
    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<TableRow>"
