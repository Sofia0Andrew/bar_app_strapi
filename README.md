1. Clone this repository to your local repository.
   -

   - Click on the field "Get from VCS"
![image](https://github.com/user-attachments/assets/2b954e0d-ccac-4572-aaeb-455170af4428)


   - Copy and paste the URL of the repository
![image](https://github.com/user-attachments/assets/34a793d7-a7f3-4b88-9d01-31bc4ecf1a33)


   - The URL: https://github.com/Sofia0Andrew/bar_app_strapi.git

2. Connect to a virtual environment (or create):
   -

    - python -m venv C:\path\to\new\virtual\environment
      
     |Linux/macOS:  source {path_to_venv}/bin/activate
   
     |Windows:      {path_to_venv}\Scripts\activate.bat


3. Install the necessary libraries from the file "requirements.txt"
   -

   - pip install -r requirements.txt


4. Run the project in the terminal:
   -
   
   - ivucorn app.main:app --reload
![image](https://github.com/user-attachments/assets/e50796ab-8616-4e6d-ac28-c9c33378b925)

Click on  http://127.0.0.1:8000 

To work with endpoints and make requests in the browser, write http://127.0.0.1:8000/docs/
You will see the automatic interactive API documentation
![image](https://github.com/user-attachments/assets/97768ce2-9e22-4098-ab85-93496300d5cd)

You can test endpoints here. You have to register and login and get from admin or manager the role (barman/manager/admin) to test this endpoints.
