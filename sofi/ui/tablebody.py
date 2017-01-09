from .element import Element

class TableBody(Element):
    """Implements the <tbody> tag"""

    html_tag = 'tbody'
    def __init__(self, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

    def __repr__(self):
        return "<TableBody>"
