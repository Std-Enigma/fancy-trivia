
import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = -1
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        return self.question_number == len(self.question_list) - 1

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number + 1}: {html.unescape(self.current_question.text)}"

    def check_answer(self, answer: bool) -> bool:
        if answer == self.question_list[self.question_number].answer:
            self.score += 1
            return True
        else:
            return False
    