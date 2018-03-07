import json

tmp_file_name = '/home/data/corpora/wikipedia/stanford_enhanced++_parsed_data/1000000.json'

with open(tmp_file_name, 'r') as original_f:
    sampled_data = json.load(original_f)

verb_nsubj_amod_dict = dict()
verb_dobj_amod_dict = dict()
for sentence in sampled_data:
    for pair in sentence:
        if pair[1] == 'nsubj':
            for tmp_pair in sentence:
                if tmp_pair[1] == 'amod' and tmp_pair[0][0] == pair[2][0]:
                    tmp_verb = pair[0][1]
                    tmp_adj = tmp_pair[2][1]
                    if tmp_verb not in verb_nsubj_amod_dict:
                        verb_nsubj_amod_dict[tmp_verb] = dict()
                    if tmp_adj not in verb_nsubj_amod_dict[tmp_verb]:
                        verb_nsubj_amod_dict[tmp_verb][tmp_adj] = 0
                    verb_nsubj_amod_dict[tmp_verb][tmp_adj] += 1
        if pair[1] == 'dobj':
            for tmp_pair in sentence:
                if tmp_pair[1] == 'amod' and tmp_pair[0][0] == pair[2][0]:
                    tmp_verb = pair[0][1]
                    tmp_adj = tmp_pair[2][1]
                    if tmp_verb not in verb_dobj_amod_dict:
                        verb_dobj_amod_dict[tmp_verb] = dict()
                    if tmp_adj not in verb_dobj_amod_dict[tmp_verb]:
                        verb_dobj_amod_dict[tmp_verb][tmp_adj] = 0
                    verb_dobj_amod_dict[tmp_verb][tmp_adj] += 1

with open('verb_nsubj_amod_dict.json', 'w') as nsubj_f:
    json.dump(verb_nsubj_amod_dict, nsubj_f)

with open('verb_dobj_amod_dict.json', 'w') as dobj_f:
    json.dump(verb_dobj_amod_dict, dobj_f)

print('end')
