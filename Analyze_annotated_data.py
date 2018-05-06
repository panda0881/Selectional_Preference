import pandas
import os

print('We are working on amod')
result_dict = dict()
worker_ids = list()
test_folder_path = 'merged_result/amod'
for f_name in os.listdir(test_folder_path):
    file_name = test_folder_path + '/' + f_name
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

result_file = open('amod_anotation.txt', 'w')

with open('amod_pairs.txt', 'r') as f:
    counter = 0
    for line in f:
        counter += 1
        words = line[:-1].split('\t')
        noun = words[0]
        adjs = words[1:]
        for i, adj in enumerate(adjs):
            tmp_name = 'amod_n' + str(counter) + '_' + str(i+1)
            score = sum(result_dict[tmp_name])/len(result_dict[tmp_name])
            score = (score-1)*2.5
            result_file.write(noun+'\t'+adj+'\t'+str(score)+'\n')
result_file.close()
print(len(set(worker_ids)))

print('We are working on dobj')
result_dict = dict()
test_folder_path = 'merged_result/dobj'
for f_name in os.listdir(test_folder_path):
    file_name = test_folder_path + '/' + f_name
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

result_file = open('dobj_anotation.txt', 'w')

with open('dobj_pairs.txt', 'r') as f:
    counter = 0
    for line in f:
        counter += 1
        words = line[:-1].split('\t')
        verb = words[0]
        nouns = words[1:]
        for i, noun in enumerate(nouns):
            tmp_name = 'dobj_v' + str(counter) + '_' + str(i+1)
            score = sum(result_dict[tmp_name])/len(result_dict[tmp_name])
            score = (score-1)*2.5
            result_file.write(verb+'\t'+noun+'\t'+str(score)+'\n')
result_file.close()
print(len(set(worker_ids)))

print('We are working on nsubj')
result_dict = dict()
test_folder_path = 'merged_result/nsubj'
for f_name in os.listdir(test_folder_path):
    file_name = test_folder_path + '/' + f_name
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

result_file = open('nsubj_anotation.txt', 'w')

with open('nsubj_pairs.txt', 'r') as f:
    counter = 0
    for line in f:
        counter += 1
        words = line[:-1].split('\t')
        verb = words[0]
        nouns = words[1:]
        for i, noun in enumerate(nouns):
            tmp_name = 'subj_v' + str(counter) + '_' + str(i+1)
            score = sum(result_dict[tmp_name])/len(result_dict[tmp_name])
            score = (score-1)*2.5
            result_file.write(verb+'\t'+noun+'\t'+str(score)+'\n')
result_file.close()
print(len(set(worker_ids)))

print('We are working on dobj_amod')
result_dict = dict()
test_folder_path = 'merged_result/dobj_amod'
for f_name in os.listdir(test_folder_path):
    file_name = test_folder_path + '/' + f_name
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

result_file = open('dobj_amod_anotation.txt', 'w')

with open('dobj_amod_pairs.txt', 'r') as f:
    counter = 0
    for line in f:
        counter += 1
        words = line[:-1].split('\t')
        verb = words[0]
        adjs = words[1:]
        for i, adj in enumerate(adjs):
            tmp_name = 'dobj_amod_v' + str(counter) + '_' + str(i+1)
            score = sum(result_dict[tmp_name])/len(result_dict[tmp_name])
            score = (score-1)*2.5
            result_file.write(verb+'\t'+adj+'\t'+str(score)+'\n')
result_file.close()
print(len(set(worker_ids)))

print('We are working on nsubj_amod')
result_dict = dict()
test_folder_path = 'merged_result/nsubj_amod'
for f_name in os.listdir(test_folder_path):
    file_name = test_folder_path + '/' + f_name
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

result_file = open('nsubj_amod_anotation.txt', 'w')

with open('nsubj_amod_pairs.txt', 'r') as f:
    counter = 0
    for line in f:
        counter += 1
        words = line[:-1].split('\t')
        verb = words[0]
        adjs = words[1:]
        for i, adj in enumerate(adjs):
            tmp_name = 'dobj_amod_v' + str(counter) + '_' + str(i+1)
            score = sum(result_dict[tmp_name])/len(result_dict[tmp_name])
            score = (score-1)*2.5
            result_file.write(verb+'\t'+adj+'\t'+str(score)+'\n')
result_file.close()
print(len(set(worker_ids)))


print('end')
