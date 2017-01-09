from .element import Element

class Well(Element):
    """Implements the Bootstrap Well <div class="well">"""

    def __init__(self, text=None, size=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.size = size
        self.text = text

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        classes.add('well')
        if self.size:
            if self.size == "large" or self.size == "lg":
                classes.add("well-lg")
            elif self.size == "small" or self.size == "sm":
                classes.add("well-sm")
        return classes

    def __repr__(self):
        return "<Well(text='" + self.text + "')>"
