# Assignement Solution

### set up the environment
-- pip install -r requirements.txt

use this environment

### After that change the directory run this following command
-- python app.py

### copy the perticular link and past into postman http for testing
--- Watch my video for testing puspose
### This is some sample data use this for testing

{
  "name": "mark4",
  "email": "mark4@gmail.com",
  "password": "Pass@123"
}

1. add user :  http://127.0.0.1:5000/add
   -select : POST > body > raw > Json
   -add the given data
 -NOTE : you can add multiple users one-by-one

3. show users :  http://127.0.0.1:5000/users
     -select : GET

3 . show user by id : http://127.0.0.1:5000/users/_id

4. update :  http://127.0.0.1:5000/update/_id
   - select : PUT > body > raw > Json
   -update the data which you want

5. delete : http://127.0.0.1:5000/delete/_id


# Here I have used custome id we can change it by changing the code
