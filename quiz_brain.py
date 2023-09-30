import html

class Quiz_brain:
    
    def __init__(self,q_list):
        self.question_number=0
        self.score=0
        self.question_list=q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        

    def next_ques(self):
        self.current_q=self.question_list[self.question_number]
        self.question_number+=1
        q_text = html.unescape(self.current_q.text)
        return f"Q.{self.question_number}:{q_text}"
        # user_answer = input(f"Q.{self.question_number}:{q_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer= self.current_q.answer
        if user_answer.lower()==correct_answer.lower():

            self.score+=1
            return True
        else:
            return False

