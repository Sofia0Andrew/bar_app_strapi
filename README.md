<h1>WEB API BAR APP</h1>

<h1>Description</h1>

   This application is designed to conveniently search for the necessary data about bars and drinks for bar employees by accessing the database through API requests.

   The application structure contains the main "app.py" folder, which implements the connection to the database I created, describes the database model and its structure. Also in this folder is the "routes" folder, which implements the endpoints that are used for the GET, POST, PUT, DELETE and etc methods for each entity. The application provides registration and authorization of users. In the "crud.py" file contains functions that interact with the database. The file is responsible for initializing and launching your application "main.py".  

Alembic allows you to create migration files that describe changes to the database schema. It allows you to automate the database creation process, supports database schema versioning, which allows you to easily track and manage changes.


<h1>Run app</h1>

<h2>1. Clone this repository to your local repository</h2>

   
  <h3>PyCharm</h3> 

   
   - Click on the field "Get from VCS"
![image](https://github.com/user-attachments/assets/2b954e0d-ccac-4572-aaeb-455170af4428)


   - Copy and paste the URL of the repository
![image](https://github.com/user-attachments/assets/34a793d7-a7f3-4b88-9d01-31bc4ecf1a33)


   - The URL: https://github.com/Sofia0Andrew/bar_app_strapi.git

<h2>2. Connect to a virtual environment (or create)</h2>


    - python -m venv C:\path\to\new\virtual\environment
      
     |Linux/macOS:  source {path_to_venv}/bin/activate
   
     |Windows:      {path_to_venv}\Scripts\activate.bat


<h2>3. Install the necessary libraries from the file "requirements.txt"</h2>


   - pip install -r requirements.txt


<h2>4. Run the project in the terminal:</h2>

   
   - ivucorn app.main:app --reload
![image](https://github.com/user-attachments/assets/e50796ab-8616-4e6d-ac28-c9c33378b925)

Click on  http://127.0.0.1:8000 

To work with endpoints and make requests in the browser, write http://127.0.0.1:8000/docs/
You will see the automatic interactive API documentation
![image](https://github.com/user-attachments/assets/97768ce2-9e22-4098-ab85-93496300d5cd)

You can test endpoints here. You have to register and login and get from admin or manager the role (barman/manager/admin) to test this endpoints.
