import random

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


def create_app(config_filename):
    app.config.from_pyfile(config_filename)
    return app


@app.get("/temperature")
def get_temperature():
    random_temperature = random.randint(-20, 50)
    return f"<p>current temperature: {escape(random_temperature)}</p>"


@app.get("/humidity")
def get_humidity():
    random_humidity = random.randint(0, 100)
    return f"<p>current humidity: {escape(random_humidity)}</p>"


if __name__ == '__main__':
    app.run()