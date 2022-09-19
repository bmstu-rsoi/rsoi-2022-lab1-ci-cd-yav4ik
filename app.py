from flask import Flask, request, jsonify, make_response
from src.person import Person

app = Flask(__name__)


@app.route('/api/v1/persons/<int:person_id>', methods=["GET"])
def get_person(person_id):
    person = Person()
    person_json = person.get_person(person_id)
    if person_json is None:
        return f"person with id {person_id} not found", 404

    response = app.response_class(
        response=person_json,
        status=200,
        mimetype='application/json'
    )

    return response


@app.route('/api/v1/persons', methods=["GET"])
def get_all_person():
    person = Person()
    persons_json = person.get_all_persons()
    if persons_json is None:
        return f"there's no persons", 404

    response = app.response_class(
        response=persons_json,
        status=200,
        mimetype='application/json'
    )

    return response


@app.route('/api/v1/persons', methods=["POST"])
def post_person():
    new_person = request.json
    person = Person()
    person_id = person.create_person(new_person)
    if person_id is None:
        return "something wrong", 500
    return app.redirect(location=f'{request.host_url}api/v1/persons/{int(person_id)}', code=201)


@app.route('/api/v1/persons/<int:person_id>', methods=["PATCH"])
def patch_person(person_id):
    new_person = request.json
    person = Person()
    person.update_person(new_person, person_id)
    person_json = person.get_person(person_id)
    if person_json is None:
        return "something wrong", 500

    response = app.response_class(
        response=person_json,
        status=200,
        mimetype='application/json'
    )

    return response, 200


@app.route('/api/v1/persons/<int:person_id>', methods=["DELETE"])
def delete_person(person_id):
    person = Person()
    person_json = person.get_person(person_id)
    if person_json is None:
        return f"person with id {person_id} not found", 404
    return f"person with id {person_id} deleted", 204


if __name__ == '__main__':
    app.run()
