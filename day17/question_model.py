class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
    def get_text(self):
        return self.text
    def get_answer(self):
        return self.answer