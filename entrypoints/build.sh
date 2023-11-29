#!/bin/bash
# exit on error
set -o errexit

python3  downloader/manage.py collectstatic --no-input
python3 downloader/manage.py migrate