#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return Elpais

class Elpais(BaseFeedBook):
    title                 = u'El País'
    description           = u'西班牙《国家报》Noticias de última hora sobre la actualidad en España y el mundo.'
    language              = 'es'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "Elpais.gif"
    coverfile             = "cover-es.jpg"
    feeds = [
            (u'Lo último', 'http://ep00.epimg.net/rss/tags/ultimas_noticias.xml'),
            (u'Lo más visto', 'http://ep00.epimg.net/rss/tags/noticias_mas_vistas.xml'),
            (u'INTERNACIONAL', 'http://ep00.epimg.net/rss/internacional/portada.xml'),
            (u'OPINIÓN', 'http://ep01.epimg.net/rss/elpais/opinion.xml'),
            (u'ESPAÑA', 'http://ep00.epimg.net/rss/politica/portada.xml'),
            (u'ECONOMÍA', 'http://ep00.epimg.net/rss/economia/portada.xml'),
            (u'TECNOLOGÍA', 'http://ep01.epimg.net/rss/tecnologia/portada.xml'),
            (u'CIENCIA', 'http://ep00.epimg.net/rss/elpais/ciencia.xml'),
            (u'ESTILO', 'http://ep00.epimg.net/rss/elpais/estilo.xml'),
            (u'DEPORTES', 'http://ep00.epimg.net/rss/deportes/portada.xml'),
            (u'CULTURA', 'http://ep00.epimg.net/rss/cultura/television.xml'),
            (u'SOCIEDAD', 'http://ep00.epimg.net/rss/sociedad/portada.xml'),
            (u'DEPORTES', 'http://ep00.epimg.net/rss/deportes/portada.xml'),
            ]    
    
    
