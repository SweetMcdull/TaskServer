#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from celery import Celery

from taskserver.config import celery_config

celery_app = Celery('TaskServer',
                    backend='redis://127.0.0.1:6379/2',
                    broker='redis://127.0.0.1:6379/1')

# celery_app.autodiscover_tasks()
celery_app.conf.update(
    timezone='Asia/Shanghai'
    # enable_utc=True,
)
celery_app.config_from_object(celery_config)


@celery_app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
