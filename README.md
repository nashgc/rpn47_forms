# Формы v0.1
Джанго формы для РПН47

## Установка

Создайте новое виртуальное окружение после чего активируйте его и выполните следующие команды

За подробностями деплоя -- > https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04


```bash
git clone https://github.com/nashgc/rpn47_forms.git
pip install -r rpn47_forms/requirements.txt
cd rpn47_forms
python manage.py makemigrations
python manage.py mirgate
python manage.py collectstatic
python manage.py loaddata CheckTypesMenu
python manage.py loaddata DepartmentsMenu
python manage.py loaddata DistrictsMenu
python manage.py loaddata GlobalDocNumber
python manage.py loaddata PerformersMenu
python manage.py createsuperuser

```

## Запуск

```bash
python manage.py runserver
```


## Лицензия - License
Приватная лицензия, код только для внутреннего использования

It's a private license, only for internal usage