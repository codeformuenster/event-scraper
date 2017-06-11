# Models for your scraped items, see:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

# thanks to https://stackoverflow.com/a/40581523/274811
class EventItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    organizer = scrapy.Field()
    url = scrapy.Field()
    source = scrapy.Field()
    startDate = scrapy.Field()
    endDate = scrapy.Field()
    location = scrapy.Field()
    geo = scrapy.Field()

    def __init__(self):
        super().__init__()
        self.fields["@context"] = scrapy.Field()
        # self.fields["@context"] = "http://schema.org"
        self.fields["@type"] = scrapy.Field()
        self.fields["x-category"] = scrapy.Field()
        self.fields["x-tags"] = scrapy.Field()

class OrganizerItem(scrapy.Item):

    def __init__(self):
        super().__init__()
        self.fields["@type"] = scrapy.Field()
        self.fields["name"] = scrapy.Field()

class LocationItem(scrapy.Item):

    def __init__(self):
        super().__init__()
        self.fields["@type"] = scrapy.Field()
        self.fields["name"] = scrapy.Field()
        self.fields["address"] = scrapy.Field()

class GeoItem(scrapy.Item):

    def __init__(self):
        super().__init__()
        self.fields["@type"] = scrapy.Field()
        self.fields["latitude"] = scrapy.Field()
        self.fields["longitute"] = scrapy.Field()

class AddressItem(scrapy.Item):
    addressCountry = scrapy.Field()
    addressLocality = scrapy.Field()
    postalCode = scrapy.Field()
    streetAddress = scrapy.Field()

    def __init__(self):
        super().__init__()
        self.fields["@type"] = scrapy.Field()
