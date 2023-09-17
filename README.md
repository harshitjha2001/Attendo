# PUNK HAZARD CHATBOT


AttenDo is a real-time face recognition-based attendance tracking system. This system is integrated with a student database to streamline and automate attendance management processes. By utilizing the face-recognition Python library for face encoding and recognition, and seamlessly integrating it with Firebase to store student information, we've created an efficient and accurate solution for attendance tracking.

## Screenshots

- ACTIVE SCREEN
- 
![1](https://github.com/harshitjha2001/Attendo/assets/85453454/9fedde62-8909-41c1-80d1-d82da0e556c8)

- SHOWING STUDENT DATA IF FACE MATCHED FROM DATABASE

![2](https://github.com/harshitjha2001/Attendo/assets/85453454/d517d132-6b72-4e4e-9b78-0e32908c3a4d)

- CAN ONLY MARK ATTENDANCE ONCE PER DAY

![3](https://github.com/harshitjha2001/Attendo/assets/85453454/a86caad5-3409-489c-8c41-260a157d28db)





## Features

- Real-time Face Recognition: AttenDo uses cutting-edge face recognition technology to mark attendance as students enter the classroom.
- Firebase Integration: Student information is securely stored in a Firebase database, ensuring easy access and data integrity.
- User-Friendly GUI: We've designed an intuitive and visually appealing GUI using Photoshop and Figma for a seamless user experience.
- Efficiency Improvement: AttenDo significantly reduces manual effort in attendance management, making it a valuable tool for educators.

## Prerequisites

Before you begin, ensure you have met the following requirements:

1. **Python and Libraries**: You should have Python installed on your system. Additionally, make sure to install the necessary Python libraries using pip:

   ```bash
   pip install opencv-python face-recognition cvzone firebase-admin numpy
   ```

2. **Firebase Configuration**: Obtain a Firebase service account key (`serviceAccountKey.json`) and ensure you have Firebase set up with a database and storage bucket. Replace `"https://faceatten-64f9c-default-rtdb.firebaseio.com/"` and `"faceatten-64f9c.appspot.com"` in your code with your Firebase project's URLs.

3. **Background Image**: You'll need a background image named 'background.png' in the 'Resources' directory. This image is used as a background for the camera feed.

4. **Face Encoding Data**: Make sure you have the encoding data for known faces in a file named 'EncodeFile.p'. This file should contain encoded face data and associated student IDs.

5. **Mode Images**: Prepare mode images for your GUI in the 'Resources/Modes' directory.

6. **Firebase Storage**: Ensure you have a storage bucket in Firebase configured to store student images in the 'Images' folder.

7. **Firebase Realtime Database**: Set up a Firebase Realtime Database to store student information and attendance records.

8. **Camera**: Make sure you have a working camera connected to your system (usually accessible via index 1 as set in your code).

##

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/harshitjha2001/gridtemp](https://github.com/harshitjha2001/Attendo
   cd Attendo
2. Configure the Firebase service account key and URLs in your code.
3. Ensure you have the required background image, face encoding data, mode images, and Firebase storage/database set up.
4. Run the code:
Run the application:

   ```bash
   python app.py
