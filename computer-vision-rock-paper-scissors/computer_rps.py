import cv2
from keras.models import load_model
import numpy as np
import time

class RockPaperScissorsGame:
    def __init__(self, model_path):
        self.model = load_model(model_path)
        self.cap = cv2.VideoCapture(0)
        self.computer_wins = 0
        self.user_wins = 0

    def get_prediction(self, frame):
        resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1
        data = np.expand_dims(normalized_image, axis=0)
        prediction = self.model.predict(data)
        return prediction[0]

    def play(self):
        while self.computer_wins < 3 and self.user_wins < 3:
            countdown_time = 3
            start_time = time.time()

            while True:
                ret, frame = self.cap.read()

                elapsed_time = time.time() - start_time
                remaining_time = countdown_time - int(elapsed_time)
                if remaining_time <= 0:
                    prediction = self.get_prediction(frame)
                    user_guess = np.argmax(prediction)
                    guess_text = self.get_gesture_text(user_guess)
                    print(f"You chose: {guess_text}")
                    break

                self.display_countdown(frame, remaining_time)
                cv2.imshow('frame', frame)

                # Press q to close the window or c to continue immediately
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('c'):
                    remaining_time = 0

            if remaining_time <= 0:
                computer_guess = np.random.randint(3)
                print(f"Computer chose: {self.get_gesture_text(computer_guess)}")
                self.determine_winner(user_guess, computer_guess)

        self.release_resources()

    def display_countdown(self, frame, remaining_time):
        cv2.putText(frame, f"Countdown: {remaining_time}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    def get_gesture_text(self, gesture_index):
        gestures = ["Rock", "Paper", "Scissors"]
        return gestures[gesture_index]

    def determine_winner(self, user_guess, computer_guess):
        if user_guess == (computer_guess + 1) % 3:
            self.user_wins += 1
            print("You win this round!")
        elif computer_guess == (user_guess + 1) % 3:
            self.computer_wins += 1
            print("Computer wins this round!")
        else:
            print("It's a draw!")

    def release_resources(self):
        self.cap.release()
        cv2.destroyAllWindows()


# Create an instance of the game and play
game = RockPaperScissorsGame('keras_model.h5')
game.play()
