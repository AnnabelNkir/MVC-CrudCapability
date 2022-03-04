## Employee_register

A web application that utilizes Crud capabilities. It enables one to create entries on data on employees, update it, view and also delete entries.

#### By Annabel Micheni
#### **{February 3, 2022}**

## Requirements

This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found here;

## Setup/Installation Requirements
To view the app, ensure you have the required modules installed. Here is a run through of how to set up the application:

```
Step 1 : Clone this repository using git clone https://github.com/AnnabelNkir/MVC-CrudCapability.git or downloading a ZIP file of the code.

Step 2 : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened.

Step 3 : Open the terminal, go to the project directory and run the following commands: 

+ pip install virtualenv then
+ virtualenv venv
+ source venv/bin/activate

Step 4 : Download the all dependencies in the requirements.txt using pip install -r requirements.txt.

Step 5 : Setup Database
SetUp your database User,Password, Host then make migrate

`python manage.py makemigrations`
   then
`python manage.py migrate`

Step 6 : You can now launch the application locally by running the command python manage.py runserver and copying the link given on the terminal on your browser.

Step 7 : Run the command python manage.py createsuperuser to create an admin account in order to post. Access to the admin panel is by adding the path /admin to the address bar.

Step 8 : To test the application run

`python manage.py test`

Step 9 :  Open the application on your browser 127.0.0.1:8000. 
```
## User stories

The user is expected to navigate seamlessly through the application.

+ C- Create entries on employee data.
+ R- Read/ view the created data entries.
+ U- Update data entries of employees.
+ D- Delete data entries of employees.

## Technologies
.Django
.Git
.HTML5 & CSS
.Bootstrap
.Python 3.8
.Heroku

## Live Link

### <a href="https://crudapp254.herokuapp.com/">CRUD application live link</a>

## Known Bugs

There are no unresolved bugs in this code.

## Support and contact details

Incase of any query/queries, need for collaboration or issues with this code, feel free to reach me at nkiroteannabel@gmail.com.

### MIT License
```
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE...

```
Copyright (c) [2022] Annabel Micheni
