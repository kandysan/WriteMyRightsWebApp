import connexion
import requests
from connexion import NoContent

headers = {"Content-Type": "application/json"}
STORAGE_URL = "http://localhost:8090/"


def process_employment_answers(body):
    r = requests.post(STORAGE_URL + "employment_answers", json=body, headers=headers)
    return NoContent, r.status_code


app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("wmr.yml", strict_validation=True, validate_responses=True)

if __name__ == "__main__":
    app.run(port=8080)
