import datetime
import os

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
    print ('main logs')
    try:
        from_timestamp = int(datetime.datetime.fromisoformat(request.json["from_date"]).timestamp() * 1000)
        print('leggo from_timestamp utente:',from_timestamp)
    except:
        print('parto con from_timestamp = 0')
        from_timestamp = 0

    try:
        delta2359= datetime.timedelta(0,0,0,0,0,24)
        read_date = datetime.datetime.fromisoformat(request.json["to_date"])
        to_timestamp = int((read_date + delta2359).timestamp()*1000)     #aggiungo le 23:59 e moltiplico per 1000
        print('leggo to_timestamp utente:',to_timestamp)
    except:
        print('parto con to_timestamp = 0')
        to_timestamp = 0

    bs = get_binance_bot_summary("", request.json["api_key"], request.json["api_secret"], start_timestamp=from_timestamp, end_timestamp=to_timestamp).to_json()
    r = make_response(bs)
    r.mimetype = 'application/json'

    return r


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
