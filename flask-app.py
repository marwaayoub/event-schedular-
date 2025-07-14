from flask import Flask, render_template, request, redirect, jsonify
from database import db, Event
from datetime import datetime
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Initialize database
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    query = Event.query
    search_title = request.args.get('title')
    search_location = request.args.get('location')
    search_start_date = request.args.get('start_date')
    search_end_date = request.args.get('end_date')
    search_status = request.args.get('status')

    if search_title:
        query = query.filter(Event.title.ilike(f'%{search_title}%'))
    if search_location:
        query = query.filter(Event.location.ilike(f'%{search_location}%'))
    if search_start_date:
        start_date = datetime.strptime(search_start_date, '%Y-%m-%d')
        query = query.filter(Event.datetime >= start_date)
    if search_end_date:
        end_date = datetime.strptime(search_end_date, '%Y-%m-%d').replace(hour=23, minute=59, second=59)
        query = query.filter(Event.datetime <= end_date)
    if search_status:
        query = query.filter(Event.status == search_status)

    events = query.all()
    return render_template('index.html', events=events)

@app.route('/suggest-location')
def suggest_location():
    title = request.args.get('title', '').lower()
    suggestion = ''
    if 'coffee' in title:
        suggestion = 'Starbucks'
    elif 'lunch' in title:
        suggestion = 'Local Restaurant'
    elif 'meeting' in title:
        suggestion = 'Office, Conference Room A'
    elif 'doctor' in title or 'appointment' in title:
        suggestion = 'City Clinic'
    elif 'gym' in title or 'workout' in title:
        suggestion = 'Downtown Gym'
    elif 'party' in title:
        suggestion = 'Community Hall'
    return jsonify({'suggestion': suggestion})

@app.route('/add', methods=['POST'])
def add_event():
    title = request.form['title']
    datetime_str = request.form['datetime']
    location = request.form['location']
    description = request.form['description']
    status = request.form['status']
    
    datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
    
    new_event = Event(title=title, datetime=datetime_obj, location=location, description=description, status=status)
    if not new_event.description:
        new_event.description = random.choice([
            "This event focuses on networking and professional growth.",
            "A casual gathering for community building and fun.",
            "Strategic planning session with key stakeholders.",
            "A celebratory event marking an important milestone.",
            "An educational workshop designed for skill development."
        ])
    
    db.session.add(new_event)
    db.session.commit()
    
    return redirect('/')

@app.route('/delete/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    if request.method == 'POST':
        event.title = request.form['title']
        event.datetime = datetime.strptime(request.form['datetime'], '%Y-%m-%dT%H:%M')
        event.location = request.form['location']
        event.description = request.form['description']
        event.status = request.form['status']
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', event=event)

if __name__ == '__main__':
    app.run(debug=True) 