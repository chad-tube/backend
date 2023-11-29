#!/bin/bash

# Run the application
cd downloader/ && gunicorn -b 0.0.0.0:8000 core.wsgi
