import logging
import random
from logging.handlers import RotatingFileHandler
import os
from flask import Flask, escape
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from faker import Faker
import click
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
fake = Faker()

if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler('logs/myflaskapp.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('MyFlaskApp startup')


@app.cli.command('populate-db')
@click.argument('entries', default=10)
def populate_db(entries):
    for _ in range(entries):
        temperature = round(fake.pyfloat(min_value=20, max_value=50, right_digits=2), 2)
        humidity = round(fake.pyfloat(min_value=0, max_value=100, right_digits=2), 2)

        weather_data = WeatherData(temperature=temperature, humidity=humidity)
        db.session.add(weather_data)

    db.session.commit()
    app.logger.info(f'Inserted {entries} fake weather data entries into the db')


class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<WeatherData {self.temperature}, {self.humidity}>'


@app.get("/temperature")
def get_temperature():
    random_temperature = random.randint(-20, 50)
    new_temp = WeatherData(temperature=random_temperature)
    db.session.add(new_temp)
    db.session.commit()
    return f"<p>current temperature: {escape(random_temperature)}</p>"


@app.get("/humidity")
def get_humidity():
    random_humidity = random.randint(0, 100)
    new_hum = WeatherData(humidity=random_humidity)
    db.session.add(new_hum)
    db.session.commit()
    return f"<p>current humidity: {escape(random_humidity)}</p>"


if __name__ == '__main__':
    app.run()
