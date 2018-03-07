import json
import operator


def filter_dict(input_dict):
    output_dict = dict()
    for tmp_verb in input_dict:
        sorted_x = sorted(input_dict[tmp_verb].items(), key=operator.itemgetter(1))
        output_dict[tmp_verb] = sorted_x[:5]
    return output_dict

with open('verb_nsubj_amod_dict.json', 'w') as nsubj_f:
    verb_nsubj_amod_dict = json.load(nsubj_f)

with open('verb_dobj_amod_dict.json', 'w') as dobj_f:
    verb_dobj_amod_dict = json.load(dobj_f)
filtered_nsubj_dict = filter_dict(verb_nsubj_amod_dict)
filtered_dobj_dict = filter_dict(verb_dobj_amod_dict)

while True:
    command = input('Please give me your interested word, QUIT means quit this program')
    if command == 'QUIT':
        break
    else:
        if command in filtered_nsubj_dict:
            print('Top 5 nsubj adj:', filtered_nsubj_dict[command])
        else:
            print('There is no nsubj adj record for verb:', command)
        if command in filtered_dobj_dict:
            print('Top 5 dobj adj:', filtered_dobj_dict[command])
        else:
            print('There is no dobj adj record for verb:', command)

print('end')
