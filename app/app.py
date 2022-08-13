from flask import Flask, render_template
from app.extensions import neo4j

app = Flask(__name__)
neo4j.init_app(app)

@app.route('/')
def index():
    return (render_template('index.html'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')

