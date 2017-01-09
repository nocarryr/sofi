from .element import Element

class UnorderedList(Element):
    """Implements <ul> tag"""

    html_tag = 'ul'
    def __init__(self, text=None, unstyled=False, inline=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.unstyled = unstyled
        self.inline = inline

        if text:
            self._children.append(text)

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        if self.unstyled:
            classes.add('list-unstyled')
        elif self.inline:
            classes.add('list-inline')
        return classes

    def __repr__(self):
        return "<UnorderedList(unstyled=" + str(self.unstyled) + ",inline=" + str(self.inline) + ")>"
