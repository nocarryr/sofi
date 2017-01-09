from .span import Span

class Badge(Span):
    """Implement Boostrap Badge <span class="badge">"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        classes.add('badge')
        return classes

    def __repr__(self):
        return "<Badge(text='" + self.text + "')>"
