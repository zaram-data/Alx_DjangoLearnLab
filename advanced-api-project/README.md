## API Endpoints (advanced-api-project)

- GET  /api/books/                -> List all books (public)
- GET  /api/books/?year=YYYY     -> Filter books by publication_year
- POST /api/books/create/        -> Create a book (authenticated)
- GET  /api/books/<pk>/          -> Retrieve a single book (public)
- PUT/PATCH /api/books/<pk>/update/ -> Update a book (authenticated)
- DELETE /api/books/<pk>/delete/ -> Delete a book (authenticated)

Authentication:
- Create/Update/Delete require authentication (DRF Session/Basic by default).
