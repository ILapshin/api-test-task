import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import models, crud, schemas
from app.database import get_db
from app.main import app
from app.security import create_access_token


DATABASE_URL_TEST = 'sqlite:///./database_test.db'

engine_test = create_engine(
    DATABASE_URL_TEST,
    connect_args={'check_same_thread': False}
)

TestingSessionLocal = sessionmaker(bind=engine_test, autocommit=False, autoflush=False)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)




@pytest.fixture(scope='session')
def prepare_database():
    models.Base.metadata.drop_all(engine_test)
    models.Base.metadata.create_all(bind=engine_test)
    db = TestingSessionLocal()
    crud.create_user(db, schemas.UserBase(
        name='admin',
        email='admin@admin@com',
        password='admin'
    ))
    db.close()
    print('DB prepared')


@pytest.fixture()
def fake_user():
    fake_user = {
        'name': 'FakeUser',
        'email': 'fake@user.com',
        'password': 'password'
    }
    return fake_user


@pytest.fixture(scope='session')
def access_token():
    access_token = create_access_token(
        data={'sub': 'admin'}
    )   
    return access_token