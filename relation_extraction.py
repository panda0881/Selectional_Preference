import json
import os


def counting_pairs_from_parsed_data(parsed_data, verb_nsubj_amod_dict, verb_dobj_amod_dict, verb_nsubj_dict, verb_dobj_dict):
    for sentence in parsed_data:
        for pair in sentence:
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

for name in os.listdir('parsed_yelp_data_with_stanford'):
    file_name = 'parsed_yelp_data_with_stanford/' + name
    with open(file_name, 'r') as original_f:
        sampled_data = json.load(original_f)
        counting_pairs_from_parsed_data(sampled_data, verb_nsubj_amod_dict, verb_dobj_amod_dict, verb_nsubj_dict, verb_dobj_dict)

with open('verb_nsubj_amod_dict.json', 'w') as f:
    json.dump(verb_nsubj_amod_dict, f)

with open('verb_dobj_amod_dict.json', 'w') as f:
    json.dump(verb_dobj_amod_dict, f)

with open('verb_nsubj_dict.json', 'w') as f:
    json.dump(verb_nsubj_dict, f)

with open('verb_dobj_dict.json', 'w') as f:
    json.dump(verb_dobj_dict, f)

print('end')
