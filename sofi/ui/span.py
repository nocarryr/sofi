from .element import Element

class Span(Element):
    """Implements <span> tag"""

    html_tag = 'span'
    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<Span>"


class CaretSpan(Span):
    """Implements a span that contains a caret icon, useful in dropdowns and other similar situations"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        classes.add('caret')
        return classes
