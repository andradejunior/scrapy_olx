"""Item pipeline."""
import pymongo


class MongoPipeline(object):
    """Pipeline class for mongodb."""

    collection_name = 'cars'

    def __init__(self, mongo_uri, mongo_db):
        """Init method."""
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        """From crawler class method."""
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        """Method that execute when open spider."""
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        """Method that xecute when close spider."""
        self.client.close()

    def process_item(self, item, spider):
        """Process item method."""
        self.db[self.collection_name].insert_one(dict(item))
        return item
