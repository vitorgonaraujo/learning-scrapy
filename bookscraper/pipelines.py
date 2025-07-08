# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)
        field_names = adapter.field_names()

        for field_name in field_names:
            if field_name != "description":
                value = adapter.get(field_name)

                if isinstance(value, str):
                    adapter[field_name] = value.strip()
                elif isinstance(value, (list, tuple)):
                    adapter[field_name] = [
                        v.strip() if isinstance(v, str) else v for v in value
                    ]

        return item
