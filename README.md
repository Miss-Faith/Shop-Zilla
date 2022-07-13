# Shop-Zilla


## Contributors
* Faith Mwangi
* Martin Maina
* Williams Oditi
* lilian Muita
* Kelvin Wepo


## Description
Shop-Zilla is a web application that  helps shoppers to choose their suitable products from E-commerce sites in just one click at their conviniences.


## Setup and Installation
### Requirements
1. Clone the repository by running

        https://github.com/Miss-Faith/Shop-Zilla
    Navigate to the project

        cd Shop-Zilla
 2. Create a virtual enviroment

         pip install virtualenv 

    To activate the created virtual environment, run

        source virtual/bin/activate
3. Create database
    You will need to create a new postgress database by typing the following command to access postgress

        $ psql

    Then run below query to create a new database named 

        # create databases Shop;
5. Create Database migrations
    make migrations on postgres using django

        python3.8 manage.py makemigrations shop
    then run the below command.

        python3.8 manage.py migrate

6. Run the app
    To run the application on your development machine,

        pythong3.8 manage.py runserver
### Running Tests
To run tests;

        python3.8 manage.py test


## Technologies Used
* Python3.8
* Django
* HTML
* Bootstrap
* CSS

## User Stories
1. Allows user to login
2. Allows user to view products from different E-commerce sites
3. Allows user to filter products according to their preferences
4. Allows user to view products even if they are not logged in


## License
The project is under[MIT License](LICENSE).