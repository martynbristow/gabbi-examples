# HTTP Server

The tutorial includes a minimal HTTP Server written in Python, it uses only the Python Standard Library to impliment, and is designed to basic. This is so readers can run the server on their local machine without needing to install any dependancies.

Contributors are free to extend this server, however please:
  * Write, update and validate unittests (test_server.py)
  * Write, update and validate component tests (test_server.py)
  * Only use the Python Standard Library

## Run Server

The built-in demo server is preconfigured, all settings are in settings.ini

Launch

From the base directory `gabbi-examples` simply run:
`python server.py`

## URLs

  * /
  * /api
  * /api/time - Get a JSON representation of the current time
  * /page - List all pages, done by os.listdir('')
  * /page/<name> - Read a specific page
  * /image/<image>.png - Show an image
  * /pdf/<document>.pdf - Download a PDF Document
  * /login - Test user authentication, create a user session
  * /logout - Logout the current user, destroy the session
  * /shutdown - Shutdown the server

Errors:
The following HTTP errors have associated HTTP Pages

  * 401
  * 403
  * 404

## Templating

The server uses a basic templating, based upon the format statement.

## ToDo's

  1. Error pages
  2. Format
  3. API Response
  4. Login
  5. Logout
  6. Shutdown