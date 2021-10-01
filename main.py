import datetime

from flask import Flask, render_template, request, make_response
from flask_cors import CORS

from binance_bot_summary import get_binance_bot_summary

app = Flask(__name__)
CORS(app,  resources={r"/bot-stats": {"origins": "*"}})


@app.template_filter('ztb')
def zero_to_blank(n: float, f: str):
    return f.format(n) if n != 0 else ''


@app.template_filter('millis_to_date')
def millis_to_date(t: int):
    return '{}'.format(datetime.datetime.fromtimestamp(t / 1000).isoformat(timespec='minutes'))


@app.route("/bot-stats",  methods=['POST'])
def bot_stats():
    try:
        from_timestamp = int(datetime.datetime.fromisoformat(request.json["from_date"]).timestamp() * 1000)
    except:
        from_timestamp = 0

    try:
        if request.form["last"] == 'True':
            to_timestamp = 0
        else:
            to_timestamp = int(datetime.datetime.fromisoformat(request.json["to_date"]).timestamp() * 1000)
    except:
        to_timestamp = 0

    bs = get_binance_bot_summary("", request.json["api_key"], request.json["api_secret"], start_timestamp=from_timestamp, end_timestamp=to_timestamp).to_json()
    r = make_response(bs)
    r.mimetype = 'application/json'

    return r


if __name__ == "__main__":
    app.run(debug=True)
