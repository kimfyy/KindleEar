#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return NYT

class NYT(BaseFeedBook):
    title                 = u'New York Times'
    __author__            = u'NYTimes'
    description           = u'New York Times《纽约时报》'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "NYT.gif"
    coverfile             = "cover-us.jpg"
    feeds = [
            (u'HomePage', 'https://www.nytimes.com/services/xml/rss/nyt/HomePage.xml'),
            (u'World', 'https://www.nytimes.com/services/xml/rss/nyt/World.xml'),
            (u'U.S.', 'https://www.nytimes.com/services/xml/rss/nyt/US.xml'),
            (u'N.Y./Region', 'https://www.nytimes.com/services/xml/rss/nyt/NYRegion.xml'),
            (u'Business', 'http://feeds.nytimes.com/nyt/rss/Business'),
            (u'Technology', 'http://feeds.nytimes.com/nyt/rss/Technology'),
            (u'Sports', 'https://www.nytimes.com/services/xml/rss/nyt/Sports.xml'),
            (u'Science', 'https://www.nytimes.com/services/xml/rss/nyt/Science.xml'),
            (u'Health', 'https://www.nytimes.com/services/xml/rss/nyt/Health.xml'),
            (u'Arts', 'https://www.nytimes.com/services/xml/rss/nyt/Arts.xml'),
            (u'Style', 'https://www.nytimes.com/services/xml/rss/nyt/FashionandStyle.xml'),
            (u'Travel', 'https://www.nytimes.com/services/xml/rss/nyt/Travel.xml'),
            ]    
    
    