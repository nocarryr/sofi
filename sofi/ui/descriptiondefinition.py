from .element import Element

class DescriptionDefinition(Element):
    """Implements <dd> tag"""

    html_tag = 'dd'
    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<DescriptionDefinition>"
