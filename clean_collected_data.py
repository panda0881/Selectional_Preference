from nltk.corpus import wordnet as wn
from nltk.corpus import verbnet
import pandas
import json
import xml.etree.ElementTree as etree
import os
import random
import operator

def filter_word(input_word):
    tmp_output = ''
    for c in input_word:
        if c in 'zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP':
            tmp_output += c
    return tmp_output

frequent_words_data = pandas.read_csv('verb_data/word_frequency.csv')
frequent_nouns = list()
frequent_adjectives = list()
for index, row in frequent_words_data.iterrows():
    part_of_speech = row[2]
    if part_of_speech == 'n':
        frequent_nouns.append(filter_word(row[1]))
    elif part_of_speech == 'j':
        frequent_adjectives.append(filter_word(row[1]))

print('We are working on dobj')
with open('verb_dobj_dict.json', 'r') as f:
    verb_dobj_dict = json.load(f)

cleaned_verb_dobj_dict = dict()
for verb in verb_dobj_dict:
    tmp_dict = dict()
    for noun in verb_dobj_dict[verb]:
        if noun in frequent_nouns:
            tmp_dict[noun] = verb_dobj_dict[verb][noun]
    cleaned_verb_dobj_dict[verb] = tmp_dict

with open('cleaned_verb_dobj_dict.json', 'w') as f:
    json.dump(cleaned_verb_dobj_dict, f)

print('We are working on nsubj')
with open('verb_nsubj_dict.json', 'r') as f:
    verb_nsubj_dict = json.load(f)

cleaned_verb_nsubj_dict = dict()
for verb in verb_nsubj_dict:
    tmp_dict = dict()
    for noun in verb_nsubj_dict[verb]:
        if noun in frequent_nouns:
            tmp_dict[noun] = verb_nsubj_dict[verb][noun]
    cleaned_verb_nsubj_dict[verb] = tmp_dict

with open('cleaned_verb_nsubj_dict.json', 'w') as f:
    json.dump(cleaned_verb_nsubj_dict, f)

print('We are working on dobj_amod')
with open('verb_dobj_amod_dict.json', 'r') as f:
    verb_dobj_amod_dict = json.load(f)

cleaned_verb_dobj_amod_dict = dict()
for verb in verb_dobj_amod_dict:
    tmp_dict = dict()
    for noun in verb_dobj_amod_dict[verb]:
        if noun in frequent_adjectives:
            tmp_dict[noun] = verb_dobj_amod_dict[verb][noun]
    cleaned_verb_dobj_amod_dict[verb] = tmp_dict

with open('cleaned_verb_dobj_amod_dict.json', 'w') as f:
    json.dump(cleaned_verb_dobj_amod_dict, f)

print('We are working on nsubj_amod')
with open('verb_nsubj_amod_dict.json', 'r') as f:
    verb_nsubj_amod_dict = json.load(f)

cleaned_verb_nsubj_amod_dict = dict()
for verb in verb_nsubj_amod_dict:
    tmp_dict = dict()
    for noun in verb_nsubj_amod_dict[verb]:
        if noun in frequent_adjectives:
            tmp_dict[noun] = verb_nsubj_amod_dict[verb][noun]
    cleaned_verb_nsubj_amod_dict[verb] = tmp_dict

with open('cleaned_verb_nsubj_amod_dict.json', 'w') as f:
    json.dump(cleaned_verb_nsubj_amod_dict, f)


