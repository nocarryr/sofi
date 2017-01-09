from .element import Element

class TableHead(Element):
    """Implements the <thead> tag"""

    html_tag = 'thead'
    def __init__(self, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

    def __repr__(self):
        return "<TableHead>"
