import json
import os
import pandas

def filter_word(input_word):
    tmp_output = ''
    for c in input_word:
        if c in 'zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP':
            tmp_output += c
    return tmp_output


def counting_pairs_from_yelp_parsed_data(parsed_data, verb_nsubj_amod_dict, verb_dobj_amod_dict, verb_nsubj_dict,
                                    verb_dobj_dict, noun_amod_dict):
    for i, sentence in enumerate(parsed_data):
        if i % 10000 == 0:
            print('We have counted:', i, '/', len(parsed_data))
        for subsentence in sentence:
            # print('subsentence:', subsentence)
            for pair in subsentence:
                if pair[1] == 'amod':
                    tmp_noun = pair[0][1]
                    tmp_adj = pair[2][1]
                    if tmp_noun not in noun_amod_dict:
                        noun_amod_dict[tmp_noun] = dict()
                    if tmp_adj not in noun_amod_dict[tmp_noun]:
                        noun_amod_dict[tmp_noun][tmp_adj] = 0
                    noun_amod_dict[tmp_noun][tmp_adj] += 1
                # print('pair:', pair)
                if pair[1] == 'nsubj':
                    tmp_verb = pair[0][1]
                    tmp_subj = pair[2][1]
                    if tmp_verb not in verb_nsubj_dict:
                        verb_nsubj_dict[tmp_verb] = dict()
                    if tmp_subj not in verb_nsubj_dict[tmp_verb]:
                        verb_nsubj_dict[tmp_verb][tmp_subj] = 0
                    verb_nsubj_dict[tmp_verb][tmp_subj] += 1
                    for tmp_pair in subsentence:
                        if tmp_pair[1] == 'amod' and tmp_pair[0][0] == pair[2][0]:
                            tmp_adj = tmp_pair[2][1]
                            if tmp_verb not in verb_nsubj_amod_dict:
                                verb_nsubj_amod_dict[tmp_verb] = dict()
                            if tmp_adj not in verb_nsubj_amod_dict[tmp_verb]:
                                verb_nsubj_amod_dict[tmp_verb][tmp_adj] = 0
                            verb_nsubj_amod_dict[tmp_verb][tmp_adj] += 1
                if pair[1] == 'dobj':
                    tmp_verb = pair[0][1]
                    tmp_dobj = pair[2][1]
                    if tmp_verb not in verb_dobj_dict:
                        verb_dobj_dict[tmp_verb] = dict()
                    if tmp_dobj not in verb_dobj_dict[tmp_verb]:
                        verb_dobj_dict[tmp_verb][tmp_dobj] = 0
                    verb_dobj_dict[tmp_verb][tmp_dobj] += 1
                    for tmp_pair in subsentence:
                        if tmp_pair[1] == 'amod' and tmp_pair[0][0] == pair[2][0]:
                            tmp_adj = tmp_pair[2][1]
                            if tmp_verb not in verb_dobj_amod_dict:
                                verb_dobj_amod_dict[tmp_verb] = dict()
                            if tmp_adj not in verb_dobj_amod_dict[tmp_verb]:
                                verb_dobj_amod_dict[tmp_verb][tmp_adj] = 0
                            verb_dobj_amod_dict[tmp_verb][tmp_adj] += 1


