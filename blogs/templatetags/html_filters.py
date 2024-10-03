from django import template
from html.parser import HTMLParser
from django.utils.safestring import mark_safe

register = template.Library()

class HTMLTruncator(HTMLParser):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit
        self.words = []
        self.result = []
        self.in_tag = False

    def handle_starttag(self, tag, attrs):
        if len(self.words) < self.limit:
            self.result.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if len(self.words) < self.limit:
            self.result.append(f"</{tag}>")

    def handle_data(self, data):
        if len(self.words) < self.limit:
            new_words = data.split()
            remaining = self.limit - len(self.words)
            self.words.extend(new_words[:remaining])
            self.result.append(' '.join(new_words[:remaining]))
            if len(self.words) == self.limit:
                self.result.append('...')

    def get_truncated_html(self):
        return ''.join(self.result)

@register.filter
def truncate_html_words_builtin(value, num):
    """
    Truncate words safely while preserving HTML using Python's built-in HTMLParser.
    """
    parser = HTMLTruncator(num)
    parser.feed(value)
    return mark_safe(parser.get_truncated_html())

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})
