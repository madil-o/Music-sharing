
import time
from duckduckgo_search import DDGS


def link_from_platform(platform, text):
  results = DDGS().text(
    keywords=f"{platform} {text} song",
    backend="api",
    max_results=5
  )
  return results[0]["href"]

def get_links(song):
  links = []
  for platform in ["spotify","youtube", "deezer", "apple music"]:
    links.append(link_from_platform(platform, song))
    time.sleep(1)
  
  return links
