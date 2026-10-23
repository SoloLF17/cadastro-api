from uuid import UUID

from fastapi import Depends, APIRouter
from app.deps import get_person_service
from app.schema.person import PersonCreate, PersonResponse
from app.service.person import PersonService

router = APIRouter(prefix="/v1", tags=["Pessoas"])
# camelCase = TestNome
# snake_case = test_nome

# REST SOLID API
# GET - PEGAR
# POST - CRIAR
# PUT - ATUALIZAR
# DELETE - MATAR


@router.post("/people", response_model=PersonResponse, status_code = 201)
def create_person(person: PersonCreate, service: PersonService =Depends(get_person_service)):
    return service.create_person(person)


@router.get("/persons", response_model=list[PersonResponse])
def list_person(service: PersonService =Depends(get_person_service)):
    return service.list_persons()



@router.put("/people/{people_id}", response_model=PersonResponse, status_code = 200)
def update_person(people_id: UUID, person: PersonCreate, service: PersonService =Depends(get_person_service)):
    db_person = service.update_person(people_id, person)
    if db_person is None:
        return {"mensagem": "Usuário não encontrado!"}

    return db_person


@router.delete("/people/{people_id}", status_code = 200)
def update_person(people_id: UUID,service: PersonService =Depends(get_person_service)):
    db_person = service.delete_person(people_id)
    if db_person is None:
        return {"mensagem": "Usuário não encontrado!"}
    
    return {"mensangem": "Usuário EXCLUIDO!!"}
