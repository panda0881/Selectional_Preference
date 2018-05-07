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
        # print(scoring_dict[worker_ids[i]])
        # print(average_annotation[0].tolist())
        print(worker_ids[i], spearmanr(scoring_dict[worker_ids[i]], average_annotation[0].tolist())[0])
    return sum(IAA1_spearman_scores)/len(IAA1_spearman_scores), sum(IAA2_spearman_scores)/len(IAA2_spearman_scores)

current_edge_type = 'nsubj_amod'
print('We are working on', current_edge_type)
result_dict = dict()
worker_ids = list()
test_folder_path = 'merged_result/' + current_edge_type
overall_confident_IAA1 = list()
overall_confident_IAA2 = list()
overall_difficult_IAA1 = list()
overall_difficult_IAA2 = list()
overall_all_IAA1 = list()
overall_all_IAA2 = list()
variance_dict = dict()
for f_name in os.listdir(test_folder_path):

    file_name = test_folder_path + '/' + f_name
    test_data = pandas.read_csv(file_name)
    for cal_name in test_data:
        if 'Answer' in cal_name and 'check' not in cal_name:
            record = test_data[cal_name].tolist()
            invalid_labelling = False
            tmp_scoring = list()
            for score in record:
                if pandas.isnull(score):
                    # print('NA')
                    invalid_labelling = True
                else:
                    if score == -1:
                        # print(-1)
                        invalid_labelling = True
                    elif score == 0:
                        # print(0)
                        invalid_labelling = True
                    else:
                        tmp_scoring.append(int(score))
            variance_dict[cal_name] = numpy.var(tmp_scoring)

annotation_variance = pandas.Series(variance_dict)
annotation_variance.sort()
# print(annotation_variance)

confident_ids = annotation_variance.index.tolist()[:1000]
difficult_ids = annotation_variance.index.tolist()[1000:]


for f_name in os.listdir(test_folder_path):
    # f_name = 'v225_.csv'
    print('We are working on file:', f_name)
    file_name = test_folder_path + '/' + f_name
    test_data = pandas.read_csv(file_name)
    tmp_worker_ids = test_data['WorkerId'].tolist()
    all_results = list()
    confident_annotation_dict = dict()
    difficult_annotation_dict = dict()
    all_annotation_dict = dict()
    for worker_id in tmp_worker_ids:
        confident_annotation_dict[worker_id] = list()
        difficult_annotation_dict[worker_id] = list()
        all_annotation_dict[worker_id] = list()
    print(len(tmp_worker_ids))
    for cal_name in test_data:
        if 'Answer' in cal_name:
            record = test_data[cal_name].tolist()
            invalid_labelling = False
            tmp_scoring = list()
            for score in record:
                if pandas.isnull(score):
                    # print('NA')
                    invalid_labelling = True
                else:
                    if score == -1:
                        # print(-1)
                        invalid_labelling = True
                    elif score == 0:
                        # print(0)
                        invalid_labelling = True
                    else:
                        tmp_scoring.append(int(score))
            variance_dict[cal_name] = numpy.var(tmp_scoring)
            if invalid_labelling:
                # print('lalala')
                continue
            if cal_name in confident_ids:
                for i, score in enumerate(record):
                    confident_annotation_dict[tmp_worker_ids[i]].append(int(score))
            else:
                for i, score in enumerate(record):
                    difficult_annotation_dict[tmp_worker_ids[i]].append(int(score))
            for i, score in enumerate(record):
                all_annotation_dict[tmp_worker_ids[i]].append(int(score))
    print('Confident:')
    tmp_confident_IAA1, tmp_confident_IAA2 = calculate_IAA(confident_annotation_dict, tmp_worker_ids)
    print('Difficult:')
    tmp_difficult_IAA1, tmp_difficult_IAA2 = calculate_IAA(difficult_annotation_dict, tmp_worker_ids)
    print('All:')
    tmp_all_IAA1, tmp_all_IAA2 = calculate_IAA(all_annotation_dict, tmp_worker_ids)
    overall_confident_IAA1.append(tmp_confident_IAA1)
    overall_confident_IAA2.append(tmp_confident_IAA2)
    overall_difficult_IAA1.append(tmp_difficult_IAA1)
    overall_difficult_IAA2.append(tmp_difficult_IAA2)
    overall_all_IAA1.append(tmp_all_IAA1)
    overall_all_IAA2.append(tmp_all_IAA2)
    print('tmp confident IAA1:', tmp_confident_IAA1)
    print('tmp confident IAA2:', tmp_confident_IAA2)
    print('tmp difficult IAA1:', tmp_difficult_IAA1)
    print('tmp difficult IAA2:', tmp_difficult_IAA2)
    print('tmp all IAA1:', tmp_all_IAA1)
    print('tmp all IAA2:', tmp_all_IAA2)

print('Average confident IAA1:', sum(overall_confident_IAA1)/len(overall_confident_IAA1))
print('Average confident IAA2:', sum(overall_confident_IAA2)/len(overall_confident_IAA2))
print('Average difficult IAA1:', sum(overall_difficult_IAA1)/len(overall_difficult_IAA1))
print('Average difficult IAA2:', sum(overall_difficult_IAA2)/len(overall_difficult_IAA2))
print('Average all IAA1:', sum(overall_all_IAA1)/len(overall_all_IAA1))
print('Average all IAA2:', sum(overall_all_IAA2)/len(overall_all_IAA2))

print('end')
