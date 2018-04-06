from nltk.corpus import wordnet as wn
from nltk.corpus import verbnet
import pandas
import json
import xml.etree.ElementTree as etree
import os
import random


def filter_word(input_word):
    tmp_output = ''
    for c in input_word:
        if c in 'zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP':
            tmp_output += c
    return tmp_output


frequent_verbs_data = pandas.read_csv('verb_data/verb_frequency.csv')
frequent_verbs = list()
for index, row in frequent_verbs_data.iterrows():
    # test = row['Word']
    test = filter_word(row[1])
    frequent_verbs.append(test)
    # print('lalala')
# print(frequency_data)

frequent_words_data = pandas.read_csv('verb_data/word_frequency.csv')
frequent_nouns = list()
frequent_adjectives = list()
for index, row in frequent_words_data.iterrows():
    part_of_speech = row[2]
    if part_of_speech == 'n':
        frequent_nouns.append(filter_word(row[1]))
    elif part_of_speech == 'j':
        frequent_adjectives.append(filter_word(row[1]))



# test = wn.all_synsets(pos='v')
# verb = list()
# for verb_synset in wn.all_synsets(pos='v'):
#     # verb.append(verb_synset)
#     verb.append(verb_synset._name.split('.')[0])
# print(len(verb))
# new_verb = set(verb)
# print(len(new_verb))

# test_example = 'verb_data/new_vn/eat-39.1.xml'
# category = test_example.split('-')[1].split('.')[0]
verb_dict = dict()

for f_name in os.listdir('verb_data/new_vn'):
    file_name = 'verb_data/new_vn/' + f_name
    name_verb = f_name.split('-')[0]
    category = file_name.split('-')[1].split('.')[0]
    if category not in verb_dict:
        verb_dict[category] = list()
    verb_dict[category].append(name_verb)
    with open(file_name, 'r') as f:
        raw_data = f.read()
        tmp = raw_data.split('name=')
        for tmp2 in tmp[1:]:
            verb_dict[category].append(tmp2[1:].split('"')[0])

selected_all_verbs = list()
all_verbnet_verbs = list()
limitation = 3
added_verbs = list()

for category in verb_dict:
    tmp_verbs = verb_dict[category]
    contained_verbs = list()
    for v in tmp_verbs:
        if v in frequent_verbs:
            contained_verbs.append(v)
    random.shuffle(tmp_verbs)
    contained_verbs = contained_verbs + tmp_verbs
    for v in contained_verbs[:limitation]:
        if v not in frequent_verbs:
            added_verbs.append(v)
    # if len(tmp_verbs) < limitation:
    #     for verb in tmp_verbs:
    #         selected_all_verbs.append(verb)
    # else:
    #     selected_tmp_verbs = list()
    #     for v in frequent_verbs:
    #         if v in tmp_verbs:
    #             selected_tmp_verbs.append(v)
    #         if len(selected_tmp_verbs) >= limitation:
    #             break
    #     if len(selected_tmp_verbs) < limitation:
    #         random.shuffle(tmp_verbs)
    #         selected_tmp_verbs = selected_tmp_verbs + tmp_verbs
    #         selected_tmp_verbs = selected_tmp_verbs[:limitation]
    #     for v in selected_tmp_verbs:
    #         selected_all_verbs.append(v)

print(len(added_verbs))
test_verbs = frequent_verbs + added_verbs
# test_verbs = list()
# for v in frequent_verbs:
#     if v in all_verbnet_verbs:
#         test_verbs.append(v)
# print(test_verbs)

with open('selected_verbs.json', 'w') as f:
    json.dump(test_verbs, f)


with open('Wino_verb.json', 'r') as f:
    wino_data = json.load(f)
#
print('We analyzing PDP')
PDP_data = wino_data['PDP']
PDP_covered_verbs = list()
for verb in PDP_data:
    if verb in test_verbs:
        PDP_covered_verbs.append(verb)

print('We analyzing Wino')
Wino_data = wino_data['Wino']
Wino_covered_verbs = list()
for verb in Wino_data:
    if verb in test_verbs:
        Wino_covered_verbs.append(verb)
#
print(len(PDP_covered_verbs), len(PDP_data), len(PDP_covered_verbs)/len(PDP_data))
print(len(Wino_covered_verbs), len(Wino_data), len(Wino_covered_verbs)/len(Wino_data))

print('end')
