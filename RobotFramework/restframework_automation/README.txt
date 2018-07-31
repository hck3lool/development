# Dependencies

asn1crypto==0.24.0
backcall==0.1.0
certifi==2018.4.16
cffi==1.11.5
chardet==3.0.4
cryptography==2.2.2
decorator==4.3.0
dj-database-url==0.5.0
Django==2.0.6
django-bootstrap-form==3.4
djangorestframework==3.8.2
ecdsa==0.13
future==0.16.0
gunicorn==19.9.0
httpie==0.9.9
idna==2.7
ipython==6.4.0
ipython-genutils==0.2.0
jedi==0.12.1
jsonfield==2.0.2
parso==0.3.1
pexpect==4.6.0
pickleshare==0.7.4
pkg-resources==0.0.0
prompt-toolkit==1.0.15
psycopg2==2.7.5
psycopg2-binary==2.7.5
ptyprocess==0.6.0
pyasn1==0.4.3
pycparser==2.18
pycrypto==2.6.1
pycryptodome==3.6.4
Pygments==2.2.0
python-jose==3.0.0
pytz==2018.5
requests==2.19.1
robotframework==3.0.4
robotframework-requests==0.4.7
rsa==3.4.2
simplegeneric==0.8.1
six==1.11.0
traitlets==4.3.2
urllib3==1.23
wcwidth==0.1.7
whitenoise==3.3.1


# How to execute a text case:

robot --loglevel DEBUG:INFO --outputdir ${PWD}/results cases/requests.robot
