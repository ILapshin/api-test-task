from fastapi import (
    APIRouter, 
    Depends, 
    status,
    HTTPException
)
from sqlalchemy.orm import Session
from typing import List

from .utils import parse_metadata
from .. import crud, schemas
from ..database import get_db
from ..security import get_current_user


router = APIRouter(
    prefix='/metadata',
    tags=['Metadata']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.FileMetadata])
async def get_metadata_all(
    db: Session = Depends(get_db), 
    current_user: schemas.User = Depends(get_current_user)
):    
    metadata = crud.get_file_metadata_all(db=db)
    return [parse_metadata(item) for item in metadata]


@router.get('/{filename}', status_code=status.HTTP_200_OK, response_model=schemas.FileMetadata)
async def get_metadata(
    filename: str, 
    db: Session = Depends(get_db), 
    current_user: schemas.User = Depends(get_current_user)
): 
    file_metadata = crud.get_file_metadata_by_filename(db=db, filename=filename)
    
    if not file_metadata:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return parse_metadata(file_metadata)

