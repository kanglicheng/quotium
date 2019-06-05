# quotium
*Local Development Instructions*:
Note: Need to be using python 3.7.x, it may work for 3.6.x but I have not tried it.
1) Switch to local dev branch, then clone this repo. git clone https://github.com/kanglicheng/quotium.git
2) CD to quotium, cd quotium
3) Create a python virtual environment, python3 -m virtualvenv yourvenvname
4) Install dependencies, pip install -r requirements.txt
5) Make and apply migrations, python manage.py makemigrations, python manage.py migrate
6) Start the development server, python manage.py runserver

