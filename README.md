# django-portfolio

1. Clone the repository

git clone https://github.com/vengadalagarsamy/django-portfolio.git

2. Enter the project folder

cd django-portfolio/

3. Install django onto your machine using ‘pip’ or ‘pip3’

pip3 install django

3. Make migrations and collect necessary static files for the site

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collect static

4. Create a superuser for admin control. Admin portal can be accessed via “localhost:8000/admin”

python3 manage.py createsuperuser

5. Run the server

python3 manage.py runserver
