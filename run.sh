#!/bin/sh
# high throughput recommended run
gunicorn -w 4 -k uvicorn.workers.UvicornWorker --log-level debug app:app
