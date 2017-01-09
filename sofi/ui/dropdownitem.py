from .element import Element
from .anchor import Anchor

class DropdownItem(Element):
    """Implements an item from a Dropdown list"""

    html_tag = 'li'
    def __init__(self, text=None, disabled=False, header=False, divider=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.disabled = disabled
        self.header = header
        self.divider = divider

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        if self.header:
            classes.add('dropdown-header')
        elif self.divider:
            classes.add("divider")
        elif self.disabled:
            classes.add("disabled")
        return classes

    def __repr__(self):
        return '<DropdownItem(text="' + self.text + '",disabled=' + self.disabled + ',header=' + self.header + ',divider=' + self.divider + ')>'
