# Running Shoe Tracker

Application to track running shoe distance run and send custom alerts for each shoe when a specified threshold distance is exceeded with new shoe suggestions.

Current status: Redesigning frontend forms.

## Requirements

- Python 3.7+
- Node.js (install using `sudo apt install nodejs`)

## Installation and Usage

1. Clone `flask-vue-shoe-tracker` repo
2. Initialise the backend:
```
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
```
3. Initialise the frontend
```
cd frontend/frontend
npm run serve
```
4. Open https://localhost/8080/shoes to start shoe tracker application.

## Example Usage

Current state of the app (work in progress):
![image](https://user-images.githubusercontent.com/74383191/163687388-476c20b3-d527-4634-852f-3c71d98e2bae.png)

### Adding a new shoe

Example 1: Add a new pair of Ghost 13s to the application and set the initial distance run to 12km:

![image](https://user-images.githubusercontent.com/74383191/163687455-134ecb96-ca5f-421e-99c0-87df902342b1.png)

![image](https://user-images.githubusercontent.com/74383191/163687465-c630b709-b986-4afa-8aaa-9d7f9e4acee2.png)


### Updating existing shoes

Example 2: Add a new note to the first pair of shoes "Best for tempo runs and intervals":

![image](https://user-images.githubusercontent.com/74383191/163687486-8a6b1254-e3e5-4c80-a3ec-908a39309a7d.png)

![image](https://user-images.githubusercontent.com/74383191/163687490-df4a4330-ce8d-4005-9eeb-507316486bb8.png)


### Receiving distance alerts
Work in progress

## Tests
At present time, tests have only been written for the backend API for the shoe and brand endpoints. These can be found in the `backend/tests` directory. 

To run the tests:
```
cd backend
pytest
```

## Dependencies
1. VueJS - [VueJS website](https://vuejs.org/)
2. Flask - [Flask website](https://flask.palletsprojects.com/en/2.1.x/)

## TODO:

### Frontend
- Design overhaul
- Complete form submission process

### Backend
- Finish unit tests for POST/PUT methods on shoes endpoint.
