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
![image](https://user-images.githubusercontent.com/74383191/163677045-bd95103b-74df-4991-8a55-d8814453e1bb.png)

### Adding a new shoe

### Updating existing shoes

### Receiving distance alerts

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