def counting_pairs_from_wiki_parsed_data(parsed_data, verb_nsubj_amod_dict, verb_dobj_amod_dict, verb_nsubj_dict,
                                    verb_dobj_dict, noun_amod_dict):
    for i, sentence in enumerate(parsed_data):
        if i % 10000 == 0:
            print('We have counted:', i, '/', len(parsed_data))
        for pair in sentence:
            # print('subsentence:', subsentence)
            if pair[1] == 'amod':
                tmp_noun = pair[0][1]
                tmp_adj = pair[2][1]
                if tmp_noun not in noun_amod_dict:
                    noun_amod_dict[tmp_noun] = dict()
                if tmp_adj not in noun_amod_dict[tmp_noun]:
                    noun_amod_dict[tmp_noun][tmp_adj] = 0
                noun_amod_dict[tmp_noun][tmp_adj] += 1
                # print('pair:', pair)
            if pair[1] == 'nsubj':
                tmp_verb = pair[0][1]
                tmp_subj = pair[2][1]
                if tmp_verb not in verb_nsubj_dict:
                    verb_nsubj_dict[tmp_verb] = dict()
                if tmp_subj not in verb_nsubj_dict[tmp_verb]:
                    verb_nsubj_dict[tmp_verb][tmp_subj] = 0
                verb_nsubj_dict[tmp_verb][tmp_subj] += 1
                for tmp_pair in sentence:
                    if tmp_pair[1] == 'amod' and tmp_pair[0][0] == pair[2][0]:
                        tmp_adj = tmp_pair[2][1]
                        if tmp_verb not in verb_nsubj_amod_dict:
                            verb_nsubj_amod_dict[tmp_verb] = dict()
                        if tmp_adj not in verb_nsubj_amod_dict[tmp_verb]:
                            verb_nsubj_amod_dict[tmp_verb][tmp_adj] = 0
                        verb_nsubj_amod_dict[tmp_verb][tmp_adj] += 1
            if pair[1] == 'dobj':
                tmp_verb = pair[0][1]
                tmp_dobj = pair[2][1]
                if tmp_verb not in verb_dobj_dict:
                    verb_dobj_dict[tmp_verb] = dict()
                if tmp_dobj not in verb_dobj_dict[tmp_verb]:
                    verb_dobj_dict[tmp_verb][tmp_dobj] = 0
                verb_dobj_dict[tmp_verb][tmp_dobj] += 1
                for tmp_pair in sentence:
                    if tmp_pair[1] == 'amod' and tmp_pair[0][0] == pair[2][0]:
                        tmp_adj = tmp_pair[2][1]
                        if tmp_verb not in verb_dobj_amod_dict:
                            verb_dobj_amod_dict[tmp_verb] = dict()
                        if tmp_adj not in verb_dobj_amod_dict[tmp_verb]:
                            verb_dobj_amod_dict[tmp_verb][tmp_adj] = 0
                        verb_dobj_amod_dict[tmp_verb][tmp_adj] += 1

print('Start to count the yelp dataset')
# tmp_file_name = '/home/data/corpora/wikipedia/stanford_enhanced++_parsed_data/1000000.json'
verb_nsubj_amod_dict = dict()
verb_dobj_amod_dict = dict()
verb_nsubj_dict = dict()
verb_dobj_dict = dict()
noun_amod_dict = dict()

if os.path.isfile('verb_nsubj_amod_dict_yelp.json'):
    with open('verb_nsubj_amod_dict_yelp.json', 'r') as f:
        verb_nsubj_amod_dict = json.load(f)

if os.path.isfile('verb_dobj_amod_dict_yelp.json'):
    with open('verb_dobj_amod_dict_yelp.json', 'r') as f:
        verb_dobj_amod_dict = json.load(f)

if os.path.isfile('verb_nsubj_dict_yelp.json'):
    with open('verb_nsubj_dict_yelp.json', 'r') as f:
        verb_nsubj_dict = json.load(f)

if os.path.isfile('verb_dobj_dict_yelp.json'):
    with open('verb_dobj_dict_yelp.json', 'r') as f:
        verb_dobj_dict = json.load(f)

if os.path.isfile('noun_amod_dict_yelp.json'):
    with open('noun_amod_dict_yelp.json', 'r') as f:
        noun_amod_dict = json.load(f)

if os.path.isfile('counted_yelp_file.json'):
    with open('counted_yelp_file.json', 'r') as f:
        counted_yelp_file = json.load(f)
else:
    counted_yelp_file = list()

yelp_folder_location = '/home/data/corpora/YELP/parsed_yelp_data_with_stanford/'
for f_name in os.listdir(yelp_folder_location):
    tmp_file_name = yelp_folder_location + f_name
    if tmp_file_name in counted_yelp_file:
        print('We have counted this file')
        continue
    print('We are working on file:', tmp_file_name)
    sampled_data = list()
    with open(tmp_file_name, 'r') as original_f:
        sampled_data = json.load(original_f)
    counting_pairs_from_yelp_parsed_data(sampled_data, verb_nsubj_amod_dict, verb_dobj_amod_dict, verb_nsubj_dict,
                                            verb_dobj_dict, noun_amod_dict)
    counted_yelp_file.append(tmp_file_name)

    with open('verb_dobj_dict_yelp.json', 'w') as f:
        json.dump(verb_dobj_dict, f)

    with open('verb_nsubj_dict_yelp.json', 'w') as f:
        json.dump(verb_nsubj_dict, f)

    with open('verb_dobj_amod_dict_yelp.json', 'w') as f:
        json.dump(verb_dobj_amod_dict, f)

    with open('verb_nsubj_amod_dict_yelp.json', 'w') as f:
        json.dump(verb_nsubj_amod_dict, f)

    with open('noun_amod_dict_yelp.json', 'w') as f:
        json.dump(noun_amod_dict, f)

    with open('counted_yelp_file.json', 'w') as f:
        json.dump(counted_yelp_file, f)

print('end')
