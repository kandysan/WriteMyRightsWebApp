import connexion
import requests
from connexion import NoContent
import yaml

headers = {"Content-Type": "application/json"}

with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())


def process_employment_answers(body):
    r = requests.post(app_config['eventstore1']['url'], json=body, headers=headers)
    return NoContent, r.status_code


app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("wmr.yml", strict_validation=True, validate_responses=True)

if __name__ == "__main__":
    app.run(port=8080)
