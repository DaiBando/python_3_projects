import webbrowser
import time

news_urls = ["https://www.yahoo.com"]
tech_news_urls = ["https://www.engadget.com", "https://techcrunch.com", "https://www.theverge.com"]
sec_news_urls = ["https://thehackernews.com", "https://threatpost.com", "https://cyware.com/cyber-security-news-articles"]

def open_tabs(url_group):
    for element in url_group:
        webbrowser.open_new_tab(element)

def main():
    webbrowser.open("www.google.com", new=0, autoraise=False)
    time.sleep(1)
    open_tabs(news_urls)
    open_tabs(tech_news_urls)
    open_tabs(sec_news_urls)

main()




































