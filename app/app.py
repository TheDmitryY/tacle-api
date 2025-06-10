from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from typing import Union
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



app = FastAPI()

ALLOWED_IP = ["192.168.0.110", "192.168.0.100"]


@app.middleware("http")
async def check_ip(request: Request, call_next):
        client_ip = request.client.host
        logger.info(f"[INFO] - Запит від IP: {client_ip}")
        
        if client_ip not in ALLOWED_IP:
            error_detail = 'Access decline!'
            logger.warning(error_detail)
        
            raise HTTPException(
                status_code=403,
                detail=error_detail,
                
            )
        responce = await call_next(request)
        return responce

@app.get("/")
def welcome():
    return "Hello Admin"


@app.get("/shutdown")
def shutdown():
    try:
        if os.name == "nt":
            os.system("shutdown /s /t 0")
        else:
            os.system("shutdown -h now")
    except Exception as e:
        print("[ERROR] - Command error")

@app.get("/sleepmode")
def sleep():
    try:
        if os.name == "nt":
            os.system("shutdown /h /t 3")
        else:
            os.system("systemctl suspend")
    except Exception as e:
        print("[ERROR] - Command error")
    return os.system("")

@app.get("/reboot")
def reboot():
    try:
        if os.name == "nt":
            os.system("shutdown /r /t ")
        else:
            os.system("shutdown -r now")
    except Exception as e:
        print("[ERROR] - Command error")

@app.get("/command/{command}")
def command_handler(command: str):
    command_exec = os.system(f"{command}")
    return {"command: ": command_exec}