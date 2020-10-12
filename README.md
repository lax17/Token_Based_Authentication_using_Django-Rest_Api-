# Token_Based_Authentication_using_Django(Rest_Api)
Create Api for login, signup, view profile, edit profile and delete profile for user using Django Rest Framework with mysql<br>
<b> 1. Signup where user will register with these data </b>
  <ul><li>Name</li><li>Username</li><li>Email</li><li>password</li></li><li>photo</li></ul>
 <img src="https://user-images.githubusercontent.com/41922928/95692665-01f45a80-0c45-11eb-9218-f05d256907db.JPG" width="850px">
<b> 2. Api for Login where user can login with username/email </b>
 <img src="https://user-images.githubusercontent.com/41922928/95692793-12f19b80-0c46-11eb-8aa2-d989619c2caf.JPG" width="850px">
 <b>3. Api to view profile - don’t show the password. Users can only view profiles if they’re logged in. Pass the token in header with this API </b>
 <img src="https://user-images.githubusercontent.com/41922928/95692840-606e0880-0c46-11eb-931d-66d92f012713.JPG" width="850px">
 <b>4.Api to edit profile - User can  change the details other than email.(Won’t be able to change their email in edit profile). Pass the token in header with this API</b>
  <img src="https://user-images.githubusercontent.com/41922928/95692845-74b20580-0c46-11eb-9b62-0da3fae2939b.JPG" width="850px">
 <b>5.Delete profile. Pass the token in header with this API </b>
  <img src="https://user-images.githubusercontent.com/41922928/95692847-78de2300-0c46-11eb-8deb-b91578e2572d.JPG" width="850px">
  
  
 <b>Project Setup:</b>
 <ol><li><b>git clone</b>:https://github.com/lax17/Token_Based_Authentication_using_Django-Rest_Api-.git</li>
  <li>cd into the project till :Token_Based_Authentication Folder</li>
  <li>run the command : python manage.py runserver </li> //Webserver till start at default port 8000
</ol>


<b>Requirement list :</b><br>
pip install django <br>
pip install djangorestframework

Nothing more then that.

 
 
  



  
  
