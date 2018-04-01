#!/usr/bin/python

#Exquisite Corpse is a Python Module for generating a random text.
#Version 2.0
#Matt Briggs, April 24 2016

import random
import vocabulary1 as v

class Word:
    #Word takes a vocabulary list and returns a random word. The object is used by the Entity and Action objects
    def __init__(self):
        pass

    def pick(self, list):
        size = len(list)
        pick = random.randrange(0,size)
        selection = list[pick]
        return selection

class Paragraph:
    #Creates a paragraph object. The get method will create a number of sentences.
    def __init__(self):
        self.paragraph = ""

    def get(self, number=0):
        paragraph = ""
        for i in range(number):
            newsentence = Sentence()
            newsentence = Sentence.get(self)
            paragraph = paragraph + newsentence 
        return paragraph

class Sentence:
    #Creates a sentnece with a object, verb, direct object.
    def __init__(self):
        self.subject = Entity()
        self.verb = Action()
        self.target = Entity()

    def get(self):
        s = []
        s.append(Article.get(self) + " " + Entity.get(self)  + " " + Action.get(self) + "s " + Article.get(self) + " " + Entity.get(self) + Punctuation.get(self) + " ")
        s.append(Article.get(self) + " " + Entity.get(self) + " " + Action.get(self) + "s " + Article.get(self) + " " + Entity.get(self) + " and " + Article.get(self) + " " + Entity.get(self) + Punctuation.get(self) + " ")
        s.append(Article.get(self) + " " + Entity.get(self) + " " + Action.get(self) + "s " + Article.get(self) + " " + Entity.get(self) + ", " + Article.get(self) + " " + Entity.get(self) + ", and the " + Article.get(self) + " " + Entity.get(self) + Punctuation.get(self) + " ")
        s.append("has the " + Entity.get(self) + " " + Action.get(self) + "s " + Article.get(self) + " " + Entity.get(self) + "? ")
        s.append(Action.get(self) + " to the " + Article.get(self) + " " + Entity.get(self) + ", " + Article.get(self) + " " + Entity.get(self) + " " + Action.get(self) + Punctuation.get(self) + " ")
        size = len(s)
        pick = random.randrange(0,size)
        select = s[pick]
        return select.capitalize()

class Article:
    #Creates the opening article of the sentence. At this point always, "The."
    def __init__(self):
        self.part = "empty"
        self.definitive = False

    def get(self):
        art = Word()
        art = Word.pick(self, v.article)
        return art

class Punctuation:
    #Creates the closing punctuation of the sentence. At this point alwasy a period.
    def __init__(self):
        self.part = "empty"
        self.definitive = False
        
    def get(self):
        term = Word()
        term = Word.pick(self, v.terminal)
        return term

class Entity:
    #Creates an sentence object or a sentence direct object. Called enity so as not to conflict with entity.
    def __init__(self):
        self.part = "empty"
        self.adjective = "adjective"
        self.noun = "noun"
        self.definitive = False

    def get(self):
        adj = Word()
        adj = Word.pick(self, v.adjective)
        nun = Word()
        nun = Word.pick(self, v.noun)
        part = adj + " " + nun
        return part


class Action:
    #Creates the action (verb) portion of the sentence. Built from the Word object.
    def __init__(self):
        #self.adverb = "adverb" TODO: Add adverb to vocabulary
        self.part = "empty"
        self.verb = "verb"

    def get(self):
        ver = Word()
        ver = Word.pick(self, v.verb)
        part = ver 
        return part
