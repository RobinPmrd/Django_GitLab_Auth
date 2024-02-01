# Django_GitLab_Auth

## Installation
Create virtual environnement : `python -m venv venv`  
Start it : `source venv/bin/activate`  
Install requirements : `pip install -r 'requirements.txt'`

Create environnement file *.env* in */gitlabAuth/gitlabAuth* and provide GitLab informations :  
- GITLAB_CLIENT_ID=\<client_id>
- GITLAB_SECRET=\<secret>
- GITLAB_URL=\<url>

Run the app :
```bash
cd gitlabAuth
python manage.py runserver 8080
```