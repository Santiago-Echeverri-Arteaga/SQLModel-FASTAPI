from fastapi import APIRouter
from botocore.exceptions import ClientError
from .db import heroes_table
from fastapi.responses import JSONResponse
from boto3.dynamodb.conditions import Key

router = APIRouter()

def create_hero(hero: dict):
    try:
        heroes_table.put_item(Item=hero)
        return hero
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)

def get_hero(id: str):
    try:
        response = heroes_table.query(
            KeyConditionExpression= Key("id").eq(id)
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)

def get_heroes():
    try:
        response = heroes_table.scan(
            Limit = 5,
            AttributesToGet=["heroname", "id"]
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)

def delete_heroe(hero: dict):
    try:
        response = heroes_table.delete_item(
            Key={"id": hero["id"]}
        )
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)

def update_heroe(hero: dict):
    try:
        response = heroes_table.update_item(
            Key={"id": hero["id"]},
             UpdateExpression = "SET heroname = :heroname, age = :age",
             ExpressionAttributeValues = {
                 ":heroname": hero["heroname"],
                 ":age": hero["age"]}
        )
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)