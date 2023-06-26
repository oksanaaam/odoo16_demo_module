# Project "Demo Module"
This project is a module for Odoo 16. It includes the object demo.demo with a single field name of type char. Additionally, the module adds separate menus, tree views, and form views.

## Features
Object creation, menu integration, tree view, form view in Odoo 16.
Stores information in a PostgreSQL database.
Vowel and consonant Replacement in replace_characters.py.
Possibility to return a new sequence of dimensions, sorted ascending by area in sorted_sequence_of_shapes.py.


### Installation and Setup

1. Clone the repo
`git clone https://github.com/oksanaaam/odoo16_demo_module.git`
2. Open the project folder in your IDE
3. Open a terminal in the project folder
4. If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
cd odoo
pip install -r requirements.txt
```


### Installation PostgreSQL and create database.

Set the required environment variables in odoo.conf file:

```
db_host=<your db hostname>
db_port=<your port>
db_user=<your user name>
db_password=<your password>

addons_path = path to addons, path to addons custom_addons

```

## Usage

Cd to folder odoo and start the server:

`python odoo-bin`

For running replace_characters:

`python replace_characters.py`

For running sorted_sequence_of_shapes:

`python sorted_sequence_of_shapes.py`
