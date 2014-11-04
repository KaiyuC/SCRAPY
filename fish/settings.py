# Scrapy settings for fish project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'fish'

SPIDER_MODULES = ['fish.spiders']
NEWSPIDER_MODULE = 'fish.spiders'
ITEM_PIPELINES = {
    'fish.pipelines.FishPipeline':300,
}
