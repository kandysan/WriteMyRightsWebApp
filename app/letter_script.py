

def create_employment_letter(body):
    #do script stuff
    print(body)
    return f"this is going to be a letter about {body['name']} who works at {body['company_name']}. " \
           f"His email is {body['email']}."
