from typing import Annotated
from fastapi import (
    APIRouter, 
    UploadFile,
    Depends, 
    Query,
    status,
    HTTPException
)
from fastapi.responses import Response
from sqlalchemy.orm import Session

from .. import csv_handler, crud, schemas
from ..database import get_db
from ..checksum import get_checksum
from ..security import get_current_user


router = APIRouter(
    prefix='/files',
    tags=['Files']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.FileMetadata)
async def upload_file(
    file: UploadFile, 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user)
):

    filename = file.filename
    
    # SCV format validation
    if file.headers['content-type'] != 'text/csv':
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='File format must be .csv'
        )
    
    # Checking name collisions
    if crud.get_file_metadata_by_filename(db=db, filename=filename):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'File with name {filename} is already uploaded'
        )
    
    # Saving file to storage
    await csv_handler.store_csv(file=file, filename=filename)

    csv_head = csv_handler.get_head(filename=filename)

    bytes_data = await file.read()
    file_checksum = get_checksum(bytes_data)

    file_info = schemas.FileMetadataBase(
        name=filename,
        size=file.size,
        csv_schema=','.join(csv_head),
        checksum=file_checksum
    )

    # Adding file info to database
    new_file_info = crud.add_file_info(db, file_info)

    return new_file_info


@router.delete('/{filename}', status_code=status.HTTP_204_NO_CONTENT)
async def remove_file(
    filename: str, 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user)
):
    file_info = crud.get_file_metadata_by_filename(db=db, filename=filename)

    if not file_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)    
    
    filename = file_info.name
    
    crud.remove_file_metadata(db=db, filename=filename)

    csv_handler.remove_csv(filename=filename)

    return f'File {filename} removed'


@router.get('/{filename}', status_code=status.HTTP_200_OK)
async def download_file(
    filename: str, 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
    sort: Annotated[list[str] | None, Query()] = None,
    filter: Annotated[list[str] | None, Query()] = None
):
    file_info = crud.get_file_metadata_by_filename(db=db, filename=filename)

    if not file_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND) 
    
    filename = file_info.name

    binary_file = csv_handler.get_csv(
        filename=filename, 
        filter=filter, 
        sort=sort
    )

    return Response(content=binary_file, media_type="text/csv")

