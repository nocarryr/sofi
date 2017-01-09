from .element import Element

class TableFooter(Element):
    """Implements the <tfoot> tag"""

    html_tag = 'tfoot'
    def __init__(self, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

    def __repr__(self):
        return "<TableFooter>"
