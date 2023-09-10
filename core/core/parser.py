from core.ut_news import UtNews


def parse_news():
    import requests
    from bs4 import BeautifulSoup

    url = 'https://news.ut.ac.ir/fa/news/category/79/%D8%A7%D8%B7%D9%84%D8%A7%D8%B9%DB%8C%D9%87-%D9%87%D8%A7-%D9%88-%D9%81%D8%B1%D8%A7%D8%AE%D9%88%D8%A7%D9%86-%D9%87%D8%A7'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    main_content = soup.find('div', class_='news-index blog-view')
    news_list = main_content.find('div', class_='list-view').find('div', class_='row').find_all('div',
                                                                                                class_='col-md-4')
    for news_box in news_list:
        news = news_box.find('article')
        image_wrapper = news.find('div', class_='image-wrapper')
        item_content = news.find('div', class_='item-content')
        img = image_wrapper.find('figure').a.img

        img_src = img['src']
        img_alt = img['alt']
        short_title = img_alt
        title = item_content.h3.a.text
        news_detail_url = item_content.h3.a['href']
        is_new = item_content.find('small', class_='new-label') is not None
        brief = None
        if item_content.p is not None:
            brief = item_content.p.text.strip()

        meta = item_content.find('div', class_='item-meta-data')
        category = None
        if meta.a is not None:
            category = meta.a.text.strip()
            meta.a.extract()
        date = meta.text.strip()

        ut_news = UtNews(img_src, img_alt, short_title, title, news_detail_url, is_new, brief, category, date)
        return ut_news
