from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String 

from models import Base

class User(Base):
    """
    makes a row in the users table.
    """
    __tablename__ = "users"

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    ## ID is automatically generated when instance is created
    id = Column(Integer, primary_key = True)
    username = Column(String(64), nullable = False)
    email = Column(String(64), nullable = False)
    password = Column(String(64), nullable = False)

    ## optional, for possible future use
    firstname = Column(String(64), nullable = True)
    lastname = Column(String(64), nullable = True)
    home_region = Column(String(64), nullable = True)

    def __repr__(self):
        return "%d, %s, %s, %s, %s" % (self.id, self.username, self.firstname,
            self.lastname, self.home_region)
