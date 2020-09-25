#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from taskserver import celery_app


@celery_app.task(bind=True, name='test_add')
def add(self, x, y):
    return x + y


@celery_app.task(bind=True, name='test_mul')
def mul(self, x, y):
    return x * y


@celery_app.task(bind=True, name='xsum')
def xsum(self, numbers):
    return sum(numbers)
