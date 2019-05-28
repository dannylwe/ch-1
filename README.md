[![Build Status](https://travis-ci.org/dannylwe/ch-1.svg?branch=develop)](https://travis-ci.org/dannylwe/ch-1) [![Coverage Status](https://coveralls.io/repos/github/dannylwe/ch-1/badge.svg?branch=develop)](https://coveralls.io/github/dannylwe/ch-1?branch=develop)

# Project

sendIT

This is sendIT. The API implemtation for challenge 3.   

The endpoint you can use are shown below:

# Enpoints

|Request|Route|Desscription|
|-------|-----|------------|
|GET    |/|sanity check|
|POST   |/parcels|post a single parcel|
|GET    |/parcels/{parcel_id}|get parcel by id|
|PUT    |/parcels/{parcel_id}/cancel| cancel a single parcel delivery by Id|
|POST   |/auth/user| Register a user to sendIT|
|GET    |/token/refresh | Refresh access token after expiry|
|PUT    |/parcels/{parcel_id}/status| Admin can change status of parcel|
|PUT    |/parcels/{parcel_id}/destination| User can change destination of parcel|

To use clone repo:
```
https://github.com/dannylwe/ch-1
```

After cloning the repo, change directory to the "develop branch"

Run:

```
pip install -r requirements.txt
```

Afetr installing requirements, install postgres on your system and create two tables,  
admin and testing.

After installation setup; to to run the application:

```
python run.py
```

Note:The application uses python 3.5.2. Have python3 installed on your system to avoid inconviences.

OR you can visit the link below to try it out.
Hosted on: https://challenge3andela.herokuapp.com/api/v1

#Postman Collection
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/dfc9a865af0f47919ca2)

# Author

Daniel Lwetabe

