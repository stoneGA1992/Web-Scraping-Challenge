# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_fun"
mongo = PyMongo(app)


@app.route("/")
def home():

    # Find data
    mars_ = mongo.db.collection.find_one()

    # return template and data
    return render_template("index.html", mars_=mars_)

# create route that renders index.html template and finds documents from mongo
@app.route("/scrape")
def scrape():
    # Drop Previous Collection
    mongo.db.collection.drop()
    # Run scraped functions
    mars_one = scrape_mars.scrape()

    # Insert forecast into database
    mongo.db.collection.insert_one(mars_one)
    print(mars_one)
    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=False)

  