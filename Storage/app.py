import connexion
from connexion import NoContent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Storage.base import Base
from Storage.employment_answers import Employment_Answers

DB_ENGINE = create_engine("sqlite:///surveys.sqlite")
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)


def process_employment_answers(body):
    session = DB_SESSION()

    ea = Employment_Answers(body['name'],
                            body['company_name'],
                            body['boss_name'],
                            body['time_worked'],
                            body['severance'],
                            body['email'])

    session.add(ea)

    session.commit()
    session.close()
    return NoContent, 201


app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("wmr.yml", strict_validation=True, validate_responses=True)

if __name__ == "__main__":
    app.run(port=8090)
