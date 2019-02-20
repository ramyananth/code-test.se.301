## Code Test for General Software Engineers

This is a code test for general Software Engineers at Quantworks. Consider this an assessment rather than a graded exam. This test helps us gauge a candidate's level of familiarity and comfort with technologies and techniques.

### Project Description
Create a very simple data visualization web application.

#### Solution Requirements
Core Requirements:
- The web app must:
  - be built with any popular web application framework
  - have a bar chart which presents data retrieved from the API
  - have a data entry form which submits data to the API
- The API server must:
  - use an interpreted language such as Python, Node, etc.
  - have an endpoint to receive requests with data submitted as JSON and record it in the database
  - have an endpoint to receive requests to retrieve data from the database and return it as JSON
- The database must:
  - be a SQL database (we prefer PostgreSQL)
  - be pre-seeded with data

Optional Requirements:
- the web app, API, and database should each be containerized
- at least the API server should have unit tests with >= 90% code coverage
- testing, building, and running should be automated via makefile, shell script, etc.

Nice-to-have Requirements:
- user accounts with secure password storage
- endpoint authorization with JWT
- machine readable logging for each service
- very basic health endpoints for each service