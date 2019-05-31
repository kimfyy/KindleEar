#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return ABC

class ABC(BaseFeedBook):
    title                 = u'ABC'
    __author__            = u'ABC'
    description           = u'ABC 西班牙《ABC报》'
    language              = 'es'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "abc.gif"
    coverfile             = "cover-es.jpg"
    feeds = [
            (u'Portada', 'http://www.abc.es/rss/feeds/abcPortada.xml'),
            (u'Última hora', 'http://www.abc.es/rss/feeds/abc_ultima.xml'),
            (u'España', 'http://www.abc.es/rss/feeds/abc_EspanaEspana.xml'),
            (u'Internacional', 'http://www.abc.es/rss/feeds/abc_Internacional.xml'),
            (u'Economía', 'http://www.abc.es/rss/feeds/abc_Economia.xml'),
            (u'Opinión', 'http://www.abc.es/rss/feeds/abc_opinioncompleto.xml'),
            (u'Deportes', 'http://www.abc.es/rss/feeds/abc_Deportes.xml')
            (u'Conocer', 'http://www.abc.es/rss/feeds/abc_Conocer.xml'),
            (u'Ciencia', 'https://www.abc.es/rss/feeds/abc_Ciencia.xml'),
            (u'Gente & Estilo', 'http://www.abc.es/rss/feeds/abc_Estilo.xml'),
            (u'Summum', 'https://www.abc.es/rss/feeds/abc_Summum.xml'),
            (u'Cultura & Ocio', 'http://www.abc.es/rss/feeds/abc_Cultura.xml'),
            ]