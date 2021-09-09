# About BeautifuSoup: tries to make sense of the nonsensical; it helps fromat and organize the messy web by fixing bad HTML and presenting us with easily traversable Python objects representing XML structures.

# urllib: us a package that collects several modules for working with URLS:
  # urllib.request: for opening and reading URLs
  # urllib.error: containing the exceptions raised by urllib.request
  # urllib.parse: for parsing URLs - parsing functions focus on splitting a URL string into its components, or on combining URL components into a URL string.
  # urllib.robotparser: for parsing robots.txt files
 
 # HTMLError_URLError
 
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTMLError
from urllib.error import URLError

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
    bs = BeautifulSoup(html.read(), 'lxml')
    title = bs.body.h1
except HTTPError as e:
    print(e)
except URLError as e:
    print('the server is not found')
except AttributeError as e:
    print('tag was not found')
else:
    print('web is ok')
    if title == None:
        print('Title could not be found')
    else:
        print(title)


