# Smartsheet and Trello integration

This is a simple script to copy content from Smartsheet to Trello. 
It uses Smartsheet and Trello APIs. 

To get Smartsheet API token:

* Click on your avatar in the top-right corner
* Click on "Personal Settings"
* In the new window click on "API Access"
* This might require upgrading your account. Click on "Upgrade" and send the request. Wait for an email confirming that you've got upgraded (usually takes less than 24 hours)
* After clicking on API Access you'll receive the token. Save it locally because you won't be able to retrieve it later

To get Trello API key and API token (aka API secret):

* Log in to Trello
* Go to https://trello.com/app-key/
* Copy the Key. It will be your "Trello API key".
* On the same page, in the next paragraph click on the link named "Token". 
It will open a new page asking you to allow "Server Token" to use your account. 
Click "Allow". Copy the token from the page that appears after that.
It will be your "Trello API token".


To install this script clone this repository:

```
git clone https://github.com/redhat-gpte-devopsautomation/smartsheet_trello.git
cd smartsheet_trello
``` 

Create and activate a Python virtual environment:

```
python3 -m venv ./venv      (choose any location for the virtual environment)
source ./venv/bin/activate
```

Install prerequisites:
```
pip instal -r requirements.txt
```

To run the script you will have to get API keys and tokens from both services.

Before running this script set the following environment variables:

* `SMARTSHEET_TOKEN`
* `TRELLO_API_KEY`
* `TRELLO_API_TOKEN`

Then find the Sheet ID of the smartsheet you want to export:

`File -> Properties`

Find or create a new Trello board where you want to export the smartsheet items. Note its name.

Call the script:

`./smartsheet_util.py -s <Sheet ID> -t <Trello Board name>`

Check if the cards were successfully imported into the chosen Trello board.
