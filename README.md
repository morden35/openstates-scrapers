# Overview - Open States People Scrapers

The goal of the [openstates-scrapers/scrapers_next/il/people.py](https://github.com/morden35/openstates-scrapers/blob/il_people_example/scrapers_next/il/people.py) script is to scrape information on Senators and Representatives for the state of Illinois. This information is scraped from the following 'list' web pages:\
https://ilga.gov/senate/default.asp?GA=102 \
https://ilga.gov/house/default.asp?GA=102

In addition to scraping information from House and Senate 'list' web pages, this script scrapes additional information from 'detail' web pages for each Senator and Representative. An example 'detail' page can be found here:\
https://ilga.gov/senate/Senator.asp?GA=102&MemberID=2886.

## Dependencies

In order to run this code locally, the [poetry library](https://pypi.org/project/poetry/) must be installed. Do so by running the following from the command line:

`$ curl -sSL https://install.python-poetry.org | python3 -`

## How to run

First, clone the scraper repository and navigate to the repository: \
`$ git clone git@github.com:morden35/openstates-scrapers.git` \
`$ cd openstates-scrapers/`

Poetry builds your Python virtual environment, and will fetch the correct version of dependencies within a repository. See the [openstates documentation](https://docs.openstates.org/contributing/#poetry) for more detail. To install the dependencies into a new virtual environment, run the following:

`$ poetry install`

In order to run the Illinois people scraper, run the following: \
`$ poetry run spatula scrape scrapers_next.il.people`

For more information on the structure of this repository, see the [openstates documentation](https://docs.openstates.org/contributing/scrapers/).

## Data Model

At the top of the [openstates-scrapers/scrapers_next/il/people.py](https://github.com/morden35/openstates-scrapers/blob/il_people_example/scrapers_next/il/people.py) file, you will find the following line: \
`from openstates.models import ScrapePerson`

This line imports our data model class, ScrapePerson, from the openstates-core repository:
https://github.com/openstates/openstates-core/blob/main/openstates/models/people.py

The ScrapePerson data model includes attributes that we want to acquire for each Senator and Representative from the state of Illinois, such as a given person's name, party, district, etc.

## Code description

Within the [openstates-scrapers/scrapers_next/il/people.py](https://github.com/morden35/openstates-scrapers/blob/il_people_example/scrapers_next/il/people.py) file, you will find 4 classes:

### House

The House class is set up to scrape the house ['list' page](https://ilga.gov/house/default.asp?GA=102). This class defines the 'source' and 'chamber' attributes before calling the LegList class.

### Senate

The Senate class is set up to scrape the senate ['list' page](https://ilga.gov/senate/default.asp?GA=102). This class defines the 'source' and 'chamber' attributes before calling the LegList class.

### LegList

The goal of the LegList class is to scrape information for each Senator and Representative from the given 'list' pages. To do so, we first define our XPath selector. The selector identifies the rows (represented by `<tr>` html elements) we want to input into the process_item() function. process_item() will be called for each `<tr>` from the selector (61 rows for the IL Senate page, 120 rows for the IL House page).

For each row, process_item() will then scrape the availble information (name, party, district) using CSS selectors and add it to the ScrapePerson object. process_item() also scrapes the 'detail link' for each row, which is the url to that Senator's/Representative's detailed page.

Finally, process_item() calls the LegDetail class, passing in the ScrapePerson object and the url to the person's 'detail' page.

More information on the spatula library and scraping a 'list' page can be found here: \
https://jamesturk.github.io/spatula/scraper-basics/#scraping-a-list-page

### LegDetail

Each Senator and Representative has a 'detail' page, which contains more information that we'd like to scrape and add to our data model. The LegDetail class takes in the ScrapePerson object and adds the following attributes to the object: image, capitol address, captiol phone, capitol fax, district address, district phone, district fax, and email.

Example 'detail' page: https://ilga.gov/senate/Senator.asp?GA=102&MemberID=2886

More information on the spatula library and scraping a 'detail' page can be found here: \
https://jamesturk.github.io/spatula/scraper-basics/#scraping-a-single-page

## Decisions

One decision that we had to make while scraping web pages was whether or not to use XPath versus CSS selectors. On one hand, CSS selectors are more straightforward and easier to learn than XPath selectors. CSS selectors have a lower learning curve for new developers, in my opinion. However, XPath selectors have some functionality that CSS selectors lack (ex: text matching, substring matching). For Open States, our rule of thumb was to default to CSS selectors, and if they can’t get the job done, use XPath in more complicated cases.

You will notice that the [openstates-scrapers/scrapers_next/il/people.py](https://github.com/morden35/openstates-scrapers/blob/il_people_example/scrapers_next/il/people.py) script contained 1 XPath selector, and a number of CSS selectors. I chose to use the XPath selector in the LegList class because I wanted to grab the rows from the 'Current Senate/House Members' table, and not the 'Former Senate/House Members' table. XPath allows us to specify which table we want to scrape (only the first), where CSS does not.

## Data storage

According to the [spatula docs](https://jamesturk.github.io/spatula/data-models/#data-models-as-output), when running `spatula scrape`, data is written to disk as JSON. After running the following command: `$ poetry run spatula scrape scrapers_next.il.people`, the scraped data can be found in the `openstates-scrapers/scrapers_next/il/_scrapes/<date_of_scrape>` folder.

In the long term, the JSON data on disk gets imported into a PostgreSQL database.

## Citations

https://jamesturk.github.io/spatula/ \
https://docs.openstates.org/
