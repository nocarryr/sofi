from .element import Element

class Anchor(Element):
    """Implements the <a> tag"""

    html_tag = 'a'
    def __init__(self, text=None, href="#", cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.href = href

        if text:
            self._children.append(text)

    def _get_all_attrs(self):
        attrs = super()._get_all_attrs()
        attrs['href'] = self.href
        return attrs

    def __repr__(self):
        return "<Anchor(href='" + self.href + "')>"
