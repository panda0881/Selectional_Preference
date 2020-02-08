import pandas
import os
from scipy.stats import spearmanr
import numpy
import json
import pickle

question_tuples = list()
question_tuples.append(
    {'question_id': 3, 'candidate_A': ('fit', 'nsubj'), 'candidate_B': ('fit', 'dobj'), 'amod': 'small', 'answer': 'A'})
question_tuples.append(
    {'question_id': 4, 'candidate_A': ('fit', 'nsubj'), 'candidate_B': ('fit', 'dobj'), 'amod': 'large', 'answer': 'B'})
question_tuples.append(
    {'question_id': 7, 'candidate_A': ('call', 'nsubj'), 'candidate_B': ('call', 'dobj'), 'amod': 'successful', 'answer': 'A'})
question_tuples.append(
    {'question_id': 8, 'candidate_A': ('call', 'nsubj'), 'candidate_B': ('call', 'dobj'), 'amod': 'available', 'answer': 'B'})
question_tuples.append(
    {'question_id': 15, 'candidate_A': ('lift', 'nsubj'), 'candidate_B': ('lift', 'dobj'), 'amod': 'strong', 'answer': 'A'})
question_tuples.append(
    {'question_id': 16, 'candidate_A': ('lift', 'nsubj'), 'candidate_B': ('lift', 'dobj'), 'amod': 'light', 'answer': 'B'})
question_tuples.append(
    {'question_id': 19, 'candidate_A': ('see', 'nsubj'), 'candidate_B': ('NA', 'dobj'), 'amod': 'tall', 'answer': 'A'})
question_tuples.append(
    {'question_id': 20, 'candidate_A': ('see', 'nsubj'), 'candidate_B': ('NA', 'dobj'), 'amod': 'short', 'answer': 'B'})
question_tuples.append(
    {'question_id': 35, 'candidate_A': ('yell', 'nsubj'), 'candidate_B': ('yell', 'dobj'), 'amod': 'upset', 'answer': 'A'})
question_tuples.append(
    {'question_id': 36, 'candidate_A': ('comfort', 'nsubj'), 'candidate_B': ('comfort', 'dobj'), 'amod': 'upset', 'answer': 'B'})
question_tuples.append(
    {'question_id': 39, 'candidate_A': ('envy', 'nsubj'), 'candidate_B': ('envy', 'dobj'), 'amod': 'unsuccessful', 'answer': 'A'})
question_tuples.append(
    {'question_id': 40, 'candidate_A': ('envy', 'nsubj'), 'candidate_B': ('envy', 'dobj'), 'amod': 'successful', 'answer': 'B'})
question_tuples.append(
    {'question_id': 43, 'candidate_A': ('NA', 'nsubj'), 'candidate_B': ('NA', 'dobj'), 'amod': 'empty', 'answer': 'A'})
question_tuples.append(
    {'question_id': 44, 'candidate_A': ('NA', 'nsubj'), 'candidate_B': ('NA', 'dobj'), 'amod': 'full', 'answer': 'B'})
question_tuples.append(
    {'question_id': 45, 'candidate_A': ('know', 'nsubj'), 'candidate_B': ('know', 'dobj'), 'amod': 'nosy', 'answer': 'A'})
question_tuples.append(
    {'question_id': 46, 'candidate_A': ('know', 'nsubj'), 'candidate_B': ('know', 'dobj'), 'amod': 'indiscreet', 'answer': 'B'})
question_tuples.append(
    {'question_id': 51, 'candidate_A': ('beat', 'nsubj'), 'candidate_B': ('beat', 'dobj'), 'amod': 'young', 'answer': 'A'})
question_tuples.append(
    {'question_id': 52, 'candidate_A': ('beat', 'nsubj'), 'candidate_B': ('beat', 'dobj'), 'amod': 'old', 'answer': 'B'})
question_tuples.append(
    {'question_id': 71, 'candidate_A': ('take', 'dobj'), 'candidate_B': ('NA', 'dobj'), 'amod': 'handy', 'answer': 'A'})
question_tuples.append(
    {'question_id': 72, 'candidate_A': ('take', 'dobj'), 'candidate_B': ('NA', 'dobj'), 'amod': 'light', 'answer': 'B'})
question_tuples.append(
    {'question_id': 73, 'candidate_A': ('put', 'dobj'), 'candidate_B': ('NA', 'dobj'), 'amod': 'short', 'answer': 'A'})
