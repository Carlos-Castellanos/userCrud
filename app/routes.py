import json
from flask import (
    Flask,
    request
)
from datetime import datetime
from flask import render_template
import json
from app.database import user
from app.database import vehicle

VERSION = "1.0.0"

app = Flask(__name__)


@app.get("/ping")
def get_ping():
    response = {
        "status": "ok",
        "message": "pong"
    }
    return response


@app.get("/version")
def get_version():
    response = {
        "status": "ok",
        "version": VERSION,
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return response


@app.get("/users")   #ok
def get_all_users():
    user_list = user.scan()
    out = {
        "status":"ok",
        "users":user_list
    }
    return out

@app.get("/users/<int:pk>")   #ok
def get_user_by_id(pk):
    user_obj = user.select_by_id(pk)
    out = {
        "status":"ok",
        "users":user_obj
    }
    return out

@app.post("/users")    #ok
def create_user():
    raw_data = request.json
    user.insert(raw_data)
    out = {
        "status":"ok",
        "message" : "created"
    }
    return out, 201

@app.put("/users/<int:pk>")    #ok
def update_user(pk):
    raw_data = request.json
    user.update(pk, raw_data)
    return "", 204

@app.delete("/users/<int:pk>")   #ok
def deactivate_user(pk):
    user.deactivate(pk)
    return "",204


################################################################################
@app.get("/vehicles")   #ok
def get_all_vehicles():
    vehicle_list = vehicle.scan()
    out = {
        "status":"ok",
        "vehicles":vehicle_list
    }
    return out

@app.get("/vehicles/<int:pk>")   #ok
def get_vehicle_by_id(pk):
    vehicle_obj = vehicle.select_by_id(pk)
    out = {
        "status":"ok",
        "vehicles":vehicle_obj
    }
    return out

@app.post("/vehicles")    
def create_vehicle():
    raw_data = request.json
    vehicle.insert(raw_data)
    out = {
        "satuts":"ok",
        "message" : "created"
    }
    return out, 201

@app.put("/vehicles/<int:pk>")    #ok
def update_vehicle(pk):
    raw_data = request.json
    vehicle.update(pk, raw_data)
    return "", 204

@app.delete("/vehicles/<int:pk>")   #ok
def deactivate_vehicle(pk):
    vehicle.deactivate(pk)
    return "",204