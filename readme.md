## to create new app type py manage.py startapp (app__name)

## to create table in database we need to run two commands
  ```python
  py manage.py makemigrations
  py manage.py migrate 
  ``` 
  note every time we perform changes in our models fields than we have run this two commands

## after creating a model we have register that model in admin.py to make that visible in admin pannel
   # in admin.py add  admin.site.register(model_name)  -> modal_name is that model which you want to make visible in admin pannel (make sure you have created superuser for accessing admin pannel 😆)  