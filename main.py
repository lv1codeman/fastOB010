from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from aiohttp import ClientSession
import asyncio
import aiohttp
import time

app = FastAPI()

# 静态文件目录，用于存放 index.html
app.mount("/static", StaticFiles(directory="static"), name="static")


# 主页路由，返回 index.html
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", "r") as file:
        html_content = file.read()
    return html_content


# 处理 POST 请求
@app.post("/fetch-data/")
async def go_fetch_data():
    start = time.time()
    res = await fetch_data()
    end = time.time()
    print("exe time=", round(end - start, 2))
    return res


# @app.post("/fetch-data/")
async def fetch_data():
    year = "112"
    semester = "2"

    data = {
        "sel_cls_branch": "D",
        "sel_scr_english": "",
        "sel_SCR_IS_DIS_LEARN": "",
        "sel_yms_year": year,
        "sel_yms_smester": semester,
        "scr_selcode": "",
        "sel_cls_id": "",
        "sel_sct_week": "",
        "sub_name": "",
        "emp_name": "",
        "X-Requested-With": "XMLHttpRequest",
    }

    url = "https://webap0.ncue.edu.tw/DEANV2/Other/OB010"
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as response:
            html_data = response.text()

            return await response.text()
