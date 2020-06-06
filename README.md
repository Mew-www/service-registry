[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![OpenAPI: live documentation](https://img.shields.io/badge/openapi%2Fswagger-live%20documentation-brightgreen)](http://deployed-project-url.com/swagger/)  

# Description / Features  

A minimalistic Service Registry.  

Supported features:  
- Multi-user registry
  - Capability to create a user via username/password. (Optionally disabled on server start for administrative-only use.)  
  - 1 user identity = 1 admin token  
  - _**Access to list means additionally (administrative) access to create/delete & edit user data, and vice versa**. There' no "limited scope" access tokens - these could be added at a later time e.g. in form of JWT._  
- Service registration 
  - Capability to register a single endpoint per service name (for authenticated identity).  
  - Capability to override any existing endpoint by "create_or_update" type of call (using HTTP POST/PUT verbs).  
  - _Leaves implementation details up to the user - be it a dedicated Load Balancer endpoint, or a set of endpoints using separate names via multiple registrations._  
- Service discovery
  - Capability to list services, endpoints, and metadata (of authenticated identity).  
  - Capability to get service endpoint by service name (of authenticated identity).
- OpenAPI live documentation  

# Installation notes  
Requires `python 3.6` or higher.  
