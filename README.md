**Following Steps are needed to Setting up Google Drive API**
Go ahead and log in to your GCP console using your gmail ID.
After logging in, create a new Project. Let’s name it FileBackup.
Now, you will need to configure and download the client configuration secrets JSON file. So, head over to APIs and Services ⮕ Select OAuth consent screen.
Select User Type as External and click Create.
Fill in the necessary App Information and click on Save and Continue.
No need to fill in Scopes for now and proceed to the next step by clicking on Save and Continue.
Add a Test User. Simply enter your email ID here, or you may choose to add another user. However, to keep things simple, I entered my email ID.
Click on Credentials ⮕ CREATE CREDENTIALS ⮕ Select OAuth client ID.
Select Enabled APIs and services ⮕ click ENABLE APIS AND SERVICES ⮕ Search Google Drive ⮕ Select the Google Drive API ⮕ Click on Enable
**Automate the Script through the window task Sheduler** 
 Success/Failure  Report will be generated in the Report.txt formate in the local directory where the script is stored
