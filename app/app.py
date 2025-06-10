from fastapi import FastAPI, Request
import os

app = FastAPI()


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

@app.post("/sleepmode")
def sleep():
    try:
        if os.name == "nt":
            os.system("shutdown /h /t 3")
        else:
            os.system("systemctl suspend")
    except Exception as e:
        print("[ERROR] - Command error")
    return os.system("")

@app.post("/reboot")
def reboot():
    try:
        if os.name == "nt":
            os.system("shutdown /r /t ")
        else:
            os.system("shutdown -r now")
    except Exception as e:
        print("[ERROR] - Command error")
