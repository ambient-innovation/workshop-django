#!/bin/bash
sleep 5                                           # Wait for DB to start
echo django shell commands
python ./manage.py migrate                        # Apply database migrations
python ./manage.py loaddata users                 # Apply fixtures
echo Starting django server on 0.0.0.0:8000
python ./manage.py runserver 0.0.0.0:8000         # Start development web server
