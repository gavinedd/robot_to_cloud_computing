from pathlib import Path

import sys
import multiprocessing
import os


APP_BASE_DIR = Path(__file__).resolve().parent
sys.path.append(APP_BASE_DIR)

command = 'gunicorn -c ' + str(APP_BASE_DIR) + 'gunicorn_config.conf robot.wsgi'

bind = '127.0.0.1:8000'
backlog = 2048

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
timeout = 60

loglevel = 'info'
capture_output = True

LOGS_DIR = os.path.join(APP_BASE_DIR, 'logs')

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

accesslog = os.path.join(LOGS_DIR, 'gunicorn_access.log')
errorlog = os.path.join(LOGS_DIR, 'gunicorn_error.log')
