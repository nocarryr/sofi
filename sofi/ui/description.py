from .element import Element

class Description(Element):
    """Implements <dl> tag"""

    html_tag = 'dl'
    def __init__(self, text=None, horizontal=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.horizontal = horizontal

        if text:
            self._children.append(text)

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        if self.horizontal:
            classes.add('dl-horizontal')
        return classes

    def __repr__(self):
        return "<Description(horizontal=" + self.horizontal + ")>"
