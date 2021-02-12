import connexion
from connexion import NoContent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Storage.base import Base
from Storage.users import Users
import yaml

with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

DB_ENGINE = create_engine(
    'mysql+pymysql://' + app_config['datastore']['user'] + ':' + app_config['datastore']['password'] +
    '@' + app_config['datastore']['hostname'] + ':' + app_config['datastore']['port'] + '/' + app_config['datastore'][
        'db'])

Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)


def process_employment_answers(body):
    session = DB_SESSION()
    ea = Users(body['name'],
               body['address'],  # this must be changed when we find out how to grab geo location
               body['email'])
    session.add(ea)
    session.commit()
    session.close()
    return NoContent, 201


app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("wmr.yml", strict_validation=True, validate_responses=True)

if __name__ == "__main__":
    app.run(port=8080)
