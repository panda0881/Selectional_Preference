import pandas
import os
from scipy.stats import spearmanr
import numpy


def calculate_IAA(scoring_dict, worker_ids):
    print('Start to calculate IAA1')
    IAA1_spearman_scores = list()
    for i in range(len(worker_ids)):
        for j in range(len(worker_ids)):
            if i < j:
                IAA1_spearman_scores.append(spearmanr(scoring_dict[worker_ids[i]], scoring_dict[worker_ids[j]])[0])

    print('Start to calculate IAA2')
    IAA2_spearman_scores = list()
    for i in range(len(worker_ids)):
        other_annotation = numpy.zeros([1, len(scoring_dict[worker_ids[i]])])
        for j in range(len(worker_ids)):
            if j != i:
                other_annotation += numpy.asarray(scoring_dict[worker_ids[j]])
        average_annotation = other_annotation/(len(worker_ids)-1)
        IAA2_spearman_scores.append(spearmanr(scoring_dict[worker_ids[i]], average_annotation[0].tolist())[0])
        print(worker_ids[i], spearmanr(scoring_dict[worker_ids[i]], average_annotation[0].tolist())[0])
    return sum(IAA1_spearman_scores)/len(IAA1_spearman_scores), sum(IAA2_spearman_scores)/len(IAA2_spearman_scores)


print('We are working on amod')
result_dict = dict()
worker_ids = list()
test_folder_path = 'merged_result/dobj'
all_IAA1 = list()
all_IAA2 = list()
for f_name in os.listdir(test_folder_path):
    print('We are working on file:', f_name)
    file_name = test_folder_path + '/' + f_name
    test_data = pandas.read_csv(file_name)
    tmp_worker_ids = test_data['WorkerId'].tolist()
    all_results = list()
    annotation_dict = dict()
    for worker_id in tmp_worker_ids:
        annotation_dict[worker_id] = list()
    print(len(tmp_worker_ids))
    for cal_name in test_data:
        if 'Answer' in cal_name or 'check' in cal_name:
            record = test_data[cal_name].tolist()
            invalid_labelling = False
            for score in record:
                if pandas.isnull(score):
                    # print('NA')
                    invalid_labelling = True
                if score == -1:
                    # print(-1)
                    invalid_labelling = True
                if score == 0:
                    # print(0)
                    invalid_labelling = True
            if invalid_labelling:
                # print('lalala')
                continue
            for i, score in enumerate(record):
                annotation_dict[tmp_worker_ids[i]].append(int(score))
    tmp_IAA1, tmp_IAA2 = calculate_IAA(annotation_dict, tmp_worker_ids)
    all_IAA1.append(tmp_IAA1)
    all_IAA2.append(tmp_IAA2)
    print('tmp_IAA1:', tmp_IAA1)
    print('tmp_IAA2:', tmp_IAA2)

print('Average IAA1:', sum(all_IAA1)/len(all_IAA1))
print('Average IAA2:', sum(all_IAA2)/len(all_IAA2))

print('end')
