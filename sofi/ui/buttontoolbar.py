from .element import Element

class ButtonToolbar(Element):
    """Implements a button toolbar <div class=\"btn-toolbar\">"""

    html_tag = 'div'
    def __init__(self, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

    def _get_all_attrs(self):
        attrs = super()._get_all_attrs()
        attrs['role'] = 'toolbar'
        return attrs

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        classes.add('btn-toolbar')
        return classes

    def __repr__(self):
        return "<ButtonToolbar()>"
