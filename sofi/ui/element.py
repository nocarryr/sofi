class Element(object):
    """Base HTML tag element"""

    html_tag = 'div'
    tag_closes_element = True
    has_content = True
    def __init__(self, cl=None, ident=None, style=None, attrs=None):
        """Create a base element where cl is a space separated class attribute,
           ident is the element id and style is a CSS style string"""

        self.cl = cl
        self.ident = ident
        self.style = style
        self.attrs = attrs

        self._children = list()

    @property
    def closing_tag(self):
        tag = getattr(self, '_closing_tag', None)
        if tag is None:
            if self.tag_closes_element:
                tag = self._closing_tag = '</{}>'.format(self.html_tag)
            else:
                tag = self._closing_tag = ' />'
        return tag

    @closing_tag.setter
    def closing_tag(self, tag):
        self._closing_tag = tag

    @property
    def html_attrs(self):
        attrs = self._get_all_attrs()
        if not len(attrs):
            return ' '
        return self._attrs_to_string(attrs)

    @property
    def content(self):
        return self._get_content()

    def _get_content(self):
        c = []
        if getattr(self, 'text', None):
            c.append(self.text)
        for child in self._children:
            c.append(str(child))
        return ''.join(c)

    def _get_all_attrs(self):
        attrs = {}
        classes = self._get_all_classes()
        if classes:
            attrs['class'] = ' '.join(classes)
        if self.ident:
            attrs['id'] = self.ident
        if self.attrs is not None:
            attrs.update(self.attrs)
        if self.style is not None:
            attrs['style'] = self.style
        return attrs

    def _get_all_classes(self):
        classes = {}
        if self.cl:
            if isinstance(self.cl, str):
                classes |= set(self.cl.split(' '))
            else:
                classes |= set(self.cl)
        return classes

    def _attrs_to_string(self, attributes=None):
        """
        A shortcut for generating all the tag attributes (id, class, etc)
        given a list of (attr_name_in_self, attr_name_in_html) pairs.

        >>> e = Element(cl='container', ident='foo')

        >>> attributes = [
        ...         ('cl', 'class'),
        ...         ('ident', 'id')]

        >>> e._attrs_to_string(attributes)
        'class="container" id="foo"'

        If no arguments are given, `attributes` defaults to
        `[('cl','class'), ('ident', 'id')]`.

        If `attributes` contains a pair of ("some_name", None), `some_name`
        will be taken as an attribute with no value and will be appended
        directly to the output string.
        """

        if attributes is None:
            attributes=[('cl','class'), ('ident', 'id')]

        output = []

        for name, as_html in attributes:
            if as_html is None:
                # This is an attribute with no value
                # e.g. <input type="text" name="name" value="" disabled>
                output.append(name)
            else:
                # Grab the value of the `name` attribute from `self`
                value = getattr(self, name, None)
                if value:
                    output.append('{}="{}"'.format(as_html, value))

        return ' '.join(output)

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.has_content:
            html_template = '<{self.tag}{self.html_attrs}>{self.content}{self.closing_tag}'
        else:
            html_template = '<{self.tag}{self.html_attrs}{self.closing_tag}'
        return html_template.format(self=self)

    def addelement(self, item):
        """Add a child element to this tag"""

        if item is not None:
            self._children.append(item)
