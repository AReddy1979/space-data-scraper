# space-data-scraper
This is a scraper program that scrapes space data from various sources
such as spaceweatherlive and NOAA. The user can do various things with this data that
is scraped, which includes viewing the raw data and viewing them in graphs.

The repository contains several files which contain the backend and frontend for the scraping of these various 
datasets. The flask_app file is the main program that runs the web application. The web application is how you interact with our program.
# Running the Program
To use our space data scraper you can visit our website <a href = "http://96.255.219.52/">here</a>
<br>
To run the tests: Tests are run in CI/CD pipeline.

# Navigating the Website
First begin by visiting the website listed in the section above. This will take you to the home page.
From there, there are numerous tabs that will direct you to various information related to space data.
Currently, the tabs that are currently supported are the Space Weather, about, feed, and solar flare tab. Clicking 
on the space weather tab will direct you to a directory page which has various buttons that lead to different
graphs. You can click on the buttons to show the graphs you want to see. The feed tab currently
displays current space weather information all in one place and allows for customization of what is shown. You can customize the data shown by checking off the boxes.
The about tab lists all the sources we scraped our data off of and other general information.

# Group Efforts and Tasks

#### Abhinav: 20%
Added a customization feature for what appears on the user's feed and created unit tests for customization feature. Wrote backend for following users and customizing community page 
#### Derek: 20%
Created HTML and CSS template for general layout of website. Fixed file parsing. Wrote tests for file parsing. Added layout for community page and help page. Added information to about page and help page.
#### Maurice: 10%
Began set up of user login system. (Login system incomplete due to personal issues that came up)
#### John: 25%
Created graphs showing last 24 hours of space weather activity and last 7 days of solar wind temperatures. Worked on connecting
backend with frontend. Helped add CI/CD implementation. Connected space weather feed backend to frontend.
#### Johnny: 25%
Created graphs showing solar wind density and speeds for the last 7 days. Helped connect frontend with backend. Updated README.
Wrote tests for space_weather_fetcher and solar_weather_fetcher. Added CI/CD implementation. Added source page and solar flare information.


