from flask import Flask, request, jsonify
from lolhistory import ELO_MAP, get_all_ranks

app = Flask(__name__)


@app.route("/tft-history")
def tft_history():
    summoner_name = request.args.get("summoner_name")

    match_history = get_all_ranks(summoner_name)
    if not match_history:
        return "Not Found", 404
    return jsonify(match_history)


@app.route("/elo-map")
def elo_map():
    return jsonify(ELO_MAP)