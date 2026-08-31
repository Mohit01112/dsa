## hash functions

## CREATING A HASH TABLE FOR THE VOTING SYSTEM

voted={}
def check_voter(name):
    if name in voted:
        print("kick them out")
    else:
        voted[name]=True
        print("let them vote")


## for a cache system

cache={}
def get_page(url):
    if url in cache:
        return cache[url]
    else:
        print("fetching new data")
        data="new data from "+url
        cache[url]=data
        return data
    