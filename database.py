import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceatten-64f9c-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Vishal",
            "branch": "CSE",
            "total_attendance": 7,
            "id": 321654,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Himanshu",
            "branch": "CSE",
            "total_attendance": 7,
            "id": 852741,
           "last_attendance_time": "2022-12-11 00:54:34"
        },
    "222222":
        {
            "name": "Hrithik",
            "branch": "ECE",
            "total_attendance": 7,
            "id": 222222,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "111111":
        {
            "name": "Harshit",
            "branch": "CSE",
            "total_attendance": 7,
            "id": 111111,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)