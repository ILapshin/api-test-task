# CSV Files Handling Web Service

## Dev Detailes

Developed using FastAPI framework. 

API documentation (created automatically by the FastAPI) is available at /docs and /redocs.

The service allows to upload *.csv files and download with additional filters and sorting queries.
Files are stored on the server as separated files of *.csv format. Files metadata is stored in sqlite database.

User authentication is implemented via WJT token and OAuth2.

File request queries are processed by Pandas library.
