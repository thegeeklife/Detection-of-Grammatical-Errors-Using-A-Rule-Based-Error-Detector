import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import numpy as np

# data load
prompts = open('prompts.txt').read().split('\n')
responses = open('responses.txt').read().split('\n')

# pos_tagging prompts
prompts_tagged = []
for item in prompts:
    tokenized = nltk.word_tokenize(item)
    tagged = nltk.pos_tag(tokenized)
    prompts_tagged.append(tagged)

# error_dict
error_dict = {'noun_pluralize':[('NN','NNS'),('NNS','NN')],
              'verb_pluralize':[('VBZ','VB'),('VB','VBZ'),('VBZ','VBP'),('VBP','VBZ')],
              'verb_past':[('VB','VBD'),('VBD','VB'),('VB','VBN'),('VBN','VB'),('VBP','VBD'),('VBD','VBP'),('VBP','VBN'),('VBN','VBP')]}

#count_incomp=0              

#comparing pos_tag tuples (1st element: ot, 2nd element: rt)
def returnNotMatches(a, b):
    return [[x for x in a if x not in b], [x for x in b if x not in a]]

#Extracting tokens from responses that are not matching with prompts 
j = 0
count_correct = 0 #total number of correct responses
count_incorrect = 0 #total number of incorrect responses
notMatch = []

for i in range(0,12):
    for j in range(j,j+30):
        if (prompts[i] == responses[j]):
            tokenized = nltk.word_tokenize(responses[j])
            tagged = nltk.pos_tag(tokenized)
            notMatch.append(returnNotMatches(prompts_tagged[i],tagged))
            count_correct+=1
        else:
            tokenized = nltk.word_tokenize(responses[j])
            tagged = nltk.pos_tag(tokenized)
            notMatch.append(returnNotMatches(prompts_tagged[i],tagged))
            count_incorrect+=1
    j+=1

#Extracting error_tokens that are same words in same syntax context but tagged differently from notMatch[]
errors_detected = []
def charMatch(notMatch):
    ot = [] 
    rt = []
    global errors_detected

    for i in range(len(notMatch)):
        ot.append(notMatch[i][0])
        rt.append(notMatch[i][1])    
    for j in range(len(ot)):
        for ot_item in ot[j]: ##item=tuple, item[0]=token, item[1]=tag
            comp1 = ot_item[0]
            for rt_item in rt[j]:
                comp2 = rt_item[0]
                if(len(comp1)>=4 and len(comp2)>=4):
                    if(comp1[:4]==comp2[:4]):
                        temp = [str(j)+"th response has error token",ot_item, rt_item, j]
                        errors_detected.append(temp)


#Identifying types of grammatical errors by comparing with error dictionary 
n_plrl = 0 #total number of noun pluralization error
v_plrl = 0 #total number of verb pluralization error
v_past = 0 #total number of verb past tense error

def errorMatch(errors_detected):
    global n_plrl
    global v_plrl
    global v_past
    
    for error in errors_detected: ##error[1]:original tuple
        error_tuple = (error[1][1], error[2][1])
        for key in error_dict:
            if(error_tuple in error_dict[key]):
                if(key == 'noun_pluralize'):
                    n_plrl+=1
                    print(error_tuple, "detected for noun pluralization error\n")
                if(key == 'verb_pluralize'):
                    v_plrl+=1
                    print(error_tuple, "detected for verb pluralization error\n")
                if(key == 'verb_past'):
                    v_past+=1
                    print(error_tuple, "detected for verb past tense error\n")

#test
charMatch(notMatch)
errorMatch(errors_detected)
total=0
total = n_plrl+v_plrl+v_past
print(total)
print(n_plrl/total)
print(v_plrl/total)
print(v_past/total)
