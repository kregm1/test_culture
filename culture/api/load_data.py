import json

from .models import Theatre


def main():
    with open('api/data-87-structure-3.json', 'r') as file:
        data = json.load(file)

    for theater_data in data:
        theater_data = theater_data['data']['general']
        print(theater_data)
        theater_name = theater_data['name']
        legal_entity = theater_data['organization']['name']
        type = theater_data['organization']['type']
        address = theater_data['address']['fullAddress']
        subordination = theater_data['organization']['subordination']['name']

        if 'mapPosition' in theater_data['address']:
            coordinates_x = theater_data['address']['mapPosition']['coordinates'][0]
            coordinates_y = theater_data['address']['mapPosition']['coordinates'][1]

        if 'contacts' in theater_data:

            if 'website' in theater_data['contacts']:
                website = theater_data['contacts']['website']

            if 'email' in theater_data['contacts']:
                email = theater_data['contacts']['email']

        if 'inn' in theater_data['organization']:
            inn = theater_data['organization']['inn']

        theater = Theatre(
            name=theater_name,
            address=address,
            legal_entity=legal_entity,
            subordination=subordination,
            website=website,
            email=email,
            inn=inn,
            type=type,
            coordinates_x=coordinates_x,
            coordinates_y=coordinates_y,
        )
        theater.save()