$ CRUD_API
CRUD API for Client and Project entities
This setup provides a basic CRUD API for managing Clients and Projects in a Django application using MySQL.

---------------------------------------------------------------------------------
You can now test your API endpoints using Postman or any other API client:

$ Client Endpoints:
GET /api/clients/: List all clients
POST /api/clients/create/: Create a new client
GET /api/clients/<id>/: Retrieve a specific client and its projects
PUT /api/clients/<id>/: Update a specific client
DELETE /api/clients/<id>/: Delete a specific client

$ Project Endpoints:
GET /api/projects/: List all projects
POST /api/clients/<client_id>/projects/create/: Create a new project for a client
GET /api/projects/<id>/: Retrieve a specific project
PUT /api/projects/<id>/: Update a specific project
DELETE /api/projects/<id>/: Delete a specific project
