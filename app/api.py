"""Users service.
This module implements user authentication
"""

from typing import Optional
from fastapi import FastAPI
import fastapi
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

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

def find_user(id):
    """Find a user from the users list
    """
    for u in users:
        if u["id"] == id:
            return u

@app.get("/status/alive")
def alive():
    """Status check function to verify the service can start
    
    Returns:
        JSON-formated response.
    """
    return {"status": "User service is alive"}


@app.get("/status/healthy")
def healthy():
    """Status check function to verify the server can serve requests.

    Returns:
        JSON-formated response.
    """
    return {"status": "User service is healthy"}


@app.get("/")
def index():
    """Index
    Returns:
        JSON-formated response.
    """
    return {"message": "Hello World"}

@app.post("/users")
def create_user(user: User):
    """Create a user
    Returns:
        JSON-formated response.
    """
    user_dict = user.dict()
    user_dict['id'] = randrange(0,99999)
    users.append(user_dict)
    return {"data": user_dict}


@app.get("/users")
def get_users():
    """Get users
    Returns:
        JSON-formated response.
    """
    return {"data": users}

@app.get("/users/{id}")
def get_user(id: int):
    """Get a user
    Returns:
        JSON-formated response.
    """
    user = find_user(int(id))
    return {"data": user}


@app.put("/users/{id}")
def update_user(user: User):
    """Update a user
    Returns:
        JSON-formated response.
    """

    users.append(user.dict())
    return {"data": user} 


@app.delete("/users/{id}")
def delete_user(user: User):
    """Delete a user
    Returns:
        JSON-formated response.
    """
    print(user)
    print(user.dict())
    # return {"message": "User created"}
    return {"data": user} 
