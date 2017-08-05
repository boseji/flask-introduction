"""Redirects.

Sometimes we'll need to redirect our user's request to another resource.
Examples include times when the user is not authenticated and we want to
redirect her to the /login page or when a resource has changed its name.

Performing redirects is simple in Flask. Remember to pay attention to the
HTTP Status Codes.
"""

from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('request_info'))


@app.route('/info')
def info():
    return redirect(url_for('request_info'), code=301)


@app.route('/request-info')
def request_info():
    # Get location info using https://freegeoip.net/
    #geoip_url = 'http://freegeoip.net/json/{}'.format(request.remote_addr)
    geoip_url = 'http://freegeoip.net/json/{}'.format(
        request.headers['X-Forwarded-For'])
    client_location = requests.get(geoip_url).json()
    return render_template('request/info.html',
                           client_location=client_location)
