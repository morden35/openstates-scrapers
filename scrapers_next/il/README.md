# Overview - Open States People Scrapers

The goal of the openstates-scrapers/scrapers_next/il/people.py script is to scrape information on Senators and Representatives for the state of Illinois. This information is scraped from the following 'list' web pages:\
https://ilga.gov/senate/default.asp?GA=102
https://ilga.gov/house/default.asp?GA=102

In addition to scraping information from House and Senate 'list' web pages, this script scrapes additional information from each 'detail' web page for each Senator and Representative. An example 'detail' page can be found here:\
https://ilga.gov/senate/Senator.asp?GA=102&MemberID=2886.

## Dependencies

In order to run this code locally, poetry must be installed:

$ curl -sSL https://install.python-poetry.org | python3 -
$ poetry install

Poetry builds your Python virtual environment, and will fetch the correct version of dependencies within a repository. See the [openstates documentation](https://docs.openstates.org/contributing/#poetry) for more detail.

## How to run

First, clone the scraper repository.
$ git clone git@github.com:morden35/openstates-scrapers.git

In order to run the Illlinois people scraper, run the following:
$ poetry run spatula scrape scrapers_next.il.people

For more information on this repository, see the [openstates documentation](https://docs.openstates.org/contributing/scrapers/).

## Code description

## Decisions

## Data storage

