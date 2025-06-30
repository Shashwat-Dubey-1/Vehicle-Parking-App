from models import db, User
from werkzeug.security import generate_password_hash

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        # auto‑create admin if not exists
        if not User.query.filter_by(role='admin').first():
            admin = User(
                username='admin',
                password=generate_password_hash('admin123'),
                role='admin'
            )
            db.session.add(admin)
            db.session.commit()
