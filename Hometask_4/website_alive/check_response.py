"""Check result of request status code"""
from website_alive.make_request import my_request


def check():
    """Check available of site"""
    my_url = input("Input url: ")
    return my_request(my_url).status_code == int(200)
