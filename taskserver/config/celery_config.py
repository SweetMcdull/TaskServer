#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

broker_url = 'redis://127.0.0.1:6379/1'
result_backend = 'redis://127.0.0.1:6379/2'

imports = ['taskserver.core.tasks']
worker_concurrency = os.cpu_count()  # worker并发数，默认cpu核数

# 日志配置
worker_redirect_stdouts_level = 'ERROR'
worker_task_log_format = (
    "[%(asctime)s: %(levelname)s/%(processName)s]"
    "[%(task_name)s(%(task_id)s)] %(message)s"
)
worker_log_format = "[%(asctime)s: %(levelname)s/%(processName)s] %(message)s"

task_send_sent_event = True
worker_send_task_events = True

# worker_max_tasks_per_child = 10
# worker_max_memory_per_child = 12 * 1024  # 12M

# task_annotations = {
#     '*': {'rate_limit': '10/m'},
#     'tasks.add': {'rate_limit': '20/m'}
# }
# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']
# enable_utc = True
