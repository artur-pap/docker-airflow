import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

user = PasswordUser(models.User())

#user.username = '${AW_USER_NAME}'
#user.email = '${AW_USER_EMAIL}'
#user.password = '${AW_USER_PASSWORD}'

session = settings.Session()

user.username = 'admin'
user.email = 'admin@example.com'
user.password = 'iiiSANA75&&'

session.add(user)
session.commit()

session.close()

