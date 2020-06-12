import os
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import string


def collect_three_lines(vocab_url):
    # get page content response from the web using requests and beautifulsoup
    res = requests.get(vocab_url)
    soup = BeautifulSoup(res.content, "lxml")
    # print(soup)
    three_summary_div = soup.find(
        "div", {"class": "comp mntl-sc-block-callout-body mntl-text-block"}
    )
    # print(three_summary_div)
    three_line_summary = three_summary_div.get_text()
    return three_line_summary


def listup_terms(scrape_url):
    VOCAB_BASE_URL = "https://www.investopedia.com/terms/"
    empty_list = []
    alphabet = scrape_url.split("-")[-2]
    print(alphabet)
    # get page content response from the web using requests and beautifulsoup
    res = requests.get(scrape_url)
    soup = BeautifulSoup(res.content, "lxml")
    # print(soup)
    for item in soup.find_all("a", href=True):
        href_item = item["href"]
        # print(href_item)
        vocab_url = VOCAB_BASE_URL + alphabet
        if vocab_url in href_item:
            # print(href_item)
            empty_list.append(href_item)
            vocab_url_list = empty_list
    # print(vocab_url_list)
    return vocab_url_list


def listup_all_terms():
    empty_list = []
    INDEX_NO = 4769351
    alphabet_list = string.ascii_lowercase
    for alphabet in alphabet_list:
        index_no_int = INDEX_NO + alphabet_list.index(alphabet)
        index_no_str = str(index_no_int)
        terms_url = f"https://www.investopedia.com/terms-beginning-with-{alphabet}-{index_no_str}"
        print(terms_url)
        empty_list.append(terms_url)
        alphabet_url_list = empty_list
    return alphabet_url_list


# listup_terms("https://www.investopedia.com/terms-beginning-with-b-4769352")
collect_three_lines("https://www.investopedia.com/terms/b/buyersmarket.asp")