question_tuples.append(
    {'question_id': 74, 'candidate_A': ('put', 'dobj'), 'candidate_B': ('NA', 'dobj'), 'amod': 'low', 'answer': 'B'})
question_tuples.append(
    {'question_id': 75, 'candidate_A': ('NA', 'dobj'), 'candidate_B': ('show', 'dobj'), 'amod': 'good', 'answer': 'A'})
question_tuples.append(
    {'question_id': 76, 'candidate_A': ('NA', 'dobj'), 'candidate_B': ('show', 'dobj'), 'amod': 'famous', 'answer': 'B'})
question_tuples.append(
    {'question_id': 77, 'candidate_A': ('pay', 'nsubj'), 'candidate_B': ('pay', 'dobj'), 'amod': 'generous', 'answer': 'A'})
question_tuples.append(
    {'question_id': 78, 'candidate_A': ('pay', 'nsubj'), 'candidate_B': ('pay', 'dobj'), 'amod': 'grateful', 'answer': 'B'})
question_tuples.append(
    {'question_id': 79, 'candidate_A': ('pay', 'nsubj'), 'candidate_B': ('pay', 'dobj'), 'amod': 'happy', 'answer': 'A'})
question_tuples.append(
    {'question_id': 80, 'candidate_A': ('pay', 'nsubj'), 'candidate_B': ('pay', 'dobj'), 'amod': 'grateful', 'answer': 'B'})
question_tuples.append(
    {'question_id': 87, 'candidate_A': ('sit', 'nsubj'), 'candidate_B': ('move', 'dobj'), 'amod': 'hot', 'answer': 'A'})
question_tuples.append(
    {'question_id': 88, 'candidate_A': ('sit', 'nsubj'), 'candidate_B': ('move', 'dobj'), 'amod': 'cool', 'answer': 'B'})
question_tuples.append(
    {'question_id': 89, 'candidate_A': ('wait', 'nsubj'), 'candidate_B': ('wait', 'dobj'), 'amod': 'patient', 'answer': 'A'})
question_tuples.append(
    {'question_id': 90, 'candidate_A': ('wait', 'nsubj'), 'candidate_B': ('wait', 'dobj'), 'amod': 'cautious', 'answer': 'B'})
question_tuples.append(
    {'question_id': 97, 'candidate_A': ('eat', 'nsubj'), 'candidate_B': ('eat', 'dobj'), 'amod': 'hungry', 'answer': 'A'})
question_tuples.append(
    {'question_id': 98, 'candidate_A': ('eat', 'nsubj'), 'candidate_B': ('eat', 'dobj'), 'amod': 'tasty', 'answer': 'B'})
question_tuples.append(
    {'question_id': 107, 'candidate_A': ('research', 'nsubj'), 'candidate_B': ('hum', 'nsubj'), 'amod': 'annoyed', 'answer': 'A'})
question_tuples.append(
    {'question_id': 108, 'candidate_A': ('research', 'nsubj'), 'candidate_B': ('hum', 'nsubj'), 'amod': 'annoying', 'answer': 'B'})
question_tuples.append(
    {'question_id': 109, 'candidate_A': ('see', 'nsubj'), 'candidate_B': ('see', 'dobj'), 'amod': 'impressed', 'answer': 'A'})
question_tuples.append(
    {'question_id': 110, 'candidate_A': ('see', 'nsubj'), 'candidate_B': ('see', 'dobj'), 'amod': 'impressive', 'answer': 'B'})
question_tuples.append(
    {'question_id': 111, 'candidate_A': ('collapse', 'nsubj'), 'candidate_B': ('help', 'nsubj'), 'amod': 'ill', 'answer': 'A'})
question_tuples.append(
    {'question_id': 112, 'candidate_A': ('collapse', 'nsubj'), 'candidate_B': ('help', 'nsubj'), 'amod': 'concerned', 'answer': 'B'})
question_tuples.append(
    {'question_id': 119, 'candidate_A': ('read', 'nsubj'), 'candidate_B': ('read', 'dobj'), 'amod': 'gripped', 'answer': 'A'})
question_tuples.append(
    {'question_id': 120, 'candidate_A': ('read', 'nsubj'), 'candidate_B': ('read', 'dobj'), 'amod': 'popular', 'answer': 'B'})
question_tuples.append(
    {'question_id': 131, 'candidate_A': ('knock', 'nsubj'), 'candidate_B': ('knock', 'dobj'), 'amod': 'disappointed', 'answer': 'A'})
