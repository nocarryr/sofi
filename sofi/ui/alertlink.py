from .element import Element
from .anchor import Anchor

class AlertLink(Anchor):
    """Implements the AlertLink <a class="alert-link"> tag"""

    def __init__(self, text=None, href="#", cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.href = href

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        classes.add('alert-link')
        return classes

    def __repr__(self):
        return "<AlertLink(href='" + self.href + "')>"
