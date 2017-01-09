from .div import Div

class FormGroup(Div):
    """Implements <div> tag with class form-group"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(text=text, cl=cl, ident=ident, style=style, attrs=attrs)

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        classes.add('form-group')
        return classes

    def __repr__(self):
        return "<FormGroup>"
