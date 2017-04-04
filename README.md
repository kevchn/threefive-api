# Yelp Restaraunt API Proxy
Backend API Proxy for my submission for the [MindSumo CapitalOne Restaurant Challenge](https://www.mindsumo.com/contests/restaurant-api)

## Deployment
This is deployed using nginx and wsgi on a DigitalOcean droplet (512MB ram).

## Local Deployment
To run this locally, simply install the requirements (in a virtualenv) and then run python app.py.
```
apt-get install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
This API proxy makes use of Flask-CORS, making cross-origin AJAX possible. This means that you can call this API proxy from any domain.

### /business 
> Uses [Yelp Business Search](https://www.yelp.com/developers/documentation/v3/business_search)
#### POST
#### Parameters: 
- `location`: Required. Specifies the combination of "address, neighborhood, city, state or zip, optional country" to be used when searching for businesses.
- `term`: Optional. Search term (e.g. "food", "restaurants"). If term isn’t included we search everything. The term keyword also accepts business names such as "Starbucks".

