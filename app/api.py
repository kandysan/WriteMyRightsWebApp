import connexion
from app import letter_script
import yaml
from connexion import NoContent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Storage.base import Base
from Storage.users import Users

with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

DB_ENGINE = create_engine('mysql+pymysql://root:P@ssw0rd@localhost:3306/wmrdb')

Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)


def process_employment_answers(body):
    start_employment_script(body)
    store_user_info(body)
    return NoContent, 201


def start_employment_script(body):
    letter = letter_script.create_employment_letter(body)
    print(letter)
    return letter


def store_user_info(body):
    session = DB_SESSION()
    ea = Users(body['name'],
               body['address'],  # this must be changed when we find out how to grab geo location
               body['email'])
    session.add(ea)
    session.commit()
    session.close()
    return NoContent, 201


app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("../wmr.yml", strict_validation=True, validate_responses=True)

if __name__ == "__main__":
    app.run(port=8080)
