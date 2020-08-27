# LA County Public Health News Release Scrape

## Description
A simple script to scrape the case numbers provided by the LA County Public Health department for each city in Los Angeles County

Used Python version 3.7

## Modules Required

- BeautifulSoup (https://pypi.org/project/beautifulsoup4/)
- requests

## Scrape Process

1.    Pulls data from News Release URL: http://publichealth.lacounty.gov/phcommon/public/media/mediapubhpdetail.cfm?prid=2614
      When the latest release comes out, change this URL within the code to pull a different news release.
2.    Slice out the city and case count data from the raw data
3.    Output the data to Excel

## Code
In the list of files in this directory, click on cityscrape.py (https://github.com/jamesvalencia1/la-county-pub-health-scrape/blob/master/cityscrape.py)
