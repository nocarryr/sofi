from .element import Element

class Button(Element):
    """Implements the <button> tag"""

    SEVERITIES = { 'danger':  'btn-danger',
                   'success': 'btn-success',
                   'info':    'btn-info',
                   'warning': 'btn-warning',
                   'primary': 'btn-primary',
                   'default': 'btn-default'
                 }

    html_tag = 'button'
    def __init__(self, text=None, severity=None, size=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.severity = severity
        self.size = size

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        if self.severity:
            classes.add(Button.SEVERITIES[self.severity])
        else:
            classes.add(Button.SEVERITIES['default'])
        if self.size:
            if self.size == "large" or self.size == "lg":
                classes.add("btn-lg")
            elif self.size == "small" or self.size == "sm":
                classes.add("btn-sm")
            elif self.size == "xsmall" or self.size == "xs":
                classes.add("btn-xs")
        return classes

    def __repr__(self):
        return "<Button(text='" + self.text + "')>"
