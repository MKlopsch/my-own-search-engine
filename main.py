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
      links.append[url]
      page = page[endPos:]
  return links

def crawlWeb(seed, max_pages):
  toCrawl = [seed]
  crawled = []
  while toCrawl:
    page = toCrawl.pop()
    if page not in crawled:
      links = getAllLinks(getPage(page))
      toCrawl.extend(links)
      crawled.append(page)
    if len(crawled) == max_pages:
      break
  return crawled
