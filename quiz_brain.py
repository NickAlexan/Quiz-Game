class QuizBrain:

    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q{self.question_num}: {current_question.text}. True/False? ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self, user_answer, right_answer):
        if user_answer.lower() == right_answer.lower():
            self.score += 1
            print("You are right!")
        else:
            print("You are wrong!")
        print(f"The right answer is {right_answer}")
        print(f"Your score is: {self.score}/{self.question_num}")

