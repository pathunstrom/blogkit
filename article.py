from jinja2 import Markup
from markdown import Markdown
from datetime import date

parser = Markdown(extensions=['markdown.extensions.meta'])


class Article(object):
    """

    """

    def __init__(self, post_file):
        self.markup = Markup(parser.reset().convertFile(post_file))
        self.meta = parser.Meta
        self.title = self.meta["title"][0]
        date_values = self.meta["date"][0].split("/")
        self.date = date(*date_values)
        self.tags = self.meta["tags"]
        self.authors = self.meta["authors"].join(", ")
        self.file_name = post_file


    def __cmp__(self, other):
        if self.date < other.date:
            return -1
        elif self.date > other.date:
            return 1
        else:
            return 0

    def __repr__(self):
        return "Article: {title}, {date}".format(title=self.title, date=self.date)