import urllib

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

def union(p,b):
    for i in b:
        if i not in a:
            a.append(i)

def crawlWeb(seed, maxPages):
  toCrawl = [seed]
  crawled = []
  index = []
  while toCrawl and len(crawled) <= maxPages:
    page = toCrawl.pop()
    if page not in crawled:
      pageContent = getPage(page)
      addPageToIndex(index, page, pageContent)
      links = getAllLinks(pageContent)
      union(toCrawl, links)
      crawled.append(page)
  return index

# The following function limits the depth of the crawl
#
# def crawlWeb(seed, max_depth):    
#     toCrawl = [seed]
#     crawled = []
#     nextDepth = []
#     depth = 0
#     while toCrawl and depth <= maxDepth:
#         page = toCrawl.pop()
#         if page not in crawled:
#             links = getAllLinks(getPage(page))
#             union(nextDepth, links)
#             crawled.append(page)
#         if not toCrawl:
#             toCrawl, nextDepth = nextDepth, []
#             depth = depth + 1
#     return crawled

def addToIndex(index, keyword, url):
  for entry in index:
    if entry[0] == keyword:
      entry[1].append(url)
      return
  index.append([keyword, [url]])
  return

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

def addPageToIndex(index, url, content):
    keywords = content.split()
    for keyword in keywords:
        addToIndex(index, keyword, url)

def getPage(url):
  try:
    return urllib.urlopen(url).read()
  except:
    return ""
