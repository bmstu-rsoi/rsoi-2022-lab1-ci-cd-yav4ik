from flask import Flask, request
from src.person import Person

app = Flask(__name__)


@app.route('/persons/<int:person_id>', methods=["GET"])
def get_person(person_id):
    person = Person()
    person_json = person.get_person(person_id)
    if person_json is None:
        return f"person with id {person_id} not found", 404
    return person_json


@app.route('/persons', methods=["GET"])
def get_all_person():
    person = Person()
    persons_json = person.get_all_persons()
    if persons_json is None:
        return f"there's no persons", 404
    return persons_json


@app.route('/persons', methods=["POST"])
def post_person():
    new_person = request.json
    person = Person()
    person_json = person.create_person(new_person)
    if person_json is None:
        return "something wrong", 500
    app.redirect(location='/persons/new_person["personID"]', code=201)


@app.route('/persons/<int:person_id>', methods=["PATCH"])
def patch_person(person_id):
    new_person = request.json
    person = Person()
    person_json = person.get_person(person_id)
    if person_json is None:
        return "something wrong", 500
    return person.update_person(new_person, person_id)


@app.route('/persons/<int:person_id>', methods=["DELETE"])
def delete_person(person_id):
    person = Person()
    person_json = person.get_person(person_id)
    if person_json is None:
        return f"person with id {person_id} not found", 404
    return f"person with id {person_id} deleted"


if __name__ == '__main__':
    app.run()
