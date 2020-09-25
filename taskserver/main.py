#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from taskserver.apps.router import api_router


def create_app() -> FastAPI:
    application = FastAPI(
        docs_url='/'
    )

    # 注册路由
    register_router(application)
    # 注册中间件
    register_middleware(application)
    return application


def register_router(application: FastAPI):
    application.include_router(api_router, prefix='/api/v1')


def register_middleware(application: FastAPI):
    # 处理跨越
    application.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],

    )


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=50002, reload=True)
