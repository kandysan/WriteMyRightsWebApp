from sqlalchemy import Column, Integer, String, DateTime
from Storage.base import Base
import datetime


class Users(Base):
    """ Stores user info """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    geo_location = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    date_created = Column(DateTime, nullable=False)

    def __init__(self, name, geo_location, email):
        """ Initializes a Delivery orders """
        self.name = name
        self.geo_location = geo_location
        self.email = email
        self.date_created = datetime.datetime.now()

    def to_dict(self):
        """ Dictionary Representation of a delivery orders """
        dict = {}
        dict['name'] = self.name
        dict['geo_location'] = self.geo_location
        dict['email'] = self.email
        dict['date_created'] = self.date_created
        return dict
