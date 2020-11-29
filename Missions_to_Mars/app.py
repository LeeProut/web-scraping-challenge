from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 
import scrape_mars

app = Flask(__name__)

#assemble configuration with Mongo URI connection string, name of Mongo database (mars_db)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.route('/')
def index():
    mars_news = mongo.db.news.find_one()
    return render_template('index.html', mars_news = mars_news)

@app.route('/scrape')
def scrape():
    mars_news = scrape_mars.scrape()
    #add data collection called "news" to mongo, set upsert to True for a single document in collection at a time, updating the data if available.
    mongo.db.news.update({}, mars_news, upsert=True)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
