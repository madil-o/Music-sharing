
import time
from duckduckgo_search import DDGS


def link_from_platform(platform, text):
  results = DDGS().text(
    keywords=f"{platform} {text} song",
    backend="api",
    max_results=1
  )
  return results[0]["href"]


def get_cover(song):
  results = DDGS().images(
    keywords=f"{song} album cover",
    max_results=1
  )
  return results[0]["image"]


def get_links(song):
  links = []
  for platform in ["spotify","youtube", "deezer", "apple music"]:
    links.append(link_from_platform(platform, song))
    time.sleep(0.5)
  
  return links


def dico_of_link_string(link_str):
  lst = link_str.split(";")
  return {"spotify" : lst[0], "youtube" : lst[1], "deezer" : lst[2], "apple music" : lst[3]}
