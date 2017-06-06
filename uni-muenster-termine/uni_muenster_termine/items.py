# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class EventItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    organizer = scrapy.Field()
    url = scrapy.Field()
    x_tags = scrapy.Field()
    source = scrapy.Field()
    x_category = scrapy.Field()
    startDate = scrapy.Field()
    endDate = scrapy.Field()
    location = scrapy.Field()
    geo = scrapy.Field()

class OrganizerItem(scrapy.Item):
    name = scrapy.Field()

class LocationItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()

class GeoItem(scrapy.Item):
    latitude = scrapy.Field()
    longitute = scrapy.Field()

class AddressItem(scrapy.Item):
    addressCountry = scrapy.Field()
    addressLocality = scrapy.Field()
    postalCode = scrapy.Field()
    streetAddress = scrapy.Field()

