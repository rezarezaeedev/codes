from fastapi import FastAPI,Query,Path ,status, HTTPException
from pydantic import *
from typing import *


"""
document of http response status code:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
"""

app=FastAPI(
        title='My test project',
        description='I learning FastAPI and practice in this file',
        version='v1.0'
    )

numbers={
	    0:"Zero",
            1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine",
            }

@app.get("/")
def root():
    return {
            "Data":"This is just a test json",
            'numbers':numbers,
            }


@app.get("/digit")
def digit(n:Optional[int]=Query(None,ge=0,le=9,alias='number',title='rezaTitle',description='rezaDesc',version='v1.4')):
    if n != None:
        return {n:numbers[n]}
    return numbers
 

 
@app.get("/number")
def get_numbers():
	return numbers


 
@app.get("/number/{num}")
def get_number(num:int=Path(0,ge=0,le=9,title='rezaTitle',description='rezaDesc')):
	return numbers[num]


# Person
class Person(BaseModel):
    name:str
    age:int
    height:Optional[int]=0

@app.post('/person',status_code=200)
def get_person(p:Person):
    res= f'{p.name} old are {p.age}'
    res+=f'-and is {p.height} centi-meters tall.' if p.height>0 else "."
    return res
#--End


# User
class User(BaseModel):
    username:str
    email:EmailStr
    password:str
    phone:Optional[str]


    class Out(BaseModel):
        username:str
        email:EmailStr
        phone:Optional[str]
        

@app.post('/user',response_model=User , status_code=status.HTTP_201_CREATED)
def get_person(u:User):
    if u.username=='admin':
        raise HTTPException(
                status_code=403,
                detail="You can't enter `admin` for username",
                headers={
                    'permission-level':'Normal user',
                    'username-entered':u.username,  
                    }
            )
    data_dict=u.dict()
    return {
            'message':"User created successfuly",
            's':data_dict
            
        }












    
    


