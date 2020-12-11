# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 21:50:59 2020

@author: jmitc
"""

import unittest as ut
from Trivia import valid_answer, evaluate, questions

class TestTrivia(ut.TestCase):
    
    def test_valid_answer(self):
        testquestion = questions[0]
        testquestion1 = questions[8]
        self.assertTrue(valid_answer("a",testquestion))
        self.assertTrue(valid_answer("A",testquestion))
        self.assertTrue(valid_answer("f",testquestion1))
        self.assertTrue(valid_answer("T",testquestion1))
    
    def test_evaluate(self):
        for position in range(0-len(questions)+1):
            question = questions[position]
            answer = question.answer
            self.assertTrue(evaluate(questions, position))
        
        
        
            













if __name__ == "__main__":
  ut.main(argv=['v'], exit=False)