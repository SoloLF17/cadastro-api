

def get_person_repository():
    from app.repo.person import PersonRepo
    return PersonRepo()

def get_person_service():
    from app.service.person import PersonService
    return PersonService(person_repository=get_person_repository())
