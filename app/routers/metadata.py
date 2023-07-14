from fastapi import (
    APIRouter, 
    Depends, 
    status,
    HTTPException
)
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas
from ..database import get_db
from ..security import get_current_user


router = APIRouter(
    prefix='/metadata',
    tags=['Metadata']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.FileMetadata])
async def get_all_files_info(
    db: Session = Depends(get_db), 
    current_user: schemas.User = Depends(get_current_user)
):    
    return crud.get_file_info_all(db=db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.FileMetadata)
async def get_all_files_info(
    id: int, 
    db: Session = Depends(get_db), 
    current_user: schemas.User = Depends(get_current_user)
): 
    file_info = crud.get_file_info(db=db, id=id)
    
    if not file_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return file_info

