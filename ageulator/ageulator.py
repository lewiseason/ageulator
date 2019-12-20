import os
import sys
import math
from datetime import datetime
from flask import Flask, request, render_template, jsonify


app = Flask(__name__)
application = app

try:
    birthday = datetime.strptime(os.environ["BIRTHDAY"], '%Y-%m-%d')
except KeyError:
    raise RuntimeError("Please supply a birthday in YYYY-MM-DD format "
                       "via the BIRTHDAY environment variable")
    sys.exit(1)


def request_wants_json():
    order = ['application/json', 'text/html']
    best = request.accept_mimetypes.best_match(order)

    return best == 'application/json' and \
        request.accept_mimetypes[best] > request.accept_mimetypes['text/html']


@app.route("/")
def age():
    days = (datetime.now() - birthday).days
    years = int(math.floor(days / 365.2425))

    if request_wants_json():
        return jsonify(days=days, years=years)
    else:
        return render_template("age.html", days=days, years=years)
