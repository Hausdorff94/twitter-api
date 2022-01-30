# python

from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional, List

# pydantic

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI
from fastapi import status

app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(
        ..., 
        alias="id",
        title="User ID",
        )
    email: EmailStr = Field(
        ..., 
        alias="email"
        )

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length = 64,
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=2,
        max_length=50,
    )
    last_name: str = Field(
        ...,
        min_length=2,
        max_length=50,
    )
    birth_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    tweet_id: UUID = Field(
        ...,
    )
    content: str = Field(
        ...,
        min_length=1,
        max_length=256,
    )
    create_at: datetime = Field(
        default=datetime.now(),
    )
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

# Path operations

@app.get(
    path="/"
    )
def home():
    return {"message": "Hello World"}

## Users

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Signup a new user",
    tags = ['Users']
)
def signup():
    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags = ['Users']
)
def login():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_201_CREATED,
    summary="Show all users",
    tags = ['Users']
)
def users():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Show a user",
    tags = ['Users']
)
def show_a_user():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Delete a user",
    tags = ['Users']
)
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Update a user",
    tags = ['Users']
)
def update_a_user():
    pass



