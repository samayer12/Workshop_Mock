import requests


def get_data():
    response = requests.get('http://xkcd.com')
    return response.status_code


def give_advice(in_file):
    with open(in_file, 'r') as file:
        advice = "Flatten the curve!\n"
        for person in file:
            advice += (person[0:-1] + ', be sure to wash your hands!\n')
        return advice
