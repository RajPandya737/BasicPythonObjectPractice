class Problem:
    def __init__(self, Question, Answer):
        self.Question = Question
        self.Answer = Answer
    def set_question(self, q):
        self.Question = q
    def set_answer(self, a):
        self.Answer = a
    def get_question(self):
        return self.Question
    def get_answer(self):
        return self.Answer
    def equals(self, p):
        if p.get_question() == self.Question and p.get_answer() == self.Answer:
            return True
        else:
            return False

