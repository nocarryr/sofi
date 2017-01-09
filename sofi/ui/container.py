from .element import Element
from .row import Row

class Container(Element):
    """Implements a container tag of form <div class=\"container\"> or
    <div class=\"container-fluid\">"""

    def __init__(self, fluid=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.fluid = fluid

    def newrow(self, element):
        r = Row()
        r.addelement(element)
        self.addelement(r)

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        classes.add('container')
        if self.fluid:
            classes.add('container-fluid')
        return classes

    def __repr__(self):
        return "<Container(fluid=" + str(self.fluid) + ")>"
