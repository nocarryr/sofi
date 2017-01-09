from .element import Element

class Heading(Element):
    """Implements heading tags using size attribute: <h1>, <h2>, etc."""

    def __init__(self, size=1, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.size = size

        if text:
            self._children.append(text)

    @property
    def html_tag(self):
        return 'h{self.size}'.format(self=self)

    def __repr__(self):
        return "<Heading(size=" + str(self.size) + ")>"
