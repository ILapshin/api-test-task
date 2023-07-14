from pydantic import BaseModel

class FileMetadataBase(BaseModel):
    name: str
    size: int
    csv_schema: str
    checksum: str

class FileMetadata(FileMetadataBase):
    id: int

class UserBase(BaseModel):
    name: str
    email: str
    password: str

class User(BaseModel):
    name: str
    email: str