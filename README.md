# UT News RSS

A Django application to parse and show the RSS of `University of Tehran (UT)` news.
This app parses the link bellow to extract news.

```url
https://news.ut.ac.ir/fa/news/category/79/%D8%A7%D8%B7%D9%84%D8%A7%D8%B9%DB%8C%D9%87-%D9%87%D8%A7-%D9%88-%D9%81%D8%B1%D8%A7%D8%AE%D9%88%D8%A7%D9%86-%D9%87%D8%A7
```

## Built With

- Django
- Django REST Framework
- Beautiful Soup 4

## Getting Started

This is an example of how you may give instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.

### Installation

1. Clone the repo
   ```bash
   git clone https://github.com/XAli-SHX/ut-news-rss.git
   ```
2. Install requirements
   ```bash
   cd core
   pip install -r requirements.txt
   ```
3. Run server
   ```bash
   python3 manage.py runserver
   ```

Now by entering the URL bellow you can access the news:

```url
http://127.0.0.1:8000/news/
```

## Usage

This project is a base to build an app to show news and send notification when a new news be published.

## Roadmap

- [x] Basic parsing of HTML page
- [ ] Show next page news
- [ ] Add filter to news
- [ ] Implement all tags
  - [x] [اطلاعیه‌ها و فراخوان‌‌ها](https://news.ut.ac.ir/fa/news/category/79/%D8%A7%D8%B7%D9%84%D8%A7%D8%B9%DB%8C%D9%87-%D9%87%D8%A7-%D9%88-%D9%81%D8%B1%D8%A7%D8%AE%D9%88%D8%A7%D9%86-%D9%87%D8%A7)
    - [ ] [اطلاعیه عمومی](https://news.ut.ac.ir/fa/news/category/472/%D8%A7%D8%B7%D9%84%D8%A7%D8%B9%DB%8C%D9%87-%D8%B9%D9%85%D9%88%D9%85%DB%8C)
    - [ ] [اطلاعیه‌های آموزشی](https://news.ut.ac.ir/fa/news/category/441/%D8%A7%D8%B7%D9%84%D8%A7%D8%B9%DB%8C%D9%87-%D9%87%D8%A7%DB%8C-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%DB%8C)
    - [ ] [اطلاعیه‌های دانشجویی](https://news.ut.ac.ir/fa/news/category/440/%D8%A7%D8%B7%D9%84%D8%A7%D8%B9%DB%8C%D9%87-%D9%87%D8%A7%DB%8C-%D8%AF%D8%A7%D9%86%D8%B4%D8%AC%D9%88%DB%8C%DB%8C)
    - [ ] [اطلاعیه‌های برگزاری رویدادها](https://news.ut.ac.ir/fa/news/category/439/%D8%A7%D8%B7%D9%84%D8%A7%D8%B9%DB%8C%D9%87-%D9%87%D8%A7%DB%8C-%D8%A8%D8%B1%DA%AF%D8%B2%D8%A7%D8%B1%DB%8C-%D8%B1%D9%88%DB%8C%D8%AF%D8%A7%D8%AF%D9%87%D8%A7)
    - [ ] [اطلاعیه‌های ستادی و سازمانی](https://news.ut.ac.ir/fa/news/category/438/%D8%A7%D8%B7%D9%84%D8%A7%D8%B9%DB%8C%D9%87-%D9%87%D8%A7%DB%8C-%D8%B3%D8%AA%D8%A7%D8%AF%DB%8C-%D9%88-%D8%B3%D8%A7%D8%B2%D9%85%D8%A7%D9%86%DB%8C)
  - [ ] [اخبار](https://news.ut.ac.ir/fa/news/category/26/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1)
    - [ ] [اخبار فناوری‌های دیجیتال](https://news.ut.ac.ir/fa/news/category/677/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D9%81%D9%86%D8%A7%D9%88%D8%B1%DB%8C-%D9%87%D8%A7%DB%8C-%D8%AF%DB%8C%D8%AC%DB%8C%D8%AA%D8%A7%D9%84)
    - [ ] [اخبار بین‌الملل](https://news.ut.ac.ir/fa/news/category/496/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%A8%DB%8C%D9%86-%D8%A7%D9%84%D9%85%D9%84%D9%84)
    - [ ] [اخبار توسعه‌ای](https://news.ut.ac.ir/fa/news/category/413/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%AA%D9%88%D8%B3%D8%B9%D9%87-%D8%A7%DB%8C)
    - [ ] [اخبار رویدادها](https://news.ut.ac.ir/fa/news/category/412/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%B1%D9%88%DB%8C%D8%AF%D8%A7%D8%AF%D9%87%D8%A7)
    - [ ] [اخبار ستادی](https://news.ut.ac.ir/fa/news/category/411/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%B3%D8%AA%D8%A7%D8%AF%DB%8C)
    - [ ] [اخبار ورزشی](https://news.ut.ac.ir/fa/news/category/410/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D9%88%D8%B1%D8%B2%D8%B4%DB%8C)
    - [ ] [اخبار هنری](https://news.ut.ac.ir/fa/news/category/409/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D9%87%D9%86%D8%B1%DB%8C)
    - [ ] [اخبار سلامت و بهداشت](https://news.ut.ac.ir/fa/news/category/408/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%B3%D9%84%D8%A7%D9%85%D8%AA-%D9%88-%D8%A8%D9%87%D8%AF%D8%A7%D8%B4%D8%AA)
    - [ ] [اخبار علمی-فناوری](https://news.ut.ac.ir/fa/news/category/407/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%B9%D9%84%D9%85%DB%8C-%D9%81%D9%86%D8%A7%D9%88%D8%B1%DB%8C)
    - [ ] [اخبار حوادث / زلزله](https://news.ut.ac.ir/fa/news/category/406/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%AD%D9%88%D8%A7%D8%AF%D8%AB-%D8%B2%D9%84%D8%B2%D9%84%D9%87)
    - [ ] [اخبار دانشجویی](https://news.ut.ac.ir/fa/news/category/405/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%AF%D8%A7%D9%86%D8%B4%D8%AC%D9%88%DB%8C%DB%8C)
    - [ ] [اخبار پژوهشی](https://news.ut.ac.ir/fa/news/category/404/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D9%BE%DA%98%D9%88%D9%87%D8%B4%DB%8C)
    - [ ] [اخبار فرهنگی-دینی](https://news.ut.ac.ir/fa/news/category/403/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D9%81%D8%B1%D9%87%D9%86%DA%AF%DB%8C-%D8%AF%DB%8C%D9%86%DB%8C)
    - [ ] [اخبار آموزشی](https://news.ut.ac.ir/fa/news/category/402/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%DB%8C)
    - [ ] [تجارب زیسته](https://news.ut.ac.ir/fa/news/category/364/%D8%AA%D8%AC%D8%A7%D8%B1%D8%A8-%D8%B2%DB%8C%D8%B3%D8%AA%D9%87)
    - [ ] [اخبار دانشگاه سبز](https://news.ut.ac.ir/fa/news/category/158/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B3%D8%A8%D8%B2)

## Contribution

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag `feature`. Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` file for more information.

## Contact

Ali Shayanpoor - shayanpoorali66@gmail.com

Project Link: https://github.com/XAli-SHX/ut-news-rss
