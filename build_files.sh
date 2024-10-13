#!/bin/bash

pip install -r requirements.txt
python3.9 manage.py migrate
python3.9 manage.py collectstatic # --noinput

chmod +x build_files.sh

# Set permissions (Optional)
chmod 666 /vercel/path0/db.sqlite3