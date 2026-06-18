#build_files.sh


#!/bin/bash

# Install Node dependencies and compile Tailwind
npm install
npm run builds

# Install Python dependencies and collect static files
pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear


