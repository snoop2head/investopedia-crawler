import os
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import string

alphabet_list = string.ascii_lowercase

for alphabet in alphabet_list:
    index_no_int = 4769351 + alphabet_list.index(alphabet)
    index_no_str = str(index_no_int)
    terms_url = (
        f"https://www.investopedia.com/terms-beginning-with-{alphabet}-{index_no_str}"
    )
    print(terms_url)
