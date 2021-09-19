#!/usr/bin/python

#Exquisite Corpse is a Python Module for generating a random text.
#Version 2
#Matt Briggs, March 26 2016
#Changes: added random sentence generator

import exquisiteOM as ex

length_in_sentences = 20

maketext = ex.Paragraph()
bodytext = maketext.get(length_in_sentences)

print(bodytext)