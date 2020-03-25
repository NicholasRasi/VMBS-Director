import argparse
import yaml
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('index.html', bin_database_url=cfg["bin_database_url"])


if __name__ == "__main__":
    # open config file
    with open("config_dashboard.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    print(cfg["bin_database_url"])

    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8082)
    args = parser.parse_args()
    app.run(debug=True, host='0.0.0.0', port=args.port)
