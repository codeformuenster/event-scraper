# Scrapy settings for tutorial project, see:
# - http://doc.scrapy.org/en/latest/topics/settings.html
# - http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# - http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'uni_muenster_termine'

SPIDER_MODULES = ['uni_muenster_termine.spiders']
NEWSPIDER_MODULE = 'uni_muenster_termine.spiders'

FEED_EXPORT_ENCODING = 'utf-8'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Code for Münster (+https://github.com/codeformuenster/event-api)'

ROBOTSTXT_OBEY = True

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Item pipelines, see:
# http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'uni_muenster_termine.pipelines.UniMuensterTerminePipeline': 300,
# }
