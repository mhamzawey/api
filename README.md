**Project Target:**

    - A multi website agenda

    - Collect all the cultural activities in Berlin into one.
    - The specifications:
        -Collect the information for your website from other web sources.
            - https://www.co-berlin.org/en/calender
            - http://berghain.de/events/
    - Events filter: User can filter the events based on different criteria:
          - Web Source
          - Dates
          - Simple partial text search on title.

**Implementation:**

    - Implement the code needed to parse 2 of the "web sources" into the standardized format.
    - Implement the code needed to collect the standardized format and render it in a website.
    - Add some simple filtering mechanism (based on backend filtering, not frontend JS filtering)
    - Prepare your code for easy deployment



------------------------------------------------------------------------------------------------------------------------------

**Prerequisites**:

- docker
- docker-compose

**Starting Project:**

`git clone  https://github.com/mhamzawey/dalia_challenge api`

1- cd api

2- docker-compose up -d --build

3- wait 2-3 minutes till the composer builds and starts the containers
P.S: sometimes cron tasks are not triggered automatically,
so for testing purposes, execute the following command from your terminal:
``docker exec -it api  python3 /app/scrapy_app/scrapy_events/core.py``

4- Go to your browser:

    - To access the swagger documentation for the api visit -> http:localhost:4000/swagger, to see the whole CRUD use session login, username: admin ,password:123456

    - To access the front-end visit -> http:localhost:3000/

**Project Setup:**

we have three docker contaiers:

**1- api:**

    - built on top of Ubuntu:16.04
    - This api is a Django project that has two apps:
        1- events:
            - A model called `event` which has those attributes: `{id, title ,description, category, start_date, end_date, link ,created_at, updated_at}`
            - Serializer that serializes the `event` Model with the proper data-types
            - We have two main filters in this api:
                -Search filter:
                    - Responsible for filtering using title, description, and category
                -FilterSet
                    - Responsible for filtering using:
                        - title: exact, in, starts_with, contains
                        - description: exact, in, starts_with, contains
                        - category: exact, in, starts_with, contains
                        - start_date: exact, lte, gte, lt, gt, in
                        - end_date: exact, lte, gte, lt, gt, in
                        - link: exact, in, contains
                        - created_at: exact, lte, gte, lt, gt, in
                        - updated_at: exact, lte, gte, lt, gt, in
            - Test case: added test case for retrieval of events to assert serializer && response status
            - To run test case manually : `docker exec -it api python3 manage.py test`
            - Used Cirrus CI which uses dalia_challenge container `.cirrus.yml`
    
            
        2- scrappy_app:
            - A crawler that's built on the Scrapy Framework that has two spiders:
                - co_berlin: that scrapes the events on co_berlin website
                - berghain: that scrapes the events on berghain website

            - This is scalable as we can define any other spider we need and handle its case and map it to our own serializer
            - Scrapping done as a crontask that gets registered once the api container is up and running
                - Cron job runs every 1 minute, this can be enhanced according to the needed time.

<img width="960" alt="capture" src="https://user-images.githubusercontent.com/5594052/47461927-43826580-d7e2-11e8-8ba1-203f879d0749.PNG">


**2- mysqldb:**

    - Built on top of mysql:5.7
    - Doesn't persist data, can be presisted by adding volumes to the docker-compose file

**3- front-end:**

    - Built on top of node:7.8.0
    - A versy simple ReactJS app that integrates with the api
    - It fetches from the `api` the events and has a search bar that does backend searching on `title`, `category`, `description`
    - There's another endpoint that can filter by dates that you can access via the swagger documentation `events/filter/`
    
 

