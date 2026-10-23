from uuid import UUID

from app.database.connection import Base, engine, get_db
from app.models.person import Person 
from app.schema.person import PersonCreate

# camelCase = TestNome
# snake_case = test_nome



class PersonRepo:

    def __init__(self):
        Base.metadata.create_all(bind=engine)
    
    def all(self):
        with get_db() as db:
            return db.query(Person).all()
    
    def create(self, person: PersonCreate):
        db_person = Person(**person.model_dump())

        with get_db() as db:
            db.add(db_person)
            db.commit()
            db.refresh(db_person)
        
            return db_person
    
    def update(self, person_id: UUID, person: PersonCreate):
        with get_db() as db:
            db_person = db.query(Person).filter(Person.id == person_id).one_or_none()
            if person is None:
                return None
            
            db_person.is_active = person.is_active
            db_person.name = person.name
            db_person.age = person.age
            db_person.email = person.email
            db.commit()
            db.refresh(db_person)

            return db_person
    
    def delete(self, people_id: UUID):
        with get_db() as db:
            person = db.query(Person).filter(Person.id == people_id).one_or_none()
            if person is None:
                return None
            
            db.delete(person)
            db.commit()
        
            return True
        