question_tuples.append(
    {'question_id': 132, 'candidate_A': ('knock', 'nsubj'), 'candidate_B': ('knock', 'dobj'), 'amod': 'out', 'answer': 'B'})
# question_tuples.append(
#     {'question_id': 139, 'candidate_A': ('cover', 'dobj'), 'candidate_B': ('cover', 'nsubj'), 'amod': 'in', 'answer': 'A'})
# question_tuples.append(
#     {'question_id': 140, 'candidate_A': ('cover', 'dobj'), 'candidate_B': ('cover', 'nsubj'), 'amod': 'here', 'answer': 'B'})
question_tuples.append(
    {'question_id': 147, 'candidate_A': ('have', 'nsubj'), 'candidate_B': ('have', 'dobj'), 'amod': 'prepared', 'answer': 'A'})
question_tuples.append(
    {'question_id': 148, 'candidate_A': ('have', 'nsubj'), 'candidate_B': ('have', 'dobj'), 'amod': 'enough', 'answer': 'B'})
question_tuples.append(
    {'question_id': 150, 'candidate_A': ('visit', 'nsubj'), 'candidate_B': ('visit', 'dobj'), 'amod': 'dead', 'answer': 'B'})
question_tuples.append(
    {'question_id': 153, 'candidate_A': ('cut', 'dobj'), 'candidate_B': ('NA', 'dobj'), 'amod': 'thin', 'answer': 'A'})
question_tuples.append(
    {'question_id': 154, 'candidate_A': ('cut', 'dobj'), 'candidate_B': ('NA', 'dobj'), 'amod': 'large', 'answer': 'B'})
question_tuples.append(
    {'question_id': 157, 'candidate_A': ('attack', 'nsubj'), 'candidate_B': ('attack', 'dobj'), 'amod': 'bold', 'answer': 'A'})
question_tuples.append(
    {'question_id': 158, 'candidate_A': ('attack', 'nsubj'), 'candidate_B': ('attack', 'dobj'), 'amod': 'nervous', 'answer': 'B'})
question_tuples.append(
    {'question_id': 171, 'candidate_A': ('declare', 'nsubj'), 'candidate_B': ('declare', 'dobj'), 'amod': 'defeated', 'answer': 'A'})
question_tuples.append(
    {'question_id': 172, 'candidate_A': ('declare', 'nsubj'), 'candidate_B': ('declare', 'dobj'), 'amod': 'victorious', 'answer': 'B'})
question_tuples.append(
    {'question_id': 179, 'candidate_A': ('interview', 'nsubj'), 'candidate_B': ('interview', 'dobj'), 'amod': 'persistent', 'answer': 'A'})
question_tuples.append(
    {'question_id': 180, 'candidate_A': ('interview', 'nsubj'), 'candidate_B': ('interview', 'dobj'), 'amod': 'cooperative', 'answer': 'B'})
question_tuples.append(
    {'question_id': 185, 'candidate_A': ('break', 'dobj'), 'candidate_B': ('NA', 'dobj'), 'amod': 'good', 'answer': 'A'})
question_tuples.append(
    {'question_id': 186, 'candidate_A': ('break', 'dobj'), 'candidate_B': ('NA', 'dobj'), 'amod': 'unnecessary', 'answer': 'B'})
question_tuples.append(
    {'question_id': 199, 'candidate_A': ('fit', 'nsubj'), 'candidate_B': ('fit', 'dobj'), 'amod': 'narrow', 'answer': 'A'})
question_tuples.append(
    {'question_id': 200, 'candidate_A': ('fit', 'nsubj'), 'candidate_B': ('fit', 'dobj'), 'amod': 'wide', 'answer': 'B'})
question_tuples.append(
    {'question_id': 227, 'candidate_A': ('pass', 'nsubj'), 'candidate_B': ('NA', 'dobj'), 'amod': 'full', 'answer': 'A'})
question_tuples.append(
    {'question_id': 228, 'candidate_A': ('pass', 'nsubj'), 'candidate_B': ('NA', 'dobj'), 'amod': 'hungry', 'answer': 'B'})
question_tuples.append(
    {'question_id': 247, 'candidate_A': ('find', 'nsubj'), 'candidate_B': ('find', 'dobj'), 'amod': 'furious', 'answer': 'A'})
question_tuples.append(
    {'question_id': 248, 'candidate_A': ('find', 'nsubj'), 'candidate_B': ('find', 'dobj'), 'amod': 'embarrassed', 'answer': 'B'})
