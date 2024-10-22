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


   <h3>Console</h3>

To clone a local repository:

- Open your Terminal
- Navigate to the location where you want the local repository to be copied, using the cd command
- Use the git clone command followed by the path to the project directory
- You can also give it a name using git clone /path/to new_repo

<h4>Move to the directory where you will run the project</h4>

````
cd path/to/local/repository
````

![image](https://github.com/user-attachments/assets/8f594c24-13f9-49f6-b0e4-029622ee117a)



<h4>Clone a Remote Repository on Your Local Computer</h4>

````
git clone git/repo/path.git
````

![image](https://github.com/user-attachments/assets/e6f59b0c-80a2-435d-b9f8-e5aeb7b0ecad)


Now you can check your folder where you cloned the repository and make sure that everything was successful
![image](https://github.com/user-attachments/assets/34d57796-2bc9-4f35-af49-0c5f31467980)


Check in your compiler
![image](https://github.com/user-attachments/assets/6d6d002a-8a6d-448c-b7d3-9e82d3cd50f3)



<h2>2. Connect to a virtual environment (or create)</h2>


<h4>Run venv</h4>

````
python -m venv C:\path\to\new\virtual\environment
````

<h4>Activate Virtual Environment</h4>

Linux/macOS: 
````    
source {path_to_venv}/bin/activate
````

Windows:
````
{path_to_venv}\Scripts\activate.bat
````

<h4>Create Virtual Environment</h4>

You can view this step in the "Documentation" -> "Virtual Environment" section 

<h2>3. Install the necessary libraries from the file "requirements.txt"</h2>

<h4>In Terminale install the necessary libraries from the file "requirements.txt"</h4>

````
 pip install -r requirements.txt
````

<h2>4. Run the project in the terminal:</h2>

<h4>Run this app in terminal with --reload to update </h4>

````
uvicorn app.main:app --reload
````
![image](https://github.com/user-attachments/assets/e50796ab-8616-4e6d-ac28-c9c33378b925)

Click on http://127.0.0.1:8000 

To work with endpoints and make requests in the browser, write:

````
http://127.0.0.1:8000/docs/
````

You will see the automatic interactive API documentation
![image](https://github.com/user-attachments/assets/97768ce2-9e22-4098-ab85-93496300d5cd)

You can test endpoints here. You have to register and login and get from admin or manager the role (barman/manager/admin) to test this endpoints.


<h1>Documentation</h1>

<h4>FastAPI</h4>
URL: https://fastapi.tiangolo.com/learn/

<h4>Alembic</h4>
URL: https://alembic.sqlalchemy.org/en/latest/tutorial.html

<h4>Virtual Environment</h4>
URL: https://timeweb.cloud/tutorials/python/kak-sozdat-virtualnoe-okruzhenie

<h4>Uvicorn</h4>
URL: https://www.uvicorn.org/

