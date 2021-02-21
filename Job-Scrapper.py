import requests, time
from bs4 import BeautifulSoup

#This one works as a marker for times whn "junior" appear
def jr(l):
    l=l.lower()
    if "jr" in l or "junior" in l:
        return 1
    else:
        return 0

#This is the one that brings the dicts together
#last_first and checker are used so jooble doesnt keep repeating pages once we
#have no more results.
def searcher(dicturls, dictusage):
    total_len= 0
    total_jr= 0
    for x, y in dicturls.items():
        print(x)
        last_first= set()
        checker = set()
        job_offers= {}
        page=1
        while True:
            time.sleep(3)
            link= requests.get(y)
            libs= BeautifulSoup(link.text, "html.parser")
            if x == "jb":
                posts= libs.find_all("article", class_=dictusage[x][0])
            else:
                posts= libs.find_all("div", class_=dictusage[x][0])
            if x == "tr":
                for l in posts:
                    if "Jobleads" in l.p.text:
                        continue
                    checker.add(l.h4.text)
                    job_offers[l.h4.text] = l.h4.a.get("href")
            else:
                for l in posts:
                    checker.add(l.h2.text)
                    job_offers[l.h2.text] = l.h2.a.get("href")
            if len(posts) == 0 or last_first.issuperset(checker):
                print(f"There's no page {page}")
                break
            else:
                checker= checker.symmetric_difference(last_first)
                last_first = last_first.union(checker)
                for z in checker:
                    total_len+=1
                    total_jr += jr(z)
                    print(z)
                    print(dictusage[x][2] + job_offers[z])
#Now this is where stuff gets messy, since every site has an unique way of going to the next page, there are explicit instructions for every site
            y, action, page = dictusage[x][3](libs, page, x, y)
            if action == "Keepgoing":
                print(f"Now going to page {page} ({y})")
                continue
            elif action == "Stop":
                break
        print(str(total_len) + " jobs were discovered")
        print(str(total_jr) + " jr discovered")

#This one changes pages to the next one according to how the pages work
def pages_jb(bsobject, page, website, url):
#JB is a pretty straigth page, the buttons only work trough the browser, so i manually change the page,
#when it reaches the limit, it goes one more page, it verifies that there isnt content (with len(posts)).
    next_page= page+1
    if url[-4:-1] == "?p=":
        return url[:-1] + str(next_page), "Keepgoing", next_page
    return url + f"?p={next_page}", "Keepgoing", next_page

#In Indeed you have a hard time manipulating the url, cuz pages are set by "&start" where once you go pass the limit,
#it starts to show unexpected behaviour, so here we manipulate the list of pages at the bottom.
def pages_i(bsobject, page, website, url):
    next_page= 0
    buttons = bsobject.find("ul", class_="pagination-list").find_all("li")
    for x in buttons:
        if next_page == 0:
            try:
                if "true" == x.b.get("aria-current"):
                    next_page = 1
            except:
                continue
        elif next_page == 1:
            return "https://ar.indeed.com" + x.a.get("href"), "Keepgoing", page + 1
    if next_page == 1:
            return "Nothing", "Stop", page

def pages_tr(bsobject, page, website, url):
    next_page=page+1
    if url[-2] == "/":
        return url[:-1]+ str(next_page), "Keepgoing", next_page
    return url + f"/{next_page}", "Keepgoing", next_page

def pages_ct(*args):
    return "", "Stop", 1





notyet='""opem":"https://www.opcionempleo.com.ar/empleo-web-developer/cordoba-113878.html""', '"zj": "https://www.zonajobs.com.ar/cordoba/ofertas-de-empleo-categoria-tecnologia.html",'
urls={
"i": "https://ar.indeed.com/Empleos-de-Software-developer-en-C%C3%B3rdoba,-C%C3%B3rdoba",
"ct": "https://www.computrabajo.com.ar/trabajo-de-programador-en-cordoba-en-capital",
"tr": "https://empleo.trovitargentina.com.ar/trabajo-developer-en-c%C3%B3rdoba,-c%C3%B3rdoba",
"jb": "https://ar.jooble.org/trabajo-front-end/Cordoba%2C-C%C3%B3rdoba",
}
usage={
#[0] is the class of the div were the important info is,
#[1] is just a reminder of were the title is, the code no longer uses these,
#[2] is the domainer for whenever the link needs it,
#[3] are there other pages in the search?
"i": ["jobsearch-SerpJobCard", "h2", "ar.indeed.com", pages_i],
"ct": ["iO", "h2", "www.computrabajo.com.ar", pages_ct],
"tr": ["item-info", "h4", "", pages_tr],
"jb": ["_31572 _07ebc", "h2", "ar.jooble.org", pages_jb],
}
searcher(urls, usage)
