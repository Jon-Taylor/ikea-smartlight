from sense_hat import SenseHat

sense = SenseHat()

def ledQuestionMark():
    sense = SenseHat()
    X = [255, 0, 0]  # Red
    O = [255, 255, 255]  # White

    question_mark = [
    O, O, O, X, X, O, O, O,
    O, O, X, O, O, X, O, O,
    O, O, O, O, O, X, O, O,
    O, O, O, O, X, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, X, O, O, O, O
    ]

    sense.set_pixels(question_mark)

def ledOff():
    sense = SenseHat()
    X = [0, 0, 0]  # Red
    O = [0, 0, 0]  # White

    question_mark = [
    O, O, O, X, X, O, O, O,
    O, O, X, O, O, X, O, O,
    O, O, O, O, O, X, O, O,
    O, O, O, O, X, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, X, O, O, O, O
    ]

    sense.set_pixels(question_mark)
