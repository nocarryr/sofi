from .element import Element

class ListItem(Element):
    """Implements <li> tag"""

    html_tag = 'li'
    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text

    def __repr__(self):
        return "<ListItem>"
