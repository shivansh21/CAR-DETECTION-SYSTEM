# CAR-DETECTION-SYSTEM

<h4>*** INTRODUCTION ***</h4>

CAR DETECTION SYSTEM IS AN CLOUD BASED APPLICATION USES COMPUTER VISION WHICH HAS THE POWER OF RECOGNISING THE IMAGE LABELS, WEB-ENTITIES AND VARIOUS OTHER PROPERTIES ALSO 
WHICH INCLUDES IN IT. WE HAVE USED GOOGLE VISION API'S AND SOME OTHER FRAMEWORKS TO MAKE ITSELF TRAINED FOR ANY IMAGE. 

Google Cloud Vision API enables developers to understand the content of an image by encapsulating powerful machine learning models in an easy to use REST API.
It quickly classifies images into thousands of categories (e.g., "sailboat", "lion", "Eiffel Tower"), detects individual objects and faces within images, and
finds and reads printed words contained within images. Analyze images "uploaded in the request or integrate with your image STORAGE on Google Cloud Storage".

<h4>*** HOW IT WORKS ***</h4>

<h5>A.)</h5> INTRO AND CREATING A VIRTUAL MACHINE ON GOOGLE CLOUD PLATFORM:<hr>
  a.) Create account on google cloud platform.<hr>
  b.) Open Console Window.<hr>
  c.) Create project of your desired name.<hr>
  d.) Open communte engine, click on VM instances and then fill the details in it.<hr>
  e.) Take shared GPU for this project (less cost) and set memory to 0.67 GB<hr>
  f.) Choose your own OS for VM (we chose UBUNTU 16.04)<hr>
  g.) Set service account to No service account.<hr>
  h.) Now we have to provide it a SSH Key which can be traced out from third party software 'PuTTY' <hr>
(Download link: https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.70-installer.msi) 
  <hr>
  i.) Generate 'SSH key' from Putty which can generate random key,add your username at last of the link to enable it.<hr>
  j.) Put that key in SSH Key column of VM instances.<hr>
  k.) Set private key if you want (I did set empty one) and create it.<hr>
  l.) It'll take several minutes to setup your instance. Till that time GOTO-->PuTTY Configuration--> SSH--> auth -->'Browse ppk file from your local disc'<hr>
(private key)--> Session--->put external IP address in Host Name(copy from instance) --->click Yes and enter in server console.<hr>
 
<h5>B.)</h5> COMMANDS TO BE ENTERED IN SERVER CONSOLE:<hr>
  a.) login: enter <username> (replace special symbols with undercores) hit enter and boom you are inside the virtual machine.<hr>
  b.) sudo apt-get install htop (this interface is passwordless sudo)<hr>
  c.) sudo su<hr>
  d.) cd ~ (root dir)<hr>
  e.) mkdir gcloudstuff<hr>
  f.) cd gcloudstuff<hr>
  h.) sudo apt-get install python-pip<hr>
  i.) sudo pip install google-cloud<hr>
  J.) GOTO: google cloud platform again and open api manager--> credentials --> create credentials--> new service account -->choose name for service account and give full ownership --> create , then it will automatically download one json file ---> copy the code in it.<hr>
  k.) pip install --upgrade pip<hr>
  l.) make json file: nano apikey.json --> open it and paste that code in this json file and save it (ctrl + X and 'Yes' then enter)<hr>
  m.) export GOOGLE_APPLICATION_CREDENTIALS=~/gcloudstuff/apikey.json , copy this path.<hr>
  n.) paste this on : nano ~/.profile , save it<hr>
  o.) source ~/.bashrc<hr>
  p.) mkdir visionex --> cd visionex<hr><hr>
  q.) nano vision.py and hit enter , now it will open an python ide.<hr>
