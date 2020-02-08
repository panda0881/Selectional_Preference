import json
import os
import numpy as np


def loadGloveModel(gloveFile):
    print ("Loading Glove Model")
    f = open(gloveFile,'r')
    model = {}
    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        try:
            embedding = np.array([float(val) for val in splitLine[1:]])
            model[word] = embedding
        except:
            print('invalid embedding')
    print ("Done.",len(model)," words loaded!")
    return model


def evaluate_dataset_pp(dataset_name, verb_dobj_dict, verb_nsubj_dict, noun_amod_dict, verb_dobj_amod_dict, verb_nsubj_amod_dict):
    print('We are working on dobj')
    SP_pairs = list()
    Plausibility_score = list()
    natural_frequency = list()
    with open('dobj_annotation.txt', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            SP_pairs.append((words[0], words[1]))
            Plausibility_score.append(float(words[2]))
            total_number = 0
            if words[0] not in verb_dobj_dict:
                natural_frequency.append(0)
            else:
                for noun in verb_dobj_dict[words[0]]:
                    total_number += verb_dobj_dict[words[0]][noun]
                if words[1] not in verb_dobj_dict[words[0]]:
                    natural_frequency.append(0)
                else:
                    natural_frequency.append(verb_dobj_dict[words[0]][words[1]]/total_number)
    dobj_result_file = open('pp_result/' + dataset_name + '_pp_verb_dobj_result', 'w')
    with open('dobj_annotation.txt', 'r') as f:
        counter = 0
        for line in f:
            words = line[:-1].split('\t')
            dobj_result_file.write(words[0]+'\t'+words[1]+'\t'+str(natural_frequency[counter])+'\n')
            counter += 1
    dobj_result_file.close()

    print('We are working on nsubj')
    SP_pairs = list()
    Plausibility_score = list()
    natural_frequency = list()
    with open('nsubj_annotation.txt', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            SP_pairs.append((words[0], words[1]))
            Plausibility_score.append(float(words[2]))
            total_number = 0
            if words[0] not in verb_nsubj_dict:
                natural_frequency.append(0)
            else:
                for noun in verb_nsubj_dict[words[0]]:
                    total_number += verb_nsubj_dict[words[0]][noun]
                if words[1] not in verb_nsubj_dict[words[0]]:
                    natural_frequency.append(0)
                else:
                    natural_frequency.append(verb_nsubj_dict[words[0]][words[1]]/total_number)

    nsubj_result_file = open('pp_result/' + dataset_name + '_pp_verb_nsubj_result', 'w')
    with open('nsubj_annotation.txt', 'r') as f:
        counter = 0
        for line in f:
            words = line[:-1].split('\t')
            nsubj_result_file.write(words[0]+'\t'+words[1]+'\t'+str(natural_frequency[counter])+'\n')
            counter += 1
    nsubj_result_file.close()

    print('We are working on amod')
    SP_pairs = list()
    Plausibility_score = list()
    natural_frequency = list()
    with open('amod_annotation.txt', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            SP_pairs.append((words[0], words[1]))
            Plausibility_score.append(float(words[2]))
            total_number = 0
            if words[0] not in noun_amod_dict:
                natural_frequency.append(0)
            else:
                for adj in noun_amod_dict[words[0]]:
                    total_number += noun_amod_dict[words[0]][adj]
                if words[1] not in noun_amod_dict[words[0]]:
                    natural_frequency.append(0)
                else:
                    natural_frequency.append(noun_amod_dict[words[0]][words[1]]/total_number)

    amod_result_file = open('pp_result/' + dataset_name + '_pp_noun_amod_result', 'w')
    with open('amod_annotation.txt', 'r') as f:
        counter = 0
        for line in f:
            words = line[:-1].split('\t')
            amod_result_file.write(words[0]+'\t'+words[1]+'\t'+str(natural_frequency[counter])+'\n')
            counter += 1
    amod_result_file.close()

    print('We are working on dobj_amod')
    SP_pairs = list()
    Plausibility_score = list()
    natural_frequency = list()
    with open('dobj_amod_annotation.txt', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            SP_pairs.append((words[0], words[1]))
            Plausibility_score.append(float(words[2]))
            total_number = 0
            if words[0] not in verb_dobj_amod_dict:
                natural_frequency.append(0)
            else:
                for adj in verb_dobj_amod_dict[words[0]]:
                    total_number += verb_dobj_amod_dict[words[0]][adj]
                if words[1] not in verb_dobj_amod_dict[words[0]]:
                    natural_frequency.append(0)
                else:
                    natural_frequency.append(verb_dobj_amod_dict[words[0]][words[1]]/total_number)

    dobj_amod_result_file = open('pp_result/' + dataset_name + '_pp_verb_dobj_amod_result', 'w')
    with open('dobj_amod_annotation.txt', 'r') as f:
        counter = 0
        for line in f:
            words = line[:-1].split('\t')
            dobj_amod_result_file.write(words[0]+'\t'+words[1]+'\t'+str(natural_frequency[counter])+'\n')
            counter += 1
    dobj_amod_result_file.close()

    print('We are working on nsubj_amod')
    SP_pairs = list()
    Plausibility_score = list()
    natural_frequency = list()
    with open('nsubj_amod_annotation.txt', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            SP_pairs.append((words[0], words[1]))
            Plausibility_score.append(float(words[2]))
            total_number = 0
            if words[0] not in verb_nsubj_amod_dict:
                natural_frequency.append(0)
            else:
                for adj in verb_nsubj_amod_dict[words[0]]:
                    total_number += verb_nsubj_amod_dict[words[0]][adj]
                if words[1] not in verb_nsubj_amod_dict[words[0]]:
                    natural_frequency.append(0)
                else:
                    natural_frequency.append(verb_nsubj_amod_dict[words[0]][words[1]]/total_number)

    nsubj_amod_result_file = open('pp_result/' + dataset_name + '_pp_verb_nsubj_amod_result', 'w')
    with open('nsubj_amod_annotation.txt', 'r') as f:
        counter = 0
        for line in f:
            words = line[:-1].split('\t')
            nsubj_amod_result_file.write(words[0]+'\t'+words[1]+'\t'+str(natural_frequency[counter])+'\n')
            counter += 1
    nsubj_amod_result_file.close()


def evaluate_dataset_ds(dataset_name, verb_dobj_dict, verb_nsubj_dict, noun_amod_dict, verb_dobj_amod_dict, verb_nsubj_amod_dict):
    print('We are working on dobj')
    SP_pairs = list()
    Plausibility_score = list()
    natural_frequency = list()
    with open('dobj_annotation.txt', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            SP_pairs.append((words[0], words[1]))
            Plausibility_score.append(float(words[2]))
            if words[0] not in verb_dobj_dict:
                natural_frequency.append(0)
            else:
                total_number = 0
                for noun in verb_dobj_dict[words[0]]:
                    if noun in glove_model:
                        total_number += verb_dobj_dict[words[0]][noun]
                if words[1] not in glove_model:
                    natural_frequency.append(0)
                else:
                    v1 = glove_model[words[1]]
                    tmp_similarity = 0
                    for noun in verb_dobj_dict[words[0]]:
                        if noun in glove_model:
                            v2 = glove_model[noun]
                            tmp_similarity += verb_dobj_dict[words[0]][noun]*np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
                    natural_frequency.append(tmp_similarity/total_number)
    dobj_result_file = open('ds_result/' + dataset_name + '_ds_verb_dobj_result', 'w')
    with open('dobj_annotation.txt', 'r') as f:
        counter = 0
        for line in f:
            words = line[:-1].split('\t')
            dobj_result_file.write(words[0]+'\t'+words[1]+'\t'+str(natural_frequency[counter])+'\n')
            counter += 1
    dobj_result_file.close()

    print('We are working on nsubj')
    SP_pairs = list()
    Plausibility_score = list()
    natural_frequency = list()
    with open('nsubj_annotation.txt', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            SP_pairs.append((words[0], words[1]))
            Plausibility_score.append(float(words[2]))
            if words[0] not in verb_nsubj_dict:
                natural_frequency.append(0)
            else:
                total_number = 0
                for noun in verb_nsubj_dict[words[0]]:
                    if noun in glove_model:
                        total_number += verb_nsubj_dict[words[0]][noun]
                if words[1] not in glove_model:
                    natural_frequency.append(0)
                else:
                    v1 = glove_model[words[1]]
                    tmp_similarity = 0
                    for noun in verb_nsubj_dict[words[0]]:
                        if noun in glove_model:
                            v2 = glove_model[noun]
                            tmp_similarity += verb_nsubj_dict[words[0]][noun]*np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
                    natural_frequency.append(tmp_similarity/total_number)

    nsubj_result_file = open('ds_result/' + dataset_name + '_ds_verb_nsubj_result', 'w')
    with open('nsubj_annotation.txt', 'r') as f:
        counter = 0
        for line in f:
            words = line[:-1].split('\t')
            nsubj_result_file.write(words[0]+'\t'+words[1]+'\t'+str(natural_frequency[counter])+'\n')
            counter += 1
    nsubj_result_file.close()

    print('We are working on amod')
    SP_pairs = list()
    Plausibility_score = list()
    natural_frequency = list()
    with open('amod_annotation.txt', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            SP_pairs.append((words[0], words[1]))
            Plausibility_score.append(float(words[2]))
            if words[0] not in noun_amod_dict:
                natural_frequency.append(0)
            else:
                total_number = 0
                for adj in noun_amod_dict[words[0]]:
                    if adj in glove_model:
                        total_number += noun_amod_dict[words[0]][adj]
                if words[1] not in glove_model:
                    natural_frequency.append(0)
                else:
                    tmp_similarity = 0
                    v1 = glove_model[words[1]]
                    for adj in noun_amod_dict[words[0]]:
                        if adj in glove_model:
                            v2 = glove_model[adj]
                            tmp_similarity += noun_amod_dict[words[0]][adj]*np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
                    natural_frequency.append(tmp_similarity/total_number)

    amod_result_file = open('ds_result/' + dataset_name + '_ds_noun_amod_result', 'w')
    with open('amod_annotation.txt', 'r') as f:
        counter = 0
        for line in f:
            words = line[:-1].split('\t')
            amod_result_file.write(words[0]+'\t'+words[1]+'\t'+str(natural_frequency[counter])+'\n')
            counter += 1
    amod_result_file.close()

    print('We are working on dobj_amod')
    SP_pairs = list()
    Plausibility_score = list()
    natural_frequency = list()
    with open('dobj_amod_annotation.txt', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            SP_pairs.append((words[0], words[1]))
            Plausibility_score.append(float(words[2]))
            if words[0] not in verb_dobj_amod_dict:
                natural_frequency.append(0)
            else:
                total_number = 0
                for adj in verb_dobj_amod_dict[words[0]]:
                    if adj in glove_model:
                        total_number += verb_dobj_amod_dict[words[0]][adj]
                if words[1] not in glove_model:
                    natural_frequency.append(0)
                else:
                    tmp_similarity = 0
                    v1 = glove_model[words[1]]
                    for adj in verb_dobj_amod_dict[words[0]]:
                        if adj in glove_model:
                            v2 = glove_model[adj]
                            tmp_similarity += verb_dobj_amod_dict[words[0]][adj]*np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
                    natural_frequency.append(tmp_similarity/total_number)

    dobj_amod_result_file = open('ds_result/' + dataset_name + '_ds_verb_dobj_amod_result', 'w')
    with open('dobj_amod_annotation.txt', 'r') as f:
        counter = 0
        for line in f:
            words = line[:-1].split('\t')
            dobj_amod_result_file.write(words[0]+'\t'+words[1]+'\t'+str(natural_frequency[counter])+'\n')
            counter += 1
    dobj_amod_result_file.close()

    print('We are working on nsubj_amod')
    SP_pairs = list()
    Plausibility_score = list()
    natural_frequency = list()
    with open('nsubj_amod_annotation.txt', 'r') as f:
        for line in f:
            words = line[:-1].split('\t')
            SP_pairs.append((words[0], words[1]))
            Plausibility_score.append(float(words[2]))
            if words[0] not in verb_nsubj_amod_dict:
                natural_frequency.append(0)
            else:
                total_number = 0
                for adj in verb_nsubj_amod_dict[words[0]]:
                    if adj in glove_model:
                        total_number += verb_nsubj_amod_dict[words[0]][adj]
                if words[1] not in glove_model:
                    natural_frequency.append(0)
                else:
                    tmp_similarity = 0
                    v1 = glove_model[words[1]]
                    for adj in verb_nsubj_amod_dict[words[0]]:
                        if adj in glove_model:
                            v2 = glove_model[adj]
                            tmp_similarity += verb_nsubj_amod_dict[words[0]][adj]*np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
                    natural_frequency.append(tmp_similarity/total_number)

    nsubj_amod_result_file = open('ds_result/' + dataset_name + '_ds_verb_nsubj_amod_result', 'w')
    with open('nsubj_amod_annotation.txt', 'r') as f:
        counter = 0
        for line in f:
            words = line[:-1].split('\t')
            nsubj_amod_result_file.write(words[0]+'\t'+words[1]+'\t'+str(natural_frequency[counter])+'\n')
            counter += 1
    nsubj_amod_result_file.close()

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

glove_model = loadGloveModel('/home/data/corpora/english_embeddings/glove/glove.840B.300d.txt')

print('Start to work on pp')
print('We are working on wiki')
evaluate_dataset_pp('wiki', wiki_verb_dobj_dict, wiki_verb_nsubj_dict, wiki_noun_amod_dict, wiki_verb_dobj_amod_dict, wiki_verb_nsubj_amod_dict)
print('We are working on yelp')
evaluate_dataset_pp('yelp', yelp_verb_dobj_dict, yelp_verb_nsubj_dict, yelp_noun_amod_dict, yelp_verb_dobj_amod_dict, yelp_verb_nsubj_amod_dict)
print('We are working on nyt')
evaluate_dataset_pp('nyt', nyt_verb_dobj_dict, nyt_verb_nsubj_dict, nyt_noun_amod_dict, nyt_verb_dobj_amod_dict, nyt_verb_nsubj_amod_dict)

print('Start to work on ds')
print('We are working on wiki')
evaluate_dataset_ds('wiki', wiki_verb_dobj_dict, wiki_verb_nsubj_dict, wiki_noun_amod_dict, wiki_verb_dobj_amod_dict, wiki_verb_nsubj_amod_dict)
print('We are working on yelp')
evaluate_dataset_ds('yelp', yelp_verb_dobj_dict, yelp_verb_nsubj_dict, yelp_noun_amod_dict, yelp_verb_dobj_amod_dict, yelp_verb_nsubj_amod_dict)
print('We are working on nyt')
evaluate_dataset_ds('nyt', nyt_verb_dobj_dict, nyt_verb_nsubj_dict, nyt_noun_amod_dict, nyt_verb_dobj_amod_dict, nyt_verb_nsubj_amod_dict)


