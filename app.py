from flask import Flask, render_template
from database import init_db
app = Flask(__name__)
app.config['SECRET_KEY'] = 'devkey55'
app.config['SQLALCHEM_DATABASE_URI'] = 'sqlite:///parking.db'
init_db(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)