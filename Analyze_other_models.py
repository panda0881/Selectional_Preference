import os
import json
from scipy.stats import spearmanr


def analyze_model(model_name):
    print('We are working on model:', model_name)
    tmp_dobj_scores = list()
    with open('Other_model_result/' + model_name + '_verb_dobj_result', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            if words[2] == 'NAN':
                tmp_dobj_scores.append(0)
            else:
                tmp_dobj_scores.append(float(words[2]))
    confident_dobj_annotation = list()
    confident_dobj_scores = list()
    for i in dobj_confident_position:
        confident_dobj_annotation.append(dobj_annotations[i])
        confident_dobj_scores.append(tmp_dobj_scores[i])
    print('dobj:', spearmanr(confident_dobj_annotation, confident_dobj_scores)[0])

    tmp_nsubj_scores = list()
    with open('Other_model_result/' + model_name + '_verb_nsubj_result', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            if words[2] == 'NAN':
                tmp_nsubj_scores.append(0)
            else:
                tmp_nsubj_scores.append(float(words[2]))
    confident_nsubj_annotation = list()
    confident_nsubj_scores = list()
    for i in nsubj_confident_position:
        # if tmp_nsubj_scores[i] == 0:
        #     continue
        confident_nsubj_annotation.append(nsubj_annotations[i])
        confident_nsubj_scores.append(tmp_nsubj_scores[i])
    print('nsubj:', spearmanr(confident_nsubj_annotation, confident_nsubj_scores)[0])

    tmp_amod_scores = list()
    with open('Other_model_result/' + model_name + '_noun_amod_result', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            if words[2] == 'NAN':
                tmp_amod_scores.append(0)
            else:
                tmp_amod_scores.append(float(words[2]))
    confident_amod_annotation = list()
    confident_amod_scores = list()
    for i in amod_confident_position:
        confident_amod_annotation.append(amod_annotations[i])
        confident_amod_scores.append(tmp_amod_scores[i])
    print('amod:', spearmanr(confident_amod_annotation, confident_amod_scores)[0])

    tmp_dobj_amod_scores = list()
    if os.path.isfile('Other_model_result/' + model_name + '_verb_dobj_amod_result'):
        with open('Other_model_result/' + model_name + '_verb_dobj_amod_result', 'r') as f:
            for line in f:
                words = line[:-1].split('\t')
                if words[2] == 'NAN':
                    tmp_dobj_amod_scores.append(0)
                else:
                    tmp_dobj_amod_scores.append(float(words[2]))
        confident_dobj_amod_annotation = list()
        confident_dobj_amod_scores = list()
        for i in dobj_amod_confident_position:
            confident_dobj_amod_annotation.append(dobj_amod_annotations[i])
            confident_dobj_amod_scores.append(tmp_dobj_amod_scores[i])
        print('dobj_amod:', spearmanr(confident_dobj_amod_annotation, confident_dobj_amod_scores)[0])
    else:
        print('dobj_amod: -')

    tmp_nsubj_amod_scores = list()
    if os.path.isfile('Other_model_result/' + model_name + '_verb_nsubj_amod_result'):
        with open('Other_model_result/' + model_name + '_verb_nsubj_amod_result', 'r') as f:
            for line in f:
                words = line[:-1].split('\t')
                if words[2] == 'NAN':
                    tmp_nsubj_amod_scores.append(0)
                else:
                    tmp_nsubj_amod_scores.append(float(words[2]))
        confident_nsubj_amod_annotation = list()
        confident_nsubj_amod_scores = list()
        for i in nsubj_amod_confident_position:
            confident_nsubj_amod_annotation.append(nsubj_amod_annotations[i])
            confident_nsubj_amod_scores.append(tmp_nsubj_amod_scores[i])
        print('nsubj_amod:', spearmanr(confident_nsubj_amod_annotation, confident_nsubj_amod_scores)[0])
    else:
        print('nsubj_amod: -')


def analyze_model_by_pair(model_name):
    print('We are working on model:', model_name)
    tmp_dobj_scores = list()
    with open('Other_model_result/' + model_name + '_verb_dobj_result', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            if words[2] == 'NAN':
                tmp_dobj_scores.append(0)
            else:
                tmp_dobj_scores.append(float(words[2]))
    confident_dobj_annotation = list()
    confident_dobj_scores = list()
    tmp_annotation = list()
    tmp_score = list()
    last_predict = 0
    for i in dobj_confident_position:
        if int(i / 4) > last_predict:
            if len(tmp_annotation) > 1:
                confident_dobj_annotation.append(tmp_annotation)
                confident_dobj_scores.append(tmp_score)
            tmp_annotation = list()
            tmp_score = list()
            last_predict = int(i/4)
        tmp_annotation.append(dobj_annotations[i])
        tmp_score.append(tmp_dobj_scores[i])
    spearmans = list()
    for i in range(len(confident_dobj_annotation)):
        tmp_spearman = spearmanr(confident_dobj_annotation[i], confident_dobj_scores[i])[0]
        if tmp_spearman > -1.5:
            spearmans.append(tmp_spearman)
    print('dobj:', sum(spearmans)/len(spearmans))

    tmp_nsubj_scores = list()
    with open('Other_model_result/' + model_name + '_verb_nsubj_result', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            if words[2] == 'NAN':
                tmp_nsubj_scores.append(0)
            else:
                tmp_nsubj_scores.append(float(words[2]))
    confident_nsubj_annotation = list()
    confident_nsubj_scores = list()
    tmp_annotation = list()
    tmp_score = list()
    last_predict = 0
    for i in nsubj_confident_position:
        if int(i / 4) > last_predict:
            if len(tmp_annotation) > 1:
                confident_nsubj_annotation.append(tmp_annotation)
                confident_nsubj_scores.append(tmp_score)
            tmp_annotation = list()
            tmp_score = list()
            last_predict = int(i/4)
        tmp_annotation.append(nsubj_annotations[i])
        tmp_score.append(tmp_nsubj_scores[i])
    spearmans = list()
    for i in range(len(confident_nsubj_annotation)):
        tmp_spearman = spearmanr(confident_nsubj_annotation[i], confident_nsubj_scores[i])[0]
        if tmp_spearman > -1.5:
            spearmans.append(tmp_spearman)
    print('nsubj:', sum(spearmans)/len(spearmans))

    tmp_amod_scores = list()
    with open('Other_model_result/' + model_name + '_noun_amod_result', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            if words[2] == 'NAN':
                tmp_amod_scores.append(0)
            else:
                tmp_amod_scores.append(float(words[2]))
    confident_amod_annotation = list()
    confident_amod_scores = list()
    tmp_annotation = list()
    tmp_score = list()
    last_predict = 0
    for i in amod_confident_position:
        if int(i / 4) > last_predict:
            if len(tmp_annotation) > 1:
                confident_amod_annotation.append(tmp_annotation)
                confident_amod_scores.append(tmp_score)
            tmp_annotation = list()
            tmp_score = list()
            last_predict = int(i/4)
        tmp_annotation.append(amod_annotations[i])
        tmp_score.append(tmp_amod_scores[i])
    spearmans = list()
    for i in range(len(confident_amod_annotation)):
        tmp_spearman = spearmanr(confident_amod_annotation[i], confident_amod_scores[i])[0]
        if tmp_spearman > -1.5:
            spearmans.append(tmp_spearman)
    print('amod:', sum(spearmans)/len(spearmans))

    tmp_dobj_amod_scores = list()
    with open('Other_model_result/' + model_name + '_verb_dobj_amod_result', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            if words[2] == 'NAN':
                tmp_dobj_amod_scores.append(0)
            else:
                tmp_dobj_amod_scores.append(float(words[2]))
    confident_dobj_amod_annotation = list()
    confident_dobj_amod_scores = list()
    tmp_annotation = list()
    tmp_score = list()
    last_predict = 0
    for i in dobj_amod_confident_position:
        if int(i / 4) > last_predict:
            if len(tmp_annotation) > 1:
                confident_dobj_amod_annotation.append(tmp_annotation)
                confident_dobj_amod_scores.append(tmp_score)
            tmp_annotation = list()
            tmp_score = list()
            last_predict = int(i/4)
        tmp_annotation.append(dobj_amod_annotations[i])
        tmp_score.append(tmp_dobj_amod_scores[i])
    spearmans = list()
    for i in range(len(confident_dobj_amod_annotation)):
        tmp_spearman = spearmanr(confident_dobj_amod_annotation[i], confident_dobj_amod_scores[i])[0]
        if tmp_spearman > -1.5:
            spearmans.append(tmp_spearman)
    print('amod:', sum(spearmans)/len(spearmans))

    tmp_nsubj_amod_scores = list()
    with open('Other_model_result/' + model_name + '_verb_nsubj_amod_result', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            if words[2] == 'NAN':
                tmp_nsubj_amod_scores.append(0)
            else:
                tmp_nsubj_amod_scores.append(float(words[2]))
    confident_nsubj_amod_annotation = list()
    confident_nsubj_amod_scores = list()
    tmp_annotation = list()
    tmp_score = list()
    last_predict = 0
    for i in nsubj_amod_confident_position:
        if int(i / 4) > last_predict:
            if len(tmp_annotation) > 1:
                confident_nsubj_amod_annotation.append(tmp_annotation)
                confident_nsubj_amod_scores.append(tmp_score)
            tmp_annotation = list()
            tmp_score = list()
            last_predict = int(i/4)
        tmp_annotation.append(nsubj_amod_annotations[i])
        tmp_score.append(tmp_nsubj_amod_scores[i])
    spearmans = list()
    for i in range(len(confident_nsubj_amod_annotation)):
        tmp_spearman = spearmanr(confident_nsubj_amod_annotation[i], confident_nsubj_amod_scores[i])[0]
        if tmp_spearman > -1.5:
            spearmans.append(tmp_spearman)
    print('nsubj_amod:', sum(spearmans)/len(spearmans))


with open('confident_pairs.json', 'r') as f:
    confident_pairs = json.load(f)
with open('difficult_pairs.json', 'r') as f:
    difficult_pairs = json.load(f)

dobj_annotations = list()
dobj_confident_position = list()
with open('dobj_annotation.txt', 'r') as f:
    for line in f:
        words = line[:-1].split('\t')
        dobj_annotations.append(float(words[2]))
tmp_confident_pairs = confident_pairs['dobj']
for pair in tmp_confident_pairs:
    p_pos = int(pair.split('v')[1].split('_')[0])
    tmp = pair.split('_')
    a_pos = int(tmp[-1])
    dobj_confident_position.append((p_pos-1)*4+a_pos-1)
dobj_confident_position.sort()

nsubj_annotations = list()
nsubj_confident_position = list()
with open('nsubj_annotation.txt', 'r') as f:
    for line in f:
        words = line[:-1].split('\t')
        nsubj_annotations.append(float(words[2]))
tmp_confident_pairs = confident_pairs['nsubj']
for pair in tmp_confident_pairs:
    p_pos = int(pair.split('v')[1].split('_')[0])
    tmp = pair.split('_')
    a_pos = int(tmp[-1])
    nsubj_confident_position.append((p_pos-1)*4+a_pos-1)
nsubj_confident_position.sort()

amod_annotations = list()
amod_confident_position = list()
with open('amod_annotation.txt', 'r') as f:
    for line in f:
        words = line[:-1].split('\t')
        amod_annotations.append(float(words[2]))
tmp_confident_pairs = confident_pairs['amod']
for pair in tmp_confident_pairs:
    p_pos = int(pair.split('n')[1].split('_')[0])
    tmp = pair.split('_')
    a_pos = int(tmp[-1])
    amod_confident_position.append((p_pos-1)*4+a_pos-1)
amod_confident_position.sort()

dobj_amod_annotations = list()
dobj_amod_confident_position = list()
with open('dobj_amod_annotation.txt', 'r') as f:
    for line in f:
        words = line[:-1].split('\t')
        dobj_amod_annotations.append(float(words[2]))
tmp_confident_pairs = confident_pairs['dobj_amod']
for pair in tmp_confident_pairs:
    p_pos = int(pair.split('v')[1].split('_')[0])
    tmp = pair.split('_')
    a_pos = int(tmp[-1])
    dobj_amod_confident_position.append((p_pos-1)*4+a_pos-1)
dobj_amod_confident_position.sort()


nsubj_amod_annotations = list()
nsubj_amod_confident_position = list()
with open('nsubj_amod_annotation.txt', 'r') as f:
    for line in f:
        words = line[:-1].split('\t')
        nsubj_amod_annotations.append(float(words[2]))
tmp_confident_pairs = confident_pairs['nsubj_amod']
for pair in tmp_confident_pairs:
    p_pos = int(pair.split('v')[1].split('_')[0])
    tmp = pair.split('_')
    a_pos = int(tmp[-1])
    nsubj_amod_confident_position.append((p_pos-1)*4+a_pos-1)

nsubj_amod_confident_position.sort()

# analyze_model('depemb')
analyze_model('glove')
analyze_model('word2vec')
analyze_model('nyt')
analyze_model('yelp')
analyze_model('wiki')
analyze_model('depcontext')

# analyze_model_by_pair('depemb')
# analyze_model_by_pair('glove')
# analyze_model_by_pair('word2vec')
# analyze_model_by_pair('nyt')
# analyze_model_by_pair('yelp')
# analyze_model_by_pair('wiki')
