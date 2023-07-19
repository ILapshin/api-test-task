# CSV Files Handling Web Service

The service allows to upload *.csv files and download with additional filters and sorting queries.
Files are stored on the server as separated files of *.csv format. Files metadata is stored in sqlite database.

## Deployment

For running the application you must have [git](https://git-scm.com/downloads) and [python 3.10](https://www.python.org/downloads/release/python-31011/) installed.

Clone the repository to the host folder with command:

```
git clone https://github.com/ILapshin/csv-web-service.git
```
Or copy source code and unpack the archive to the destination folder.


### Running Directly Via Uvicorn

1. Navigate to repository root folder. Create and activate python virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

2. Install requirements:

```
pip3 install -r requirements.txt
```

3. Run server with command 

```
uvicorn app.main:app 
```

Application will be running on http://localhost:8000. 

Saved CSV files and SQLite database will be stored in ```./uploads``` directory

### Running With Docker

1. Create docker image:

```
docker build -t csv-web-app .
```

2. Create docker volume for storing permanent data:
```
docker volume create scv-storage
```

3. Run docker container:
```
docker run -p 8000:8000 -v csv-storage:/code csv-web-app
```

Volume folder will be associated with the container, database and uploaded csv files will remain after container stops or is killed.

## Dev Notes

Developed using FastAPI framework. 

API documentation (created automatically by the FastAPI) is available in Swagger format at http://localhost:8000/docs.

User authentication is implemented via JWT token and OAuth2.

File request queries are processed by Pandas library.


### Possible Improvements
- Security sensitive data must be moved to enviroment variables.
- Paths to database and uploaded CSV files directory are hard coded. Should be implemented as config or environment variables.
- CSV files are queried by ID, it would be better to implement query by file name.
- List of CSV columns is better to be returned as a list, not as a single string.
- Get existing user endpoint is for demo purposes only, should be removed in production.

## Testing

All api endpoint are covered by unit tests via pytest.


