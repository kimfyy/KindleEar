#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return ELMUNDO

class ELMUNDO(BaseFeedBook):
    title                 = u'El Mundo'
    __author__            = u'El Mundo'
    description           = u'西班牙《世界报》'
    language              = 'es'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "elmundo.gif"
    coverfile             = "cover-es.jpg"
    
    feeds = [
            (u'Portada', 'http://estaticos.elmundo.es/elmundo/rss/portada.xml'),
            (u'Deportes', 'http://estaticos.elmundo.es/elmundodeporte/rss/portada.xml'),
            (u'Economía', 'http://estaticos.elmundo.es/elmundo/rss/economia.xml'),
            (u'España', 'http://estaticos.elmundo.es/elmundo/rss/espana.xml'),
            (u'Internacional', 'http://estaticos.elmundo.es/elmundo/rss/internacional.xml'),
            (u'Cultura', 'http://estaticos.elmundo.es/elmundo/rss/cultura.xml'),
            (u'Ciencia/Ecología', 'http://estaticos.elmundo.es/elmundo/rss/ciencia.xml'),
            (u'Comunicación', 'http://estaticos.elmundo.es/elmundo/rss/comunicacion.xml'),
            (u'Televisión', 'http://estaticos.elmundo.es/elmundo/rss/television.xml'),
            (u'Salud', 'http://estaticos.elmundo.es/elmundosalud/rss/portada.xml'),
            (u'Solidaridad', 'http://estaticos.elmundo.es/elmundo/rss/solidaridad.xml'),
            (u'Su vivienda', 'http://estaticos.elmundo.es/elmundo/rss/suvivienda.xml'),
            (u'Motor', 'http://estaticos.elmundo.es/elmundodeporte/rss/motor.xml'),
            (u'Madrid', 'http://estaticos.elmundo.es/elmundo/rss/madrid.xml'),
            (u'Barcelona', 'http://estaticos.elmundo.es/elmundo/rss/barcelona.xml'),
            (u'País Vasco', 'http://estaticos.elmundo.es/elmundo/rss/paisvasco.xml'),
            (u'Baleares', 'http://estaticos.elmundo.es/elmundo/rss/baleares.xml'),
            (u'Castilla y León', 'http://estaticos.elmundo.es/elmundo/rss/castillayleon.xml'),
            (u'Valladolid', 'http://estaticos.elmundo.es/elmundo/rss/valladolid.xml'),
            (u'Valencia', 'http://estaticos.elmundo.es/elmundo/rss/valencia.xml'),
            (u'Alicante', 'http://estaticos.elmundo.es/elmundo/rss/alicante.xml'),
            (u'Castellón', 'http://estaticos.elmundo.es/elmundo/rss/castellon.xml'),
            (u'Andalucía', 'http://estaticos.elmundo.es/elmundo/rss/andalucia.xml'),
            (u'Sevilla', 'http://estaticos.elmundo.es/elmundo/rss/andalucia_sevilla.xml'),
            (u'Málaga', 'http://estaticos.elmundo.es/elmundo/rss/andalucia_malaga.xml')
            ]
