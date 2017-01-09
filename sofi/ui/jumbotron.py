from .element import Element

class Jumbotron(Element):
    """Implements the Bootstrap Jumbotron <div class="jumbotron">"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text:
            self._children.append(text)

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        classes.add('jumbotron')
        return classes

    def __repr__(self):
        return "<Jumbotron>"
