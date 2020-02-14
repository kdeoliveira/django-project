#Hiding Personal Info using evironment variable
import os

EMAIL_USER = os.environ.get('DB_USER')
EMAIL_PASSWORD = os.environ.get('DB_PASS')

print(EMAIL_PASSWORD)
