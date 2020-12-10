# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:11:08 2020

@author: jmitc
"""

class Question:
    """
    A class used to represent a multiple choice question
    
     Attributes:
            prompt (str): a string containing the full question and options
            answer (str): the correct answer to the question
            options (str)a list of valid responses to the question
    """
    def __init__(self, prompt, answer, options):
        """ Instantiates our Questions
        
        Parameters:
            prompt (str): a string containing the full question and options
            answer (str): the correct answer to the question
            options (str)a list of valid responses to the question
            
        """
        self.prompt = prompt
        self.answer = answer
        self.options = options



        

