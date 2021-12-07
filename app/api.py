"""Users service.
This module implements user authentication
"""

import os
from typing import Optional
from fastapi import FastAPI, Response, Request, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import logging
from custom_logging import CustomizeLogger
from pathlib import Path


logger = logging.getLogger(__name__)

config_path=Path("../").with_name("logging_config.json")

FASTAPI_DEBUG = logging.getLevelName(os.environ.get("FASTAPI_DEBUG", "True"))

def create_app() -> FastAPI:
    app = FastAPI(title='Users', debug=FASTAPI_DEBUG)
    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger

    return app

app = create_app()
# app = FastAPI()

class User(BaseModel):
    first_name: str 
    last_name: str
    email: str
    mobile: Optional[str] = None
    is_active: bool = True

users = [{
  "id": 1,
  "first_name": "Vallie",
  "last_name": "O'Duane",
  "email": "voduane0@tinyurl.com",
  "mobile": "471-529-0964",
  "is_active": False
}, {
  "id": 2,
  "first_name": "Ramsey",
  "last_name": "von Hagt",
  "email": "rvonhagt1@seesaa.net",
  "mobile": "968-675-3436",
  "is_active": False
}, {
  "id": 3,
  "first_name": "Hallsy",
  "last_name": "Ditts",
  "email": "hditts2@123-reg.co.uk",
  "mobile": "554-105-7843",
  "is_active": True
}, {
  "id": 4,
  "first_name": "Shandee",
  "last_name": "Torbard",
  "email": "storbard3@nba.com",
  "mobile": "966-429-9430",
  "is_active": True
}, {
  "id": 5,
  "first_name": "Keri",
  "last_name": "Calverley",
  "email": "kcalverley4@tripadvisor.com",
  "mobile": "173-126-8083",
  "is_active": False
}, {
  "id": 6,
  "first_name": "Frank",
  "last_name": "Gruby",
  "email": "fgruby5@wikimedia.org",
  "mobile": "168-424-3772",
  "is_active": False
}, {
  "id": 7,
  "first_name": "Cally",
  "last_name": "Djakovic",
  "email": "cdjakovic6@people.com.cn",
  "mobile": "252-362-9829",
  "is_active": True
}, {
  "id": 8,
  "first_name": "Olva",
  "last_name": "Romero",
  "email": "oromero7@miitbeian.gov.cn",
  "mobile": "535-256-0682",
  "is_active": True
}, {
  "id": 9,
  "first_name": "Loreen",
  "last_name": "Lamball",
  "email": "llamball8@wordpress.org",
  "mobile": "607-675-6215",
  "is_active": True
}, {
  "id": 10,
  "first_name": "Addy",
  "last_name": "Pleager",
  "email": "apleager9@senate.gov",
  "mobile": "185-539-8066",
  "is_active": False
}]

# Find a user
def find_user(id):
    """Find a user from the users list
    """
    for u in users:
        if u["id"] == id:
            return u

# Find user index
def find_index_user(id):
  for i, p in enumerate(users):
    if p['id'] == id:
      return i


@app.get("/")
def index():
    """Index
    Returns:
        JSON-formated response.
    """
    return {"message": "Users service in running"}


@app.post("/users")
def create_user(user: User, status_code=status.HTTP_201_CREATED):
    """Create a user
    Returns:
        JSON-formated response.
    """
    user_dict = user.dict()
    user_dict['id'] = randrange(0,99999)
    users.append(user_dict)
    # TODO: Add logging
    return {"data": user_dict}


@app.get("/users")
def get_users():
    """Get users
    Returns:
        JSON-formated response.
    """
    # TODO: Add Logging
    return {"data": users}

@app.get("/users/{id}")
def get_user(id: int, response: Response):
    """Get a user
    Returns:
        JSON-formated response.
    """
    user = find_user(id)
    if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                          detail="User does not exist")
      # logging.error(f'User with id {id} was not found')
      # TODO: Add Logging
    return {"data": user}


@app.put("/users/{id}")
def update_user(id: int, user: User):
    """Update a user
    Returns:
        JSON-formated response.
    """
    index = find_index_user(id)

    if index == None:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                          detail=f"User does not exist")
    
    user_dict = user.dict()
    user_dict["id"] = id
    users[index] = user_dict
    # TODO: Add Logging
    # return {"message": "User updated successfully"} 
    return {"data": user_dict}


@app.delete("/users/{id}")
def delete_user(id: int):
    """Delete a user
    Returns:
        JSON-formated response.
    """
    index = find_index_user(id)
    
    # TODO: Add Logging
    if index == None:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                          detail=f"User does not exist")
    # return {"message": "User was successfully deleted"}
    users.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT) 


@app.get("/status/alive")
def alive():
    """Status check function to verify the service can start
    
    Returns:
        JSON-formated response.
    """
    return {"status": "Users service is alive"}


@app.get("/status/healthy")
def healthy(request: Request):
    """Status check function to verify the server can serve requests.

    Returns:
        JSON-formated response.
    """
    request.app.logger.info("Health status")
    return {"status": "Users service is healthy"}

@app.get('/custom-logger')
def customize_logger(request: Request):
    """Testing customer logger with an error
    
    """
    request.app.logger.info("Here Is Your Info Log")
    a = 1 / 0
    request.app.logger.error("Here Is Your Error Log")
    return {'data': "Successfully Implemented Custom Log"}
