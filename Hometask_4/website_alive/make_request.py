"""Make request to site"""
import requests


def my_request(url):
    """The function that uses another function that makes a request to url:)"""
    return requests.get(url)
