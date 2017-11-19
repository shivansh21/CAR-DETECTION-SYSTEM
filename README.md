# CAR-DETECTION-SYSTEM
<h4><b>API KEY: AIzaSyBhJyveyg-O_2Yj_rEMq7IGKdSP855OcMk </b></h4>
<h4>*** INTRODUCTION ***</h4>

CAR DETECTION SYSTEM IS AN CLOUD BASED APPLICATION USES COMPUTER VISION WHICH HAS THE POWER OF RECOGNISING THE IMAGE LABELS, WEB-ENTITIES AND VARIOUS OTHER PROPERTIES ALSO 
WHICH INCLUDES IN IT. WE HAVE USED GOOGLE VISION API'S AND SOME OTHER FRAMEWORKS TO MAKE ITSELF TRAINED FOR ANY IMAGE. 

Google Cloud Vision API enables developers to understand the content of an image by encapsulating powerful machine learning models in an easy to use REST API.
It quickly classifies images into thousands of categories (e.g., "sailboat", "lion", "Eiffel Tower"), detects individual objects and faces within images, and
finds and reads printed words contained within images. Analyze images "uploaded in the request or integrate with your image STORAGE on Google Cloud Storage".

<h4>*** HOW IT WORKS ***</h4>

<h5>A.)</h5> INTRO AND CREATING A VIRTUAL MACHINE ON GOOGLE CLOUD PLATFORM:<br>
  a.) Create account on google cloud platform.<br>
  b.) Open Console Window.<br>
  c.) Create project of your desired name.<br>
  d.) Open communte engine, click on VM instances and then fill the details in it.<br>
  e.) Take shared GPU for this project (less cost) and set memory to 0.67 GB<br>
  f.) Choose your own OS for VM (we chose UBUNTU 16.04)<br>
  g.) Set service account to No service account.<br>
  h.) Now we have to provide it a SSH Key which can be traced out from third party software 'PuTTY' <br>
(Download link: https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.70-installer.msi) 
  <br>
  i.) Generate 'SSH key' from Putty which can generate random key,add your username at last of the link to enable it.<br>
  j.) Put that key in SSH Key column of VM instances.<br>
  k.) Set private key if you want (I did set empty one) and create it.<br>
  l.) It'll take several minutes to setup your instance. Till that time GOTO-->PuTTY Configuration--> SSH--> auth -->'Browse ppk file from your local disc'<br>
(private key)--> Session--->put external IP address in Host Name(copy from instance) --->click Yes and enter in server console.<br>
 
<h5>B.)</h5> COMMANDS TO BE ENTERED IN SERVER CONSOLE:<br>
  a.) login: enter <username> (replace special symbols with undercores) hit enter and boom you are inside the virtual machine.<br>
  b.) sudo apt-get install htop (this interface is passwordless sudo)<br>
  c.) sudo su<br>
  d.) cd ~ (root dir)<br>
  e.) mkdir gcloudstuff<br>
  f.) cd gcloudstuff<br>
  h.) sudo apt-get install python-pip<br>
  i.) sudo pip install google-cloud<br>
  J.) GOTO: google cloud platform again and open api manager--> credentials --> create credentials--> new service account -->choose name for service account and give full ownership --> create , then it will automatically download one json file ---> copy the code in it.<br>
  k.) pip install --upgrade pip<br>
  l.) make json file: nano apikey.json --> open it and paste that code in this json file and save it (ctrl + X and 'Yes' then enter)<br>
  m.) export GOOGLE_APPLICATION_CREDENTIALS=~/gcloudstuff/apikey.json , copy this path.<br>
  n.) paste this on : nano ~/.profile , save it<br>
  o.) source ~/.bashrc<br>
  p.) mkdir visionex --> cd visionex<br>
  q.) nano vision.py and hit enter , now it will open an python ide.<br>
