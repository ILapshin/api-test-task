from sqlalchemy.orm import Session

from . import schemas, models
from .security import get_password_hash

def add_file_metadata(db: Session, request: schemas.FileMetadataBase):
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


def get_file_metadata(db: Session, id: int):
    return db.query(models.FileMetadata).filter(models.FileMetadata.id == id).first()


def get_file_metadata_all(db: Session):
    return db.query(models.FileMetadata).all()


def get_file_metadata_by_filename(db: Session, filename: str):
    return db.query(models.FileMetadata).filter(models.FileMetadata.name == filename).first()


def remove_file_metadata(db: Session, filename: str):
    file_metadata = db.query(models.FileMetadata).filter(models.FileMetadata.name == filename)    
    file_metadata.delete(synchronize_session=False)
    db.commit()
    return 'removed'


def create_user(db: Session, request: schemas.UserBase):
    hashed_password = get_password_hash(request.password)
    new_user = models.User(
        name=request.name, 
        email=request.email, 
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def get_user_by_name(db: Session, username: str):
    return db.query(models.User).filter(models.User.name == username).first()