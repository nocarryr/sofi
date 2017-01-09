from .element import Element

class FontAwesomeIcon(Element):
    """Implements a Font Awesome Icons"""

    html_tag = 'i'
    def __init__(self, name=None, size=None, fixed=False, animation=None,
                 rotate=None, flip=None, border=False, pull=None,
                 cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.name = name
        self.size = size
        self.fixed = fixed
        self.animation = animation
        self.rotate = rotate
        self.flip = flip
        self.border = border
        self.pull = pull

    def _get_all_classes(self):
        classes = super()._get_all_classes()

        classes.add('fa')
        if self.name:
            classes.add("fa-{}".format(self.name))

        if self.animation:
            classes.add("fa-".format(self.animation))

        if self.rotate:
            classes.add("fa-rotate-{}".format(self.rotate))

        if self.border:
            classes.add("fa-border")

        if self.pull:
            classes.add("fa-pull-{}".format(self.pull))

        if self.flip:
            classes.add("fa-flip-{}".format(self.flip))

        if self.size:
            classes.add("fa-{}".format(self.size))

        if self.fixed:
            classes.add("fa-fw")

        return classes

    def __repr__(self):
        return "<Icon(name='" + self.name + "')>"
