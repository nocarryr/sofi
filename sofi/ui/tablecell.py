from .element import Element

class TableCell(Element):
    """Implements <td> tag"""

    html_tag = 'td'
    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<TableCell>"
