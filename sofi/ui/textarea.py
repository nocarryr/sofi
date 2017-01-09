from .element import Element

class Textarea(Element):
    """Implements <textarea> tag"""

    html_tag = 'textarea'
    def __init__(self, text=None, rows=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text:
            self._children.append(text)

        self.rows = rows

    def _get_all_attrs(self):
        attrs = super()._get_all_attrs()
        if self.rows:
            attrs['rows'] = self.rows
        return attrs

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        classes.add('form-control')
        return classes

    def __repr__(self):
        return "<Textarea>"
