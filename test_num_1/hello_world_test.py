import urllib.request
import re

search_phrase = r"Hello world"
page_scraper = urllib.request.urlopen("http://matiushyn.dev.run//").read()
search_results = re.findall(search_phrase, str(page_scraper))
print(search_results)
if search_results:
    print("Test passed")
else:
    print("Test no passed")