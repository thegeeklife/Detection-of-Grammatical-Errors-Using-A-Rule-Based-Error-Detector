# Project Intro

We had data from an ESL Test (English as Second Language) where the prompt reads-out a sentence and the test-taker is asked to repeat it (like a listening test). 
The prompt sentences (treated as the correct ones) were in a separate .txt file and the responses were in another text file (targetted file to detect errors from).

The errors we focussed on detecting include - Noun pluralize, verb pluralize and verb past.

# Rule Based Grammatical Error Detector 

The ged.py script requires two .txt files; one with the correct sentence - prompt.txt and other with the responses - response.txt. It then returns what errors were there and which errors were common.
