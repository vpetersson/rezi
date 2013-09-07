import os
import pymongo
import platform

from bottle import route, run

# Naively assumes all devs use OS X.
is_osx = None
bind = None
if 'Darwin' in platform.platform():
    bind = '127.0.0.1'
    is_osx = True
else:
    bind = '0.0.0.0'
    is_osx = False

# Conditional setup for Mongo.
# Use localhost on OS X and env settings for Heroku.
def mongo_connect():
    if is_osx:
        mongo_string = 'mongodb://localhost:27017/'
        app_name = 'rezi'
    else:
        mongo_string = os.environ.get('MONGOHQ_URL')
        app_name = mongo_string.split('/')[-1]

    connection = pymongo.Connection(mongo_string)
    db = connection[app_name]

    users = db.users
    restaurants = db.restaurants
    neighborhoods = db.neighborhoods
    listings = db.listings

    return {
        'users': users,
        'restaurants': restaurants,
        'neighborhoods': neighborhoods,
        'listings': listings,
    }

@route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    run(host=bind, port=int(os.environ.get('PORT', 5000)))
