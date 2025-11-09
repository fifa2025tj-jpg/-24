from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taxi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    phone = db.Column(db.String(32))
    car = db.Column(db.String(120))

class Passenger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    phone = db.Column(db.String(32))
    pickup = db.Column(db.String(255))
    dropoff = db.Column(db.String(255))
    status = db.Column(db.String(20), default='open')
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register_driver', methods=['GET','POST'])
def register_driver():
    if request.method == 'POST':
        d = Driver(
            name=request.form['name'],
            phone=request.form['phone'],
            car=request.form['car']
        )
        db.session.add(d)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('register_driver.html')

@app.route('/register_passenger', methods=['GET','POST'])
def register_passenger():
    if request.method == 'POST':
        p = Passenger(
            name=request.form['name'],
            phone=request.form['phone'],
            pickup=request.form['pickup'],
            dropoff=request.form['dropoff']
        )
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register_passenger.html')

@app.route('/dashboard')
def dashboard():
    passengers = Passenger.query.filter_by(status='open').all()
    drivers = Driver.query.all()
    return render_template('dashboard.html', passengers=passengers, drivers=drivers)

@app.route('/accept/<int:passenger_id>/<int:driver_id>')
def accept(passenger_id, driver_id):
    p = Passenger.query.get(passenger_id)
    p.status = 'accepted'
    p.driver_id = driver_id
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
    from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from pyngrok import ngrok

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taxi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    phone = db.Column(db.String(32))
    car = db.Column(db.String(120))

class Passenger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    phone = db.Column(db.String(32))
    pickup = db.Column(db.String(255))
    dropoff = db.Column(db.String(255))
    status = db.Column(db.String(20), default='open')
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register_driver', methods=['GET','POST'])
def register_driver():
    if request.method == 'POST':
        d = Driver(
            name=request.form['name'],
            phone=request.form['phone'],
            car=request.form['car']
        )
        db.session.add(d)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('register_driver.html')

@app.route('/register_passenger', methods=['GET','POST'])
def register_passenger():
    if request.method == 'POST':
        p = Passenger(
            name=request.form['name'],
            phone=request.form['phone'],
            pickup=request.form['pickup'],
            dropoff=request.form['dropoff']
        )
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register_passenger.html')

@app.route('/dashboard')
def dashboard():
    passengers = Passenger.query.filter_by(status='open').all()
    drivers = Driver.query.all()
    return render_template('dashboard.html', passengers=passengers, drivers=drivers)

@app.route('/accept/<int:passenger_id>/<int:driver_id>')
def accept(passenger_id, driver_id):
    p = Passenger.query.get(passenger_id)
    p.status = 'accepted'
    p.driver_id = driver_id
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    # Иҷрои ngrok барои дастрасӣ аз интернет
    public_url = ngrok.connect(5000)
    print("Сайти шумо онлайн аст ва дастрасӣ дорад аз интернет:", public_url)
    
    app.run(host='0.0.0.0', port=5000, debug=True)
    from pyngrok import ngrok

# Эҷоди туннел барои порт 5000
public_url = ngrok.connect(5000)
print("Сайти шумо онлайн аст ва дастрасӣ дорад аз интернет:", public_url)
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from pyngrok import ngrok

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taxi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Моделҳои базаи маълумот
class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    phone = db.Column(db.String(32))
    car = db.Column(db.String(120))

class Passenger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    phone = db.Column(db.String(32))
    pickup = db.Column(db.String(255))
    dropoff = db.Column(db.String(255))
    status = db.Column(db.String(20), default='open')
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))

# Саҳифаҳои веб
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register_driver', methods=['GET','POST'])
def register_driver():
    if request.method == 'POST':
        d = Driver(
            name=request.form['name'],
            phone=request.form['phone'],
            car=request.form['car']
        )
        db.session.add(d)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('register_driver.html')

@app.route('/register_passenger', methods=['GET','POST'])
def register_passenger():
    if request.method == 'POST':
        p = Passenger(
            name=request.form['name'],
            phone=request.form['phone'],
            pickup=request.form['pickup'],
            dropoff=request.form['dropoff']
        )
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register_passenger.html')

@app.route('/dashboard')
def dashboard():
    passengers = Passenger.query.filter_by(status='open').all()
    drivers = Driver.query.all()
    return render_template('dashboard.html', passengers=passengers, drivers=drivers)

@app.route('/accept/<int:passenger_id>/<int:driver_id>')
def accept(passenger_id, driver_id):
    p = Passenger.query.get(passenger_id)
    p.status = 'accepted'
    p.driver_id = driver_id
    db.session.commit()
    return redirect(url_for('dashboard'))

# Иҷрои сервер
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    # Ngrok барои дастрасӣ аз интернет
    public_url = ngrok.connect(5000)
    print("Сайти шумо онлайн аст ва дастрасӣ дорад аз интернет:", public_url)
    
    app.run(host='0.0.0.0', port=5000, debug=True)