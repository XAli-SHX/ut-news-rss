class UtNews:
    def __init__(self, img_src, img_alt, short_title, title, news_detail_url, is_new, brief, category, date):
        self.img_src = img_src
        self.img_alt = img_alt
        self.short_title = short_title
        self.title = title
        self.news_detail_url = news_detail_url
        self.is_new = is_new
        self.brief = brief
        self.category = category
        self.date = date

    def to_dict(self):
        return {
            'img_src': self.img_src,
            'img_alt': self.img_alt,
            'short_title': self.short_title,
            'title': self.title,
            'news_detail_url': self.news_detail_url,
            'is_new': self.is_new,
            'brief': self.brief,
            'category': self.category,
            'date': self.date
        }
