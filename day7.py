## code for the breadth nfirst search

from collections import deque

from django.db.migrations import graph


def person_is_seller(name):
    return name[-1]=="m"
def search(name):
    from collections import deque
    search_queue=deque()
    search_queue+=graph[name]
    searched=[]
    while search_queue:
        person=search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person+" is a seller")
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False

search("you")