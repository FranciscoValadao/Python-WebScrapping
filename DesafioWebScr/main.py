from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from pandas import DataFrame, read_excel
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def generate_spreadsheet(data_dict):
    """
    Takes a dictionary as an argument, frames the data as a column/row style
    then exports it in excel, registering the date an hour of the search.

    Args:
        data_dict (dict): carry the current Url that is being acessed alongside its keyword search results
    """
    formatted_data = dict()
    for key, value in data_dict.items():
        if isinstance(value, list):
            formatted_data[key] = ', '.join(value)
        else:
            formatted_data[key] = value
    print("[DEBUG] Formatted Data: {}".format(formatted_data))
    data_frame = DataFrame.from_dict(formatted_data, orient='index', dtype=None, columns=['Keywords found'])
    print("[DEBUG] Framed Data: {}".format(data_frame))
    data_frame.to_excel(r'./DesafioWebScr/spreadsheets/DataScrOutput_{}.xlsx'.format(datetime.now().strftime("%m-%d-%Y_%H-%M-%S")))


def find_words_in_text(text_content, keyword_list):
    """Find the keywords into the text thats been brought from the web page requisited

    Args:
        text_content (str): contains the text existent into the web page
        keyword_list (list): contains all the words that will be searched in the text

    Returns:
        found_keyword (list): contains only the words that were found at the text.
    """

    found_keyword = []
    for keyword in keyword_list:
        if(text_content.count(keyword.upper())):
            print("[DEBUG] Keyword found: {} -> {} time(s)".format(keyword, text_content.count(keyword.upper())))
            found_keyword.append(keyword)
    print("[DEBUG] All Keywords found: {}".format(found_keyword))
    return found_keyword


def read_url_page(url_page, headless=True):
    """Opens the webpage in a automated navigator, extracts and deliver only text so it can be scrapped

    Args:
        url_page (string): contains the Url that is going to be acessed
        headless (bool, optional): Selects wheter the automated browser will work only at the bkgnd. Defaults to True.

    Returns:
        text_content (str): returns a text field that contains every written information at the site.
    """
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    webdriver_path = r'ChromeDriver'
    driver = webdriver.Chrome(webdriver_path +r'\chromedriver.exe', options=chrome_options)
    driver.get(url_page)
    sleep(5)
    raw_page_content = driver.page_source
    page_content = BeautifulSoup(raw_page_content, 'html.parser')
    text_content = page_content.text.upper()
    return text_content


if __name__=='__main__':
    input_spreadsheet = read_excel(r'DesafioWebScr\spreadsheets\parametros.xlsx')
    input_keywords = input_spreadsheet['palavras_chave'].tolist()
    input_urls = input_spreadsheet['urls'].tolist()
    input_urls = [url for url in input_urls if isinstance(url, str)]
    print('[DEBUG] Input_URLs: {}'.format(input_urls))
    keywords_found = dict()
    for url in input_urls:
        print('[DEBUG] Searching for keywords in URL page: {}'.format(url))
        text_content = read_url_page(url, headless=True)
        keywords_found[url] = find_words_in_text(text_content, input_keywords)
    print('[DEBUG] URLs and Keywords Found: {}'.format(keywords_found))
    generate_spreadsheet(keywords_found)
