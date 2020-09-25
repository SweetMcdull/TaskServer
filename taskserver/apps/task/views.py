# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from taskserver.core.tasks import add

router = APIRouter()


@router.post('/create', summary='创建任务')
def create_task():
    import time
    result = add.apply_async(task_id=str(int(time.time())), args=[10, 20])
    return result.task_id
