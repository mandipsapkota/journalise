# journalise
This is a app to create and share journals using react and django.


## Some theory for my revision
Note: Backend is build to help people control how, what and why users can access data.
REST Api means representional state transfer.

Backend should give data in a generic json format that can be understood by programming languages.

### Request methods:
- GET 
- PUT
- OPTIONS
- HEAD 
- DELETE
- TRACE 
- POST
- CONNECT
- PATCH

### HTTP Response codes
We can indicate the frontend with these codes.

- 2xx (Success)
    - 200(Success), 201(Created) ,202(Accepted)
- 3xx (Redirections)
- 4xx (Client Error)
    - 404 (Not found)
- 5xx (Server Error)
    - 500 (Internal Server error)

### Restful API's

- Criterias
    - Must have a base URL
    - is stateless, like HTTP
    - Has HTTP methods
    - Include media types to define state transition data elements (JSON)

We can have same backend for different extended frontends.

### Stateless Protocol
It doesnt store data for previous sessions or requests.

### Endpoints

- Webpage normally contains links to resources (https://site.com/blog)
- Restful apis have endpoints
    - .../api/user/1 can return user with id 1 on get request.

- Service based on request type:
    - Like get, put ... operates differenly on same url.