import scrapy
import string
from events.models import Event
from events.serializers import EventSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

import datetime

#http://berghain.de/events/


class Berghain(scrapy.Spider):
    name = "berghain"

    BASE_URL ="http://berghain.de"

    events_url = BASE_URL+"/events/{}"

    months = ["2018-10","2018-11","2018-10","2018-12","2018-09","2019-02"]



    urls = []
    for month in months:
        urls.append(events_url.format(month))



    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def clean_text(self,text):
        printable = set(string.printable)
        return ''.join(filter(lambda x: x in printable, text))

    def parse(self, response):
        for type in response.css(".navi_level3_extra ::attr(class)"):
            if type.extract() != "navi_level3_extra":
                _class = ".col_teaser_{}"
                for event in response.css(_class.format(type.extract())):
                    dict = {}
                    date =[x.strip() for x in event.css("."+type.extract()+" ::attr(title)").extract_first().split(':')][0]
                    title = [x.strip() for x in event.css("."+type.extract()+" ::attr(title)").extract_first().split(':')][1]
                    start = datetime.datetime.strptime(date, '%a %d %B %Y').strftime('%d/%m/%y')
                    end = datetime.datetime.strptime(date, '%a %d %B %Y').strftime('%d/%m/%y')
                    category = response.css("."+type.extract() +"::text").extract_first()
                    href = self.BASE_URL + event.css("."+type.extract()+" ::attr(href)").extract_first()
                    desc = event.css("."+type.extract()+"_color span::text").extract()[1]




                    event_object = Event(title=title,start_date=start,end_date=end,category=category,link=href,description=desc)
                    serializer = EventSerializer(event_object)
                    content = JSONRenderer().render(serializer.data)
                    stream = io.BytesIO(content)
                    data = JSONParser().parse(stream)
                    serializer = EventSerializer(data=data)
                    serializer.is_valid()
                    serializer.save()





