#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from .task.views import router as task_router

api_router = APIRouter()
api_router.include_router(task_router, prefix='/tasks', tags=['任务管理'])
