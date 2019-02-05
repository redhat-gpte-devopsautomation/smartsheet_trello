# Smartsheet and Trello integration

This is a simple script to copy content from Smartsheet to Trello. 
It uses Smartsheet and Trello APIs. 

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
