# A simple Management command that goes through your apps and models and re-encrpyts your data with a rotated Django key

Builds off of the amazing work done by: https://github.com/georgemarshall/django-cryptography

I wanted to make a simple way to rotate the secret key in Django but I realized all of my encrypted fields used that secret key to encrypt the data.
So I made a simple management command that can be run to reencrypt all the data.

Check it out under books/management/commands/re_encrypt_data.py
