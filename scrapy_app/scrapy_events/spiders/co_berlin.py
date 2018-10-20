import scrapy
import string
import datetime
from events.models import Event
from events.serializers import EventSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer



class CoBerlin(scrapy.Spider):
    name = "co_berlin"
    BASE_URL = "https://www.co-berlin.org/en"

    def start_requests(self):
        urls = [
            self.BASE_URL+"/calender",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def clean_text(self,text):
        printable = set(string.printable)
        return ''.join(filter(lambda x: x in printable, text))

    def parse(self, response):
        for event in response.css(".seite-c-single"):
            title = event.css(".article-title::text").extract_first()
            category = event.css(".article-category::text").extract_first()
            desc = event.css(".article-text::text").extract_first()
            href = self.BASE_URL + event.css(".seite-c-single ::attr(href)").extract_first()
            print(event.css(".date-display-start ::attr(content)").extract_first())
            try:
                start = [x.strip() for x in event.css(".date-display-start ::attr(content)").extract_first().split('T')][0]
                start = datetime.datetime.strptime(start, '%Y-%m-%d').strftime('%d/%m/%y')
                end = [x.strip() for x in event.css(".date-display-end ::attr(content)").extract_first().split('T')][0]
                end = datetime.datetime.strptime(end, '%Y-%m-%d').strftime('%d/%m/%y')
            except:
                start = [x.strip() for x in event.css(".date-display-single ::attr(content)").extract_first().split('T')][0]
                start = datetime.datetime.strptime(start, '%Y-%m-%d').strftime('%d/%m/%y')
                end = start


            event_object = Event(title=title,start_date=start,end_date=end,category=category,link=href,description=desc)
            serializer = EventSerializer(event_object)
            content = JSONRenderer().render(serializer.data)
            stream = io.BytesIO(content)
            data = JSONParser().parse(stream)
            serializer = EventSerializer(data=data)
            serializer.is_valid()
            serializer.save()


