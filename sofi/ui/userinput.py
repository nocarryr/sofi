from .element import Element

class UserInput(Element):
    """Implements <kbd> tag"""

    html_tag = 'kbd'
    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<UserInput>"
