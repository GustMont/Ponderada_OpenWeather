from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///openweatherdata.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    class OpenWeather(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        ingestion_date = db.Column(db.DateTime, default=datetime.utcnow)
        data_type = db.Column(db.String(50))
        values = db.Column(db.Float)
        usage = db.Column(db.String(50))

    @app.route('/get_openweatherdata')
    def get_openweatherdata():
        api_key = 'put_the_api_key_here'
        cities = ['Santos', 'Socorro', 'Franca', 'Guarulhos', 'Campinas', 'Osasco', 'Sorocaba', 'Diadema', 'Bauru', 'Barueri']  

        openweatherdata = []
        for city in cities:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
            response = requests.get(url)
            data = response.json()

            openweatherentry = OpenWeather(
                data_type='Weather',
                values=data['main']['temp'],
                usage='Exemplo de Uso'
            )
            db.session.add(openweatherentry)
            db.session.commit()

            openweatherdata.append({
                'data_ingestao': openweatherentry.ingestion_date.strftime('%Y-%m-%d %H:%M:%S'),
                'tipo': openweatherentry.data_type,
                'valores': openweatherentry.values,
                'uso': openweatherentry.usage
            })

        return jsonify(openweatherdata)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
