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
      links.append(url)
      page = page[endPos:]
  return links

def union(a, b):
    for i in b:
        if i not in a:
            a.append(i)

def crawlWeb(seed, maxPages):
  toCrawl = [seed]
  crawled = []
  index = {}
  graph = {}
  while toCrawl and len(crawled) <= maxPages:
    page = toCrawl.pop()
    if page not in crawled:
      pageContent = getPage(page)
      addPageToIndex(index, page, pageContent)
      outlinks = getAllLinks(pageContent)
      
      union(toCrawl, outlinks)
      crawled.append(page)
  return index, graph

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
  if keyword in index:
      index[keyword].append(url)
      return
  # not found, add new keyword to index
  else:
      index[keyword] = [url]
      return

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

def addPageToIndex(index, url, content):
    keywords = content.split()
    for keyword in keywords:
        addToIndex(index, keyword, url)

def getPage(url):
  try:
    return urllib.urlopen(url).read()
  except:
    return ""
