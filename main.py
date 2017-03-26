def getNextLink(page):
  startLink = page.find("<a href=")
  if startLink == -1:
    return None, 0
  startQuote = page.find('"', startLink)
  endQuote = page.find('"', startQuote + 1)
  url = page[startQuote + 1:endQuote]
  return url, endQuote

def getAllLinks(page):
  url = True
  links = []
  while url:
    url, endPos = getNextLink(page)
    if url:
      link.append[url]
      page = page[endPos:]
