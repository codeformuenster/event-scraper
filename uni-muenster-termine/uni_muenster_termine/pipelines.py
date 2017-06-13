# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class UniMuensterTerminePipeline(object):
    def process_item(self, item, spider):
        # item["@json-ld"] = "test"
        # item["@json-ld"] = _at_json_ld
        # del item["_at_json_ld"]
        return item
