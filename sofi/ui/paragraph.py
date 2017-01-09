from .element import Element

class Paragraph(Element):
    """Implements <p> tag"""

    html_tag = 'p'
    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<Paragraph>"
