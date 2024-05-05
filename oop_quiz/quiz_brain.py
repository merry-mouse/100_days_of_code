class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        q_text = self.question_list[self.question_number].text
        q_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {q_text} (True/False t/f)?: ")
        print(f"Right answer is {q_answer}.")
        if self.check_answer(user_answer, q_answer) is True:
            self.score += 1
        print(f"Score: {self.score}/{self.question_number}")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, right_answer):
        return user_answer[0].lower() == right_answer[0].lower()
