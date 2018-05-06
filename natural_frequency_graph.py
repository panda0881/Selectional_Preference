import json
import os


with open('verb_nsubj_dict_all.json', 'r') as f:
    verb_nsubj_dict = json.load(f)

with open('verb_dobj_dict_all.json', 'r') as f:
    verb_dobj_dict = json.load(f)

with open('noun_amod_dict_all.json', 'r') as f:
    noun_amod_dict = json.load(f)


print('We are working on amod')
SP_pairs = list()
Plausibility_score = list()
natural_frequency = list()
with open('amod_anotation.txt', 'r') as f:
    for line in f:
        words = line[:-1].split('\t')
        SP_pairs.append((words[0], words[1]))
        Plausibility_score.append(float(words[2]))
        total_number = 0
        for adj in noun_amod_dict[words[0]]:
            total_number += noun_amod_dict[words[0]][adj]
        if words[1] not in noun_amod_dict[words[0]]:
            natural_frequency.append(0)
        else:
            natural_frequency.append(noun_amod_dict[words[0]][words[1]]/total_number)

amod_result = dict()
amod_result['annotation'] = Plausibility_score
amod_result['frequency'] = natural_frequency

print('We are working on nsubj')
SP_pairs = list()
Plausibility_score = list()
natural_frequency = list()
with open('nsubj_anotation.txt', 'r') as f:
    for line in f:
        words = line[:-1].split('\t')
        SP_pairs.append((words[0], words[1]))
        Plausibility_score.append(float(words[2]))
        total_number = 0
        for noun in verb_nsubj_dict[words[0]]:
            total_number += verb_nsubj_dict[words[0]][noun]
        if words[1] not in verb_nsubj_dict[words[0]]:
            natural_frequency.append(0)
        else:
            natural_frequency.append(verb_nsubj_dict[words[0]][words[1]]/total_number)

nsubj_result = dict()
nsubj_result['annotation'] = Plausibility_score
nsubj_result['frequency'] = natural_frequency

print('We are working on dobj')
SP_pairs = list()
Plausibility_score = list()
natural_frequency = list()
with open('dobj_anotation.txt', 'r') as f:
    for line in f:
        words = line[:-1].split('\t')
        SP_pairs.append((words[0], words[1]))
        Plausibility_score.append(float(words[2]))
        total_number = 0
        for noun in verb_dobj_dict[words[0]]:
            total_number += verb_dobj_dict[words[0]][noun]
        if words[1] not in verb_dobj_dict[words[0]]:
            natural_frequency.append(0)
        else:
            natural_frequency.append(verb_dobj_dict[words[0]][words[1]]/total_number)

dobj_result = dict()
dobj_result['annotation'] = Plausibility_score
dobj_result['frequency'] = natural_frequency

with open('natural_frequency_result.json', 'w') as f:
    json.dump({'amod': amod_result, 'nsubj':nsubj_result, 'dobj':dobj_result}, f)

print('end')
