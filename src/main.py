import redis
from flask import Flask
import datetime
app = Flask(__name__)


@app.route("/")
def index():
    r = redis.Redis(host='redis', port=6379, db=0)
    r.rpush('visits', datetime.datetime.now())
    count = r.llen('visits')

    if count == 1:
        return "You have accessed this website 1 time".format(count=count)
    else:
        return "You have accessed this website {count} times".format(count=count)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
