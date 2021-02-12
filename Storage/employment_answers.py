from sqlalchemy import Column, Integer, String, DateTime
from Storage.base import Base
import datetime


class Employment_Answers(Base):
    """ Delivery Orders """

    __tablename__ = "employment_answers"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    company_name = Column(String(250), nullable=False)
    company_address = Column(String(250), nullable=False)
    boss_name = Column(String(250), nullable=False)
    time_worked = Column(String(250), nullable=False)
    severance = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    date_created = Column(DateTime, nullable=False)

    def __init__(self, name, address, company_name, company_address, boss_name, time_worked, severance, email):
        """ Initializes a Delivery orders """
        self.name = name
        self.address = address
        self.company_name = company_name
        self.company_address = company_address
        self.boss_name = boss_name
        self.time_worked = time_worked
        self.severance = severance
        self.email = email
        self.date_created = datetime.datetime.now()

    def to_dict(self):
        """ Dictionary Representation of a delivery orders """
        dict = {}
        dict['name'] = self.name
        dict['address'] = self.address
        dict['company_name'] = self.company_name
        dict['company_address'] = self.company_address
        dict['boss_name'] = self.boss_name
        dict['time_worked'] = self.time_worked
        dict['severance'] = self.severance
        dict['email'] = self.email
        dict['date_created'] = self.date_created
        return dict
