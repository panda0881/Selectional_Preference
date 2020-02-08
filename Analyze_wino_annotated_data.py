import pandas
import os
import json


worker_ids = list()


print('We are working on dobj_amod')
result_dict = dict()

file_name = 'wino_annotation/wino_dobj_amod.csv'
test_data = pandas.read_csv(file_name)
for cal_name in test_data:
    if cal_name == 'WorkerId':
        worker_ids += test_data[cal_name].tolist()
    if 'Answer' in cal_name:
        record = test_data[cal_name].tolist()
        if cal_name[7:] not in result_dict:
            result_dict[cal_name[7:]] = list()
        for score in record:
            if score > 0:
                result_dict[cal_name[7:]].append(score)

result_file = open('wino_annotation/dobj_amod_annotation.txt', 'w')

with open('wino_dobj_amod.txt', 'r') as f:
    counter = 0
    for line in f:
        counter += 1
        words = line[:-1].split('\t')
        verb = words[0]
        adjs = words[1:]
        for i, adj in enumerate(adjs):
            tmp_name = 'dobj_amod_v' + str(counter) + '_' + str(i+1)
            if tmp_name in ['dobj_amod_v12_4']:
                continue
            score = sum(result_dict[tmp_name])/len(result_dict[tmp_name])
            score = (score-1)*2.5
            result_file.write(verb+'\t'+adj+'\t'+str(score)+'\n')
result_file.close()
print(len(set(worker_ids)))

print('We are working on nsubj_amod')
result_dict = dict()
file_name = 'wino_annotation/wino_nsubj_amod.csv'
test_data = pandas.read_csv(file_name)
for cal_name in test_data:
    if cal_name == 'WorkerId':
        worker_ids += test_data[cal_name].tolist()
    if 'Answer' in cal_name:
        record = test_data[cal_name].tolist()
        if cal_name[7:] not in result_dict:
            result_dict[cal_name[7:]] = list()
        for score in record:
            if score > 0:
                result_dict[cal_name[7:]].append(score)

result_file = open('wino_annotation/nsubj_amod_annotation.txt', 'w')

with open('wino_nsubj_amod.txt', 'r') as f:
    counter = 0
    for line in f:
        counter += 1
        words = line[:-1].split('\t')
        verb = words[0]
        adjs = words[1:]
        for i, adj in enumerate(adjs):
            tmp_name = 'nsubj_amod_v' + str(counter) + '_' + str(i+1)
            if tmp_name in ['nsubj_amod_v10_4']:
                continue
            score = sum(result_dict[tmp_name])/len(result_dict[tmp_name])
            score = (score-1)*2.5
            result_file.write(verb+'\t'+adj+'\t'+str(score)+'\n')
result_file.close()
print(len(set(worker_ids)))


print('end')
