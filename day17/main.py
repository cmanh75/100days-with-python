from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(question_bank)

while quiz.is_continue():
    your_answer = quiz.query()
    quiz.check_answer(your_answer)
    quiz.report()
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.scores} / {len(quiz.question_list)}")
