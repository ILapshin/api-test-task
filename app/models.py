from sqlalchemy import Column, Integer, String

from .database import Base

class FileMetadata(Base):
    __tablename__ = 'file_metadata'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    size = Column(Integer)
    csv_schema = Column(String)
    checksum = Column(String)
