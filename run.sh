#! /bin/bash

#Command to generate the key and certificate files
#openssl req -x509 -newkey rsa:4096 -keyout files/key.pem -out files/cert.pem -sha256 -days 365 -nodes -subj '/CN=localhost'

#Command to run python script
python3 script.py