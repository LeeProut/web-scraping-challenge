## Mission to Mars
* web scraping with Pandas, Beautiful Soup, and Splinter using Jupyter Notebook
* creating an app to display the data retrieved using MongoDB with Flask
* end user can easily retrieve the latest information with a simple click

---

#### Source sites: 
* [NASA Mars News Site](https://mars.nasa.gov/news) with recent news items about Mars.
* [NASA Space Images Site](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) with Mars Images from the Jet Propulsion Laboratory at California Institute of Technology.
* [Space Facts Site](https://space-facts.com/mars/) with a Mars planet profile. 
* [USGS Site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) with images of each of Mars' four hemispheres. 

---

#### Web scraping

Initial web scraping was done in a Jupyter notebook that can be viewed [here](https://github.com/LeeProut/web-scraping-challenge/blob/main/Missions_to_Mars/mission_to_mars.ipynb). 

#### MongoDB and Flask Application

The Jupyter notebook was converted into a Python script that can be viewed [here](https://github.com/LeeProut/web-scraping-challenge/blob/main/Missions_to_Mars/scrape_mars.py). It defined a `scrape` function to execute scraping code and return a Python dictionary that contains the scraped data. 

Created an app using Flask, with code that can be viewed [here](https://github.com/LeeProut/web-scraping-challenge/blob/main/Missions_to_Mars/app.py). The root route queries the Mongo database and passes the Mars data into an [HTML template](https://github.com/LeeProut/web-scraping-challenge/blob/main/Missions_to_Mars/templates/index.html) to display on a webpage. The `/scrape` route imports the Python [script](https://github.com/LeeProut/web-scraping-challenge/blob/main/Missions_to_Mars/scrape_mars.py) and calls the scrape function to retrieve new data when the user clicks the "Scrape New Data" button on the page. 

##### The finished product is interactive, with a clean design: 

![Mission to Mars](/Missions_to_Mars/images/MissiontoMars1.png)

![Mars Hemispheres Images](/Missions_to_Mars/images/MissiontoMars2.png)

##### The information updates with each click of the "Scrape New Data" button. The most striking retrieval is the "Featured Mars Image." 


**Featured Image retrieved** | **updated Featured Image**
--------------------- | ---------------------
![Mission to Mars](/Missions_to_Mars/images/MissiontoMars1.png) | ![Mission to Mars](/Missions_to_Mars/images/MtoMFeatImg.png)

##### The design is responsive to screen size: 

![Responsive Design Display](/Missions_to_Mars/images/MtoMresponsive1.png)



