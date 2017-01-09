from .element import Element

class Form(Element):
    """Implements the <form> tag"""

    html_tag = 'form'
    def __init__(self, inline=False, horizontal=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.inline = inline
        self.horizontal = horizontal

    def _get_all_classes(self):
        classes = super()._get_all_classes()
        if self.inline:
            classes.add('form-inline')
        if self.horizontal:
            classes.add('form-horizontal')
        return classes

    def __repr__(self):
        return "<Form(inline=" + self.inline + ",horizontal=" + self.horizontal + ")>"
