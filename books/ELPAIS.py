#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return Elpais

class Elpais(BaseFeedBook):
    title                 = 'El País'
    description           = '西班牙《国家报》Noticias de última hora sobre la actualidad en España y el mundo.'
    language              = 'es'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "Elpais.gif"
    coverfile             = "cover-es.jpg"
    feeds = [
        ('Lo último', 'http://ep00.epimg.net/rss/tags/ultimas_noticias.xml'),
        ('Lo más visto', 'http://ep00.epimg.net/rss/tags/noticias_mas_vistas.xml'),
        ('INTERNACIONAL', 'http://ep00.epimg.net/rss/internacional/portada.xml'),
        ('OPINIÓN', 'http://ep01.epimg.net/rss/elpais/opinion.xml'),
        ('ESPAÑA', 'http://ep00.epimg.net/rss/politica/portada.xml'),
        ('ECONOMÍA', 'http://ep00.epimg.net/rss/economia/portada.xml'),
        ('TECNOLOGÍA', 'http://ep01.epimg.net/rss/tecnologia/portada.xml'),
        ('CIENCIA', 'http://ep00.epimg.net/rss/elpais/ciencia.xml'),
        ('ESTILO', 'http://ep00.epimg.net/rss/elpais/estilo.xml'),
        ('DEPORTES', 'http://ep00.epimg.net/rss/deportes/portada.xml'),
        ('CULTURA', 'http://ep00.epimg.net/rss/cultura/television.xml'),
        ('SOCIEDAD', 'http://ep00.epimg.net/rss/sociedad/portada.xml'),
        ('DEPORTES', 'http://ep00.epimg.net/rss/deportes/portada.xml'),
        ]    
    
    