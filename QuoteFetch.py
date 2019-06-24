"""
Author: Aidan Jude
Date: 06/23/2019
Description:
    -This file contains the function which carries out the BrainyQuote search and retrieve
    -We utilize the BeautifulSoup library for the HTML parsing
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import html5lib
import random

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,}

#we search google for the given author and scrape a random quote
def get_random_quote(author):
    author = author.replace(' ', '_')
    base_url = 'https://www.brainyquote.com/authors/'
    query = base_url + author
    req = Request(query)
    req.add_header('User-Agent', user_agent)
    response = urlopen(req).read()
    content = response.decode("utf8")
    soup = BeautifulSoup(content, 'html5lib')
    html = list(soup.children)[1]
    body = list(html.children)[2]
    #random number will allow for a random quote selection from the author which was passed to the function
    x = random.choice(range(1, 41, 4))
    try:
        #get the quote object container
        quote_body = list(list(list(list(list(list(list(list(soup.children)[1])[2])[13])[1])[1])[1])[3])[x]
        #if we make a bad grab (most likely caused by an ad on the webpage, we fetch the first quote instead
        if(quote_body.get_text().strip() == ''):
            quote_body = list(list(list(list(list(list(list(list(soup.children)[1])[2])[13])[1])[1])[1])[3])[1]
    #if we go out of range on our call for a quote (not that many quotes from the author), we resort to the first one
    except IndexError as i:
        quote_body = list(list(list(list(list(list(list(list(soup.children)[1])[2])[13])[1])[1])[1])[3])[1]
    #utilize the BeautifulSoup library to clean up the HTML and only keep the text on the page (not object headers)
    text = quote_body.get_text().strip()
    final_quote = ''
    for char in text:
        if(char == '\n' or char == ''):
            break
        else:
            final_quote += char
  
    return(final_quote)
