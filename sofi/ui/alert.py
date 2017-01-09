from .element import Element
from .button import Button
from .span import Span

class Alert(Element):
    """Implements the <div class="alert"> tag"""

    SEVERITIES = { 'danger':  'alert-danger',
                   'success': 'alert-success',
                   'info':    'alert-info',
                   'warning': 'alert-warning'
                 }

    def __init__(self, text=None, severity=None, closebtn=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.severity = severity
        self.closebtn = closebtn
        if self.closebtn:
            btn = Button(cl="close", attrs={'data-dismiss':'alert', 'aria-label':'Close'})
            btn.addelement(Span(text='&times;', attrs={'aria-hidden':'true'}))
            self.addelement.append(btn)

    def _get_all_attrs(self):
        attrs = super()._get_all_attrs()
        attrs['role'] = 'alert'
        return attrs

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        if self.severity:
            classes.add(Alert.SEVERITIES[self.severity])
        if self.closebtn:
            classes |= {"alert-dismissible", "fade in"}
        return classes

    def __repr__(self):
        return "<Alert(text='" + self.text + "')>"
