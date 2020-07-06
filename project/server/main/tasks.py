# project/server/main/tasks.py

import time

from project.server import db
from project.server.models  import User


def send_email(email, body):
    time.sleep(15)
    user = User.query.filter_by(email=email).first()
    user.email_sent = True
    db.session.commit()
    return True
