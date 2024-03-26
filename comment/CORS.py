from fastapi.middleware.cors import CORSMiddleware

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],  # 允许访问的来源
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # 允许的 HTTP 方法
    allow_headers=["*"],  # 允许的请求头
)

https://webap0.ncue.edu.tw/deanv2/other/ob010/GetJson_D110BN3A?year=112&smester=2&CLS_BRANCH=D