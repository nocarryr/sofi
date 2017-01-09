from .element import Element
from .span import Span

class Label(Element):
    """Implements a Bootstrap Label <span class="label"> tag"""

    SEVERITIES = { 'danger':  'label-danger',
                   'success': 'label-success',
                   'info':    'label-info',
                   'warning': 'label-warning',
                   'primary': 'label-primary',
                   'default': 'label-default'
                 }

    html_tag = 'span'
    def __init__(self, text=None, severity=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.severity = severity

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        classes.add('label')
        if self.severity:
            classes.add(Label.SEVERITIES[self.severity])
        else:
            classes.add(Label.SEVERITIES['default'])
        return classes

    def __repr__(self):
        return "<Label(text='" + self.text + "')>"
