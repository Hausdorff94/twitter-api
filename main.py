# python

from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional, List
import json

# pydantic

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body

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

class UserRegistry(UserLogin, User):
    pass

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

## Users

### Register a new user
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Signup a new user",
    tags = ['Users']
)
def signup(
    user: UserRegistry = Body(...),
    ):
    """

    This path operation register a new user in the app.

    - Parameters:
        - Request body parameters:
            - user: User, UserRegistry

    - Returns a json with the user data.
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: str
    """

    with open('users.json', 'r+', encoding='utf-8') as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict['user_id'] = str(user_dict['user_id'])
        user_dict['birth_date'] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))

    return user

### Login a user
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags = ['Users']
)
def login():
    pass

### Show all users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_201_CREATED,
    summary="Show all users",
    tags = ['Users']
)
def users():
    pass

### Show a user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Show a user",
    tags = ['Users']
)
def show_a_user():
    pass

### Delete a user
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Delete a user",
    tags = ['Users']
)
def delete_a_user():
    pass

### Update a user
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Update a user",
    tags = ['Users']
)
def update_a_user():
    pass

## Tweets

### Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Signup all tweets",
    tags = ['Tweets']
    )
def home():
    return {"message": "Hello World"}

### Post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a new user",
    tags = ['Tweets']
)
def post():
    pass

### Show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags = ['Tweets']
)
def show_a_tweet():
    pass

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags = ['Tweets']
)
def delete_a_tweet():
    pass

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags = ['Tweets']
)
def update_a_tweet():
    pass



