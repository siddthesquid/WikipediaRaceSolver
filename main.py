# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:43:41 2014

@author: james
"""

from pattern.web import *
from random import randint
from gensim import *

#oliver_twist_full_text = URL('http://www.gutenberg.org/ebooks/730.txt.utf-8').download()
#print oliver_twist_full_text

w = Wikipedia()


def search(start):
    """takes in a string start 
    
    returns the list of links on the page"""
    return w.search(start)

def find_link(article):
    """takes in an article 
    
    returns its links"""
    return article.links
    
     
def next_destination(links):
    """takes in a list of links called link 
    
    retuns the next article"""
    new_article = search(links[randint(0,len(links))])
    return new_article

def wiki_race(start, end):
    """ takes in strings for start and end pages for the wiki race
    
    returns the end page
    """
    start_article = search(start)
    links = find_link(start_article)
    while not(next_destination(links) == end):
        new_article = next_destination(links)
        
        
    
    
destination = "Babson College"
start = "Olin College"
first = search(start)
for l in first.links:
    if l == destination:
        print w.search(l).title
        print w.search(l).plaintext()

#print next_destination(find_link(first))
#print find_link(search(start))