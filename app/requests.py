import urllib.request,json
from .models import User
import requests

#Getting the base url
base_url = None

def configure_request(app):
    global base_url #,api_key
    base_url = app.config['QUOTES_API_BASE_URL']
    #api_key = app.config['BLOG_API_KEY']

def get_quote():
    '''
    function that gets the json response to the url request
    '''
    pos = requests.get(base_url)
    posts = pos.json()
    return posts

def process_results(quote_list):
    '''
    function that processes results of the quote and returns a list of quotes
    '''
    quote_results = []
    for quote_item in quote_list:
        id = quote_item.get('id')
        quote = quote_item.get('quote')
        author = quote_item.get('author')

        quote_object = Quote(id,quote,author)
        quote_results.append(quote_object)

    return quote_results