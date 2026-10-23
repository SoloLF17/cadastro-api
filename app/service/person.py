from app.repo.person import PersonRepo


class PersonService:
    def __init__(self, person_repository: PersonRepo):
        self.person_repository = person_repository

    def list_persons(self):
        return self.person_repository.all()

    def get_person(self, person_id):
        return self.person_repository.get(person_id)

    def create_person(self, person_data):
        return self.person_repository.create(person_data)

    def update_person(self, person_id, person_data):
        return self.person_repository.update(person_id, person_data)

    def delete_person(self, person_id):
        return self.person_repository.delete(person_id)