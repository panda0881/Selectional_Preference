import json
import os

def merge_dict(wiki_dict, yelp_dict, nyt_dict):
    final_dict = dict()
    for term1 in wiki_dict:
        if term1 not in final_dict:
            final_dict[term1] = dict()
        for term2 in wiki_dict[term1]:
            if term2 not in final_dict[term1]:
                final_dict[term1][term2] = 0
            final_dict[term1][term2] += wiki_dict[term1][term2]

    for term1 in yelp_dict:
        if term1 not in final_dict:
            final_dict[term1] = dict()
        for term2 in yelp_dict[term1]:
            if term2 not in final_dict[term1]:
                final_dict[term1][term2] = 0
            final_dict[term1][term2] += yelp_dict[term1][term2]

    for term1 in nyt_dict:
        if term1 not in final_dict:
            final_dict[term1] = dict()
        for term2 in nyt_dict[term1]:
            if term2 not in final_dict[term1]:
                final_dict[term1][term2] = 0
            final_dict[term1][term2] += nyt_dict[term1][term2]

    return final_dict



print('Loading data for Wiki')
with open('verb_nsubj_amod_dict_wiki.json', 'r') as f:
    wiki_verb_nsubj_amod_dict = json.load(f)

with open('verb_dobj_amod_dict_wiki.json', 'r') as f:
    wiki_verb_dobj_amod_dict = json.load(f)

with open('verb_nsubj_dict_wiki.json', 'r') as f:
    wiki_verb_nsubj_dict = json.load(f)

with open('verb_dobj_dict_wiki.json', 'r') as f:
    wiki_verb_dobj_dict = json.load(f)

with open('noun_amod_dict_wiki.json', 'r') as f:
    wiki_noun_amod_dict = json.load(f)

print('Loading data for Yelp')
with open('verb_nsubj_amod_dict_yelp.json', 'r') as f:
    yelp_verb_nsubj_amod_dict = json.load(f)

with open('verb_dobj_amod_dict_yelp.json', 'r') as f:
    yelp_verb_dobj_amod_dict = json.load(f)

with open('verb_nsubj_dict_yelp.json', 'r') as f:
    yelp_verb_nsubj_dict = json.load(f)

with open('verb_dobj_dict_yelp.json', 'r') as f:
    yelp_verb_dobj_dict = json.load(f)

with open('noun_amod_dict_yelp.json', 'r') as f:
    yelp_noun_amod_dict = json.load(f)

print('Loading data for NYT')
with open('verb_nsubj_amod_dict_nyt.json', 'r') as f:
    nyt_verb_nsubj_amod_dict = json.load(f)

with open('verb_dobj_amod_dict_nyt.json', 'r') as f:
    nyt_verb_dobj_amod_dict = json.load(f)

with open('verb_nsubj_dict_nyt.json', 'r') as f:
    nyt_verb_nsubj_dict = json.load(f)

with open('verb_dobj_dict_nyt.json', 'r') as f:
    nyt_verb_dobj_dict = json.load(f)

with open('noun_amod_dict_nyt.json', 'r') as f:
    nyt_noun_amod_dict = json.load(f)

print('Starting to merge dict')

verb_nsubj_dict = merge_dict(wiki_verb_nsubj_dict, yelp_verb_nsubj_dict, nyt_verb_nsubj_dict)
verb_dobj_dict = merge_dict(wiki_verb_dobj_dict, yelp_verb_dobj_dict, nyt_verb_dobj_dict)
noun_amod_dict = merge_dict(wiki_noun_amod_dict, yelp_noun_amod_dict, nyt_noun_amod_dict)
verb_nsubj_amod_dict = merge_dict(wiki_verb_nsubj_amod_dict, yelp_verb_nsubj_amod_dict, nyt_verb_nsubj_amod_dict)
verb_dobj_amod_dict = merge_dict(wiki_verb_dobj_amod_dict, yelp_verb_dobj_amod_dict, nyt_verb_dobj_amod_dict)


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

print('We are working on nsubj_amod')
SP_pairs = list()
Plausibility_score = list()
natural_frequency = list()
with open('nsubj_amod_anotation.txt', 'r') as f:
    for line in f:
        words = line[:-1].split('\t')
        SP_pairs.append((words[0], words[1]))
        Plausibility_score.append(float(words[2]))
        total_number = 0
        for adj in verb_nsubj_amod_dict[words[0]]:
            total_number += verb_nsubj_amod_dict[words[0]][adj]
        if words[1] not in verb_nsubj_amod_dict[words[0]]:
            natural_frequency.append(0)
        else:
            natural_frequency.append(verb_nsubj_amod_dict[words[0]][words[1]]/total_number)

nsubj_amod_result = dict()
nsubj_amod_result['annotation'] = Plausibility_score
nsubj_amod_result['frequency'] = natural_frequency

print('We are working on dobj_amod')
SP_pairs = list()
Plausibility_score = list()
natural_frequency = list()
with open('dobj_amod_anotation.txt', 'r') as f:
    for line in f:
        words = line[:-1].split('\t')
        SP_pairs.append((words[0], words[1]))
        Plausibility_score.append(float(words[2]))
        total_number = 0
        for adj in verb_dobj_amod_dict[words[0]]:
            total_number += verb_dobj_amod_dict[words[0]][adj]
        if words[1] not in verb_dobj_amod_dict[words[0]]:
            natural_frequency.append(0)
        else:
            natural_frequency.append(verb_dobj_amod_dict[words[0]][words[1]]/total_number)

dobj_amod_result = dict()
dobj_amod_result['annotation'] = Plausibility_score
dobj_amod_result['frequency'] = natural_frequency

with open('natural_frequency_result.json', 'w') as f:
    json.dump({'amod': amod_result, 'nsubj': nsubj_result, 'dobj': dobj_result, 'nsubj_amod': nsubj_amod_result, 'dobj_amod': dobj_result}, f)

print('end')