question_tuples.append(
    {'question_id': 251, 'candidate_A': ('stop', 'nsubj'), 'candidate_B': ('stop', 'dobj'), 'amod': 'compassionate', 'answer': 'A'})
question_tuples.append(
    {'question_id': 252, 'candidate_A': ('stop', 'nsubj'), 'candidate_B': ('stop', 'dobj'), 'amod': 'cruel', 'answer': 'B'})
question_tuples.append(
    {'question_id': 256, 'candidate_A': ('give', 'nsubj'), 'candidate_B': ('give', 'dobj'), 'amod': 'plump', 'answer': 'A'})
question_tuples.append(
    {'question_id': 257, 'candidate_A': ('give', 'nsubj'), 'candidate_B': ('give', 'dobj'), 'amod': 'hungry', 'answer': 'B'})
question_tuples.append(
    {'question_id': 262, 'candidate_A': ('cede', 'nsubj'), 'candidate_B': ('cede', 'dobj'), 'amod': 'unpopular', 'answer': 'A'})
question_tuples.append(
    {'question_id': 263, 'candidate_A': ('cede', 'nsubj'), 'candidate_B': ('cede', 'dobj'), 'amod': 'popular', 'answer': 'B'})
question_tuples.append(
    {'question_id': 265, 'candidate_A': ('pass', 'nsubj'), 'candidate_B': ('pass', 'dobj'), 'amod': 'open', 'answer': 'B'})
question_tuples.append(
    {'question_id': 282, 'candidate_A': ('figure', 'nsubj'), 'candidate_B': ('figure', 'dobj'), 'amod': 'smart', 'answer': 'A'})
question_tuples.append(
    {'question_id': 283, 'candidate_A': ('figure', 'nsubj'), 'candidate_B': ('figure', 'dobj'), 'amod': 'simple', 'answer': 'B'})

nsubj_amod_result = dict()
with open('nsubj_amod_annotation.txt', 'r') as f:
    for line in f:
        tmp_words = line[:-1].split('\t')
        if tmp_words[0] not in nsubj_amod_result:
            nsubj_amod_result[tmp_words[0]] = dict()
        nsubj_amod_result[tmp_words[0]][tmp_words[1]] = float(tmp_words[2])
dobj_amod_result = dict()
with open('dobj_amod_annotation.txt', 'r') as f:
    for line in f:
        tmp_words = line[:-1].split('\t')
        if tmp_words[0] not in dobj_amod_result:
            dobj_amod_result[tmp_words[0]] = dict()
        dobj_amod_result[tmp_words[0]][tmp_words[1]] = float(tmp_words[2])



correct_counter = 0
wrong_counter = 0
NA_counter = 0

print('finish loading data...')


nsubj_amod_dict = dict()
dobj_amod_dict = dict()

for tmp_example in question_tuples:

    if tmp_example['candidate_A'][1] == 'nsubj':
        if tmp_example['candidate_A'][0] not in nsubj_amod_dict:
            nsubj_amod_dict[tmp_example['candidate_A'][0]] = list()
        nsubj_amod_dict[tmp_example['candidate_A'][0]].append(tmp_example['amod'])
    else:
        if tmp_example['candidate_A'][0] not in dobj_amod_dict:
            dobj_amod_dict[tmp_example['candidate_A'][0]] = list()
        dobj_amod_dict[tmp_example['candidate_A'][0]].append(tmp_example['amod'])
    if tmp_example['candidate_B'][1] == 'nsubj':
        if tmp_example['candidate_B'][0] not in nsubj_amod_dict:
            nsubj_amod_dict[tmp_example['candidate_B'][0]] = list()
        nsubj_amod_dict[tmp_example['candidate_B'][0]].append(tmp_example['amod'])
    else:
        if tmp_example['candidate_B'][0] not in dobj_amod_dict:
            dobj_amod_dict[tmp_example['candidate_B'][0]] = list()
        dobj_amod_dict[tmp_example['candidate_B'][0]].append(tmp_example['amod'])

with open('wino_nsubj_amod.txt', 'w') as f:
    for v in nsubj_amod_dict:
        if v == 'NA':
            continue
        f.write(v)
        for n in nsubj_amod_dict[v]:
            f.write('\t')
            f.write(n)
        f.write('\n')

with open('wino_dobj_amod.txt', 'w') as f:
    for v in dobj_amod_dict:
        if v == 'NA':
            continue
        f.write(v)
        for n in dobj_amod_dict[v]:
            f.write('\t')
            f.write(n)
        f.write('\n')

print('end')
