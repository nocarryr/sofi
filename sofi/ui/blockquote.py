from .element import Element

class Blockquote(Element):
    """Implements the <blockquote> tag"""

    html_tag = 'blockquote'
    def __init__(self, text=None, reverse=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.reverse = reverse

        if text:
            self._children.append(text)

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        if self.reverse:
            classes.add('blockquote-reverse')
        return classes

    def __repr__(self):
        return "<Blockquote(reverse=" + str(self.reverse) + ")>"
