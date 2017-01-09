from .element import Element
from .button import Button

class ButtonGroup(Element):
    """Implements a button group <div class=\"btn-group\">"""

    def __init__(self, size=None, vertical=False, justified=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.size = size
        self.vertical = vertical
        self.justified = justified

    def _get_content(self):
        if not self.justified:
            return super()._get_content()
        c = []
        for child in self._children:
            if isinstance(child, Button):
                bgrp = ButtonGroup()
                bgrp.addelement(child)
                c.append(str(bgrp))
            else:
                c.append(str(child))
        return c

    def _get_all_attrs(self):
        attrs = super()._get_all_attrs()
        attrs['role'] = 'group'
        return attrs

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        classes.add('btn-group')
        if self.justified:
            classes.add("btn-group-justified")
        if self.vertical:
            classes.add("btn-group-vertical")
        if self.size:
            if self.size == "large" or self.size == "lg":
                classes.add("btn-group-lg")
            elif self.size == "small" or self.size == "sm":
                classes.add("btn-group-sm")
            elif self.size == "xsmall" or self.size == "xs":
                classes.add("btn-group-xs")
        return classes

    def __repr__(self):
        return "<ButtonGroup(size=" + self.size + ")>"
