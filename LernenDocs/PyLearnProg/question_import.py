__author__ = 'Fabian'

import random

class QuestionImporter():

    def __init__(self):
        pass

    def read_questions_from_file(self, path: str= "G:\Workplace\PythonWorkspace\Simple\LernenDocs\PyLearnProg\question.txt"):
        f = open(path, 'r')
        subject = f.readline()
        category = f.readline()

        list_content = []
        for line in f:
            list_content.append(line)

        return_questions = Questions()
        return_questions.category = category
        return_questions.subject = subject

        x = 1

        while x <= list_content.__len__():
            return_questions.list_questions.append(Question(list_content[x-1], list_content[x]))
            x += 2

        return return_questions

class Question():

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return "Frage: " + self.question + "\nAntwort:  " + self.answer

class Questions():

    def __init__(self):
        self.list_questions = []
        self.category = ""
        self.subject = ""
        self.question_index = 0

    def get_random_question(self) -> Question:
        x = random.randint(0, self.list_questions.__len__() - 1)
        return self.list_questions[x]

    def get_next_question(self)-> Question:
        x = self.question_index
        self.question_index += 1

        if x >= self.list_questions.__len__():
            x = 0
            self.question_index = 1

        return self.list_questions[x]

    def reset_question_index(self):
        self.question_index = 0


