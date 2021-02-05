import connexion
from connexion import NoContent
import letter_script


def process_employment_answers(body):
    start_employment_script(body)
    return NoContent, 201


def start_employment_script(body):
    letter = letter_script.create_employment_letter(body)
    print(letter)
    return letter


app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("api.yml", strict_validation=True, validate_responses=True)


if __name__ == "__main__":
    app.run(port=8080)
