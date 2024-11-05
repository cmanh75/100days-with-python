class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.scores = 0
    def current_answer(self):
        return self.question_list[self.question_number].get_answer()
    def next_question(self):
        self.question_number += 1
    def is_continue(self):
        print(self.question_number)
        return self.question_number < len(self.question_list)
    def query(self):
        current_question = self.question_list[self.question_number].get_text()
        return (input(f"Q.{self.question_number + 1}: {current_question} (True/False):"))
    def report(self):
        print(f"The correct answer was: {self.current_answer()}")
        print(f"Your current score is {self.scores} / {self.question_number + 1}")
    def check_answer(self, answer):
        correct_answer = self.current_answer()
        if correct_answer == answer:
            print("You got it right!")
            self.scores += 1
        else:
            print("You got it wrong!")