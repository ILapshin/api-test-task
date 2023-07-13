from sqlalchemy.orm import Session

from . import schemas, models

def add_file_info(db: Session, request: schemas.FileMetadataBase):
    new_file_info = models.FileMetadata(
        name=request.name,
        size=request.size,
        csv_schema=request.csv_schema,
        checksum=request.checksum
    )
    db.add(new_file_info)
    db.commit()
    db.refresh(new_file_info)

    return new_file_info


def get_file_info(db: Session, id: int):
    return db.query(models.FileMetadata).filter(models.FileMetadata.id == id).first()


def get_file_info_all(db: Session):
    return db.query(models.FileMetadata).all()


def search_name(db: Session, filename: str):
    return db.query(models.FileMetadata).filter(models.FileMetadata.name == filename).first()


def remove_file_info(db: Session, id: int):
    file_info = db.query(models.FileMetadata).filter(models.FileMetadata.id == id)    
    file_info.delete(synchronize_session=False)
    db.commit()
    return 'removed'
