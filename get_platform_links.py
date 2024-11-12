
from duckduckgo_search import DDGS


def link_from_platform(platform, text):
  results = DDGS().text(
    keywords=f"{platform} {text} song",
    backend="api",
    max_results=5
  )
  return results[0]["href"]

song = input("song name :")

for i in ["spotify", "youtube", "deezer", "apple music"]:
  print(link_from_platform(i, song))
