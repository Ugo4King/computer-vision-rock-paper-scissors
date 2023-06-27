# Computer Vision RPS
# Rock-Paper-Scissors Game

This is a Python-based Rock-Paper-Scissors game that uses computer vision to allow the user to play against the computer. The game captures the user's hand gesture using the webcam, processes it with a pre-trained machine learning model, and determines the winner based on the gestures.


## Features

- Uses OpenCV to capture and display frames from the webcam.
- Utilizes a pre-trained Keras model for gesture recognition.
- Implements a countdown timer for the user to show their hand gesture.
- Tracks and displays the score of the computer and user.
- Plays the game until either the computer or the user wins three rounds.

## Installation

1. Clone the repository:


2. Install the required dependencies:


3. Download the pre-trained Keras model `keras_model.h5` and place it in the project directory.

## Usage

1. Run the `camera_rps.py` script:


2. The webcam will open, and you will see a countdown timer displayed on the screen.

3. Show your hand gesture before the timer reaches zero.

4. The computer will randomly choose a gesture, and the winner of the round will be determined.

5. The game continues until either the computer or the user wins three rounds.

## Screenshots

## Future Improvements

- Enhance the user experience by incorporating graphical elements in the interface.
- Implement a better hand detection and tracking algorithm for more accurate gesture recognition.
- Add sound effects and animations to make the game more engaging.
- Provide an option to switch between different AI models for gesture recognition.
- Develop a multiplayer mode to allow users to play against each other remotely.
- Implement a high score leaderboard to track the best performances.

