[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![OpenAPI: live documentation](https://img.shields.io/badge/openapi%2Fswagger-live%20documentation-brightgreen)](http://deployed-project-url.com/swagger/)  

# Description / Features  

A minimalistic Service Registry.  

Supported features:  
- Multi-user registry
  - Capability to create a user via username/password. (Optionally disabled on server start for administrative-only use.)  
  - _1 user identity = 1 (resettable) admin token. There' no "limited scope" access tokens - these could be added at a later time e.g. in form of JWT._  
- Service registration 
  - Capability to register new endpoint (for authenticated user).  
  - Capability to override existing endpoint (for authenticated user).
  - Capability to delete existing endpoint (for authenticated user).  
  - _Leaves implementation details up to the user - be it a dedicated Load Balancer endpoint, or a set of endpoints using separate names via multiple registrations._  
- Service discovery
  - Capability to list services, endpoints, and metadata (for authenticated user).  
  - Capability to get service endpoint by id (for authenticated user).  
  - Capability to get service endpoint by name (for authenticated user).  
- OpenAPI live documentation  

# Installation notes  
Requires `python 3.6` or higher.  
