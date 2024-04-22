# Rotate your Django Keys with Django-Cryptography

Builds off of the amazing work done by: https://github.com/georgemarshall/django-cryptography

There currently isn't a way to rotate your keys safely, so I hacked the package a bit to allow us to do that. This is far from a good solution and once I have more time on my hands I will work with the original creators to get something better merged in.

Management command is under `books/management/commands/re_encrypt_data.py`
The project folder is under `reencrypt/reencrypt/encrypt_fields`
Those are the only two things you need to start. Read the instructions below.

## 1. Copy the folder into your project

copy the `reencrypt/reencrypt/encrypt_fields` folder and add it to your project
All fields that need to be encrypted need to extend from this folder now instead of the package

i.e. in my book model I have:
`from reencrypt.encrypt_fields.fields import encrypt`
instead of
`from django_cryptography.fields import encrypt`

## 2. Run migrations

Make sure your fields are updated to use the custom `encrypt` field in your database

## 3. Copy the management command into your project

Copy the management command from `reencrypt/books/management/commands/re_encrypt_data.py` into your project

## 4. Add the new settings param

Add the settings param: `ROTATED_KEY` and copy your original key (The key that will be rotated out) into that field.
Generate a new secret key. You can use this: `python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
copy that new secret key into your original `SECRET_KEY`.

you should now have your old key in the `ROTATED_KEY` and your new key in the `SECRET_KEY`

## 5. Run the management command

Run the management command and your data will now be re-encrypted with your new key.

## 6. Check your data to make sure it is readable with the new key

Make sure your data is readable before discarding your old secret key
After you validate it you can safely remove the `ROTATED_KEY` value and your data will now use the new key.
