import re
from utils import url_xpath, State
from .events import UTEventScraper
from .bills import UTBillScraper


class Utah(State):
    scrapers = {
        "events": UTEventScraper,
        "bills": UTBillScraper,
    }
    legislative_sessions = [
        {
            "_scraped_name": "2011 General Session",
            "classification": "primary",
            "identifier": "2011",
            "name": "2011 Regular Session",
            "start_date": "2011-01-24",
            "end_date": "2011-03-10",
        },
        {
            "_scraped_name": "2011 1st Special Session",
            "classification": "special",
            "identifier": "2011S1",
            "name": "2011, 1st Special Session",
            "start_date": "2011-03-25",
            "end_date": "2011-03-25",
        },
        {
            "_scraped_name": "2011 2nd Special Session",
            "classification": "special",
            "identifier": "2011S2",
            "name": "2011, 2nd Special Session",
            "start_date": "2011-07-20",
            "end_date": "2011-07-20",
        },
        {
            "_scraped_name": "2011 3rd Special Session",
            "classification": "special",
            "identifier": "2011S3",
            "name": "2011, 3rd Special Session",
            "start_date": "2011-10-03",
            "end_date": "2011-10-17",
        },
        {
            "_scraped_name": "2012 General Session",
            "classification": "primary",
            "identifier": "2012",
            "name": "2012 General Session",
            "start_date": "2012-01-23",
            "end_date": "2012-03-08",
        },
        {
            "_scraped_name": "2012 4th Special Session",
            "classification": "special",
            "identifier": "2012S4",
            "name": "2012, 4th Special Session",
            "start_date": "2012-06-20",
            "end_date": "2012-06-20",
        },
        {
            "_scraped_name": "2013 General Session",
            "classification": "primary",
            "identifier": "2013",
            "name": "2013 General Session",
            "start_date": "2013-01-28",
            "end_date": "2013-03-14",
        },
        {
            "_scraped_name": "2013 House Session",
            "classification": "special",
            "identifier": "2013h1",
            "name": "2013 House Session",
            "start_date": "2013-07-03",
            "end_date": "2013-07-03",
        },
        {
            "_scraped_name": "2013 1st Special Session",
            "classification": "special",
            "identifier": "2013s1",
            "name": "2013 1st Special Session",
            "start_date": "2013-07-17",
            "end_date": "2013-07-17",
        },
        {
            "_scraped_name": "2013 2nd Special Session",
            "classification": "special",
            "identifier": "2013s2",
            "name": "2013 2nd Special Session",
            "start_date": "2013-10-16",
            "end_date": "2013-10-16",
        },
        {
            "_scraped_name": "2014 General Session",
            "classification": "primary",
            "identifier": "2014",
            "name": "2014 General Session",
            "start_date": "2014-01-27",
            "end_date": "2014-03-13",
        },
        {
            "_scraped_name": "2015 General Session",
            "classification": "primary",
            "identifier": "2015",
            "name": "2015 General Session",
            "start_date": "2015-01-26",
            "end_date": "2015-03-12",
        },
        {
            "_scraped_name": "2015 1st Special Session",
            "classification": "special",
            "identifier": "2015s1",
            "name": "2015 1st Special Session",
            "start_date": "2015-08-19",
            "end_date": "2015-08-19",
        },
        {
            "_scraped_name": "2016 General Session",
            "classification": "primary",
            "identifier": "2016",
            "name": "2016 General Session",
            "start_date": "2016-01-25",
            "end_date": "2016-03-10",
        },
        {
            "_scraped_name": "2016 2nd Special Session",
            "classification": "special",
            "identifier": "2016S2",
            "name": "2016 2nd Special Session",
            "start_date": "2016-05-18",
            "end_date": "2016-05-18",
        },
        {
            "_scraped_name": "2016 3rd Special Session",
            "classification": "special",
            "identifier": "2016S3",
            "name": "2016 3rd Special Session",
            "start_date": "2016-07-13",
            "end_date": "2016-07-13",
        },
        {
            "_scraped_name": "2016 4th Special Session",
            "classification": "special",
            "identifier": "2016S4",
            "name": "2016 4th Special Session",
            "start_date": "2016-11-16",
            "end_date": "2016-11-16",
        },
        {
            "_scraped_name": "2017 General Session",
            "classification": "primary",
            "identifier": "2017",
            "name": "2017 General Session",
            "start_date": "2017-01-23",
            "end_date": "2017-03-09",
        },
        {
            "_scraped_name": "2017 1st Special Session",
            "classification": "special",
            "identifier": "2017S1",
            "name": "2017 1st Special Session",
            "start_date": "2017-09-20",
            "end_date": "2017-09-20",
        },
        {
            "_scraped_name": "2018 General Session",
            "classification": "primary",
            "identifier": "2018",
            "name": "2018 General Session",
            "start_date": "2018-01-22",
            "end_date": "2018-03-08",
        },
        {
            "_scraped_name": "2018 2nd Special Session",
            "classification": "special",
            "identifier": "2018S2",
            "name": "2018 2nd Special Session",
            "start_date": "2018-07-18",
            "end_date": "2018-07-18",
        },
        {
            "_scraped_name": "2018 3rd Special Session",
            "classification": "special",
            "identifier": "2018S3",
            "name": "2018 3rd Special Session",
            "start_date": "2018-12-03",
            "end_date": "2018-12-03",
        },
        {
            "_scraped_name": "2019 General Session",
            "classification": "primary",
            "identifier": "2019",
            "name": "2019 General Session",
            "start_date": "2019-01-28",
            "end_date": "2019-03-08",
        },
        {
            "_scraped_name": "2019 1st Special Session",
            "classification": "special",
            "identifier": "2019S1",
            "name": "2019 1st Special Session",
            "start_date": "2019-09-16",
            "end_date": "2019-09-16",
        },
        {
            "_scraped_name": "2019 2nd Special Session",
            "classification": "special",
            "identifier": "2019S2",
            "name": "2019 2nd Special Session",
            "start_date": "2019-12-11",
            "end_date": "2019-12-12",
        },
        {
            "_scraped_name": "2020 General Session",
            "classification": "primary",
            "identifier": "2020",
            "name": "2020 General Session",
            "start_date": "2020-01-27",
            "end_date": "2020-03-12",
        },
        {
            "_scraped_name": "2020 3rd Special Session",
            "classification": "special",
            "identifier": "2020S3",
            "name": "2020 3rd Special Session",
            "start_date": "2020-04-15",
            "end_date": "2020-04-17",
        },
        {
            "_scraped_name": "2020 4th Special Session",
            "classification": "special",
            "identifier": "2020S4",
            "name": "2020 4th Special Session",
            "start_date": "2020-04-27",
            "end_date": "2020-05-01",
        },
        {
            "_scraped_name": "2020 5th Special Session",
            "classification": "special",
            "identifier": "2020S5",
            "name": "2020 5th Special Session",
            "start_date": "2020-06-18",
            "end_date": "2020-06-20",
        },
        {
            "_scraped_name": "2020 6th Special Session",
            "classification": "special",
            "identifier": "2020S6",
            "name": "2020 6th Special Session",
            "start_date": "2020-08-20",
            # TODO: Proper end date after session
            "end_date": "2020-08-28",
        },
        {
            "_scraped_name": "2021 General Session",
            "classification": "primary",
            "identifier": "2021",
            "name": "2021 General Session",
            "start_date": "2021-01-19",
            # TODO: proper end date after session
            "end_date": "2021-03-12",
        },
        {
            "_scraped_name": "2021 1st Special Session",
            "classification": "special",
            "identifier": "2021S1",
            "name": "2021 1st Special Session",
            "start_date": "2021-05-19",
            # TODO: Proper end date after session
            "end_date": "2020-05-28",
        },
        {
            "_scraped_name": "2021 1st House Extraordinary Session",
            "classification": "special",
            "identifier": "2021S1H",
            "name": "2021 1st House Extraordinary Session",
            "start_date": "2021-05-19",
            "end_date": "2021-05-25",
        },
        {
            "_scraped_name": "2021 1st Senate Extraordinary Session",
            "classification": "special",
            "identifier": "2021S1S",
            "name": "2021 1st Senate Extraordinary Session",
            "start_date": "2021-05-19",
            "end_date": "2021-05-25",
        },
    ]
    ignored_scraped_sessions = [
        "2022 General Session",
        "2013 1st House Session",
        "2011 Veto Override Session",
        "2010 2nd Special Session",
        "2010 General Session",
        "2009 1st Special Session",
        "2009 General Session",
        "2008 2nd Special Session",
        "2008 General Session",
        "2007 1st Special Session",
        "2007 General Session",
        "2006 5th Special Session",
        "2006 4th Special Session",
        "2006 3rd Special Session",
        "2006 General Session",
        "2005 2nd Special Session",
        "2005 1st Special Session",
        "2005 General Session",
        "2004 4th Special Session",
        "2004 3rd Special Session",
        "2004 General Session",
        "2003 2nd Special Session",
        "2003 1st Special Session",
        "2003 General Session",
        "2002 Veto Override Session",
        "2002 6th Special Session",
        "2002 5th Special Session",
        "2002 4th Special Session",
        "2002 3rd Special Session",
        "2002 General Session",
        "2001 2nd Special Session",
        "2001 1st Special Session",
        "2001 General Session",
        "2000 General Session",
        "1999 General Session",
        "1998 General Session",
        "1997 2nd Special Session",
        "1997 1st Special Session",
        "1997 General Session",
        "1990-1996",
    ]

    def get_session_list(self):
        sessions = url_xpath(
            "https://le.utah.gov/asp/billsintro/index.asp?year=2021X1",
            "//select[@id='Listbox1']/option/text()",
        )
        return [re.sub(r"\s+", " ", session.strip()) for session in sessions]
