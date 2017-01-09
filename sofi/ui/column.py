from .element import Element

class Column(Element):
    """Implements the column layout <div class=\"col-\"> where size, count and offset
    attributes are used to create the class name, i.e.: col-md-4 or col-offset-md-4"""

    def __init__(self, size='md', count=4, offset=0, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.size = size
        self.count = count
        self.offset = offset

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        fmt_str = 'col-{self.size}-{self.count}'
        classes.add(fmt_str.format(self=self))
        if self.offset > 0:
            fmt_str = '-'.join([fmt_str, 'offset-{self.offset}'])
            classes.add(fmt_str.format(self=self))
        return classes

    def __repr__(self):
        return "<Column(size='" + self.size + "',count='" + str(self.count) + "',offset=" + str(self.offset) + ")>"
