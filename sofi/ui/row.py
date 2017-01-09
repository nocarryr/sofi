from .element import Element

class Row(Element):
    """Implements row layout with format <div class=\"row\">"""

    def __init__(self, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        classes.add('row')
        return classes

    def __repr__(self):
        return "<Row>"
