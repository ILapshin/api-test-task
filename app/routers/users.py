from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from .. import schemas, models, crud
from ..database import get_db

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(request: schemas.UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db=db, request=request)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db=db, id=id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id {id} not found'
        )
    
    return user