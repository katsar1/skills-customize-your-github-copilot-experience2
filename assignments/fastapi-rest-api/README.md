# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, scalable REST APIs using the FastAPI framework. You'll create a web service that handles HTTP requests, manages data, and returns JSON responses while learning about routing, request validation, and API documentation.

## 📝 Tasks

### 🛠️ Set Up FastAPI and Create Basic Endpoints

#### Description
Initialize a FastAPI application and create your first API endpoints. You'll set up the project structure, install dependencies, and implement basic GET and POST endpoints to handle requests.

#### Requirements
Completed program should:

- Import and initialize a FastAPI application
- Create at least one GET endpoint that returns data
- Create at least one POST endpoint that accepts request data
- Run the server using `uvicorn` on localhost:8000
- Include proper HTTP status codes in responses


### 🛠️ Implement Data Validation and CRUD Operations

#### Description
Expand your API with request validation using Pydantic models and implement full CRUD (Create, Read, Update, Delete) operations. Your API should validate incoming data and handle different HTTP methods appropriately.

#### Requirements
Completed program should:

- Define Pydantic models for request/response validation
- Implement GET endpoint to retrieve all items or a specific item
- Implement POST endpoint to create new items
- Implement PUT endpoint to update existing items
- Implement DELETE endpoint to remove items
- Return appropriate HTTP status codes (200, 201, 400, 404, etc.)


### 🛠️ Add Error Handling and Documentation

#### Description
Enhance your API with comprehensive error handling and automatic API documentation. Implement exception handling for edge cases and leverage FastAPI's built-in documentation features.

#### Requirements
Completed program should:

- Handle errors gracefully with appropriate HTTP error responses
- Include custom error messages for validation failures
- Access auto-generated Swagger UI documentation at `/docs`
- Access ReDoc documentation at `/redoc`
- Include docstrings in route handlers
