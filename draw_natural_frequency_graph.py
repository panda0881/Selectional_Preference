import json
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

with open('natural_frequency_result.json', 'r') as f:
    data = json.load(f)

with open('confident_pairs.json', 'r') as f:
    confident_pairs = json.load(f)
with open('difficult_pairs.json', 'r') as f:
    difficult_pairs = json.load(f)


# print('We are working on dobj')
# tmp_confident_pairs = confident_pairs['dobj']
# tmp_difficult_pairs = difficult_pairs['dobj']
# tmp_confident_position = list()
# for pair in tmp_confident_pairs:
#     p_pos = int(pair.split('v')[1].split('_')[0])
#     tmp = pair.split('_')
#     a_pos = int(tmp[-1])
#     tmp_confident_position.append((p_pos-1)*4+a_pos-1)
# annotation = data['dobj']['annotation']
# frequency = data['dobj']['frequency']
# confident_annotation = list()
# confident_frequency = list()
# difficult_annotation = list()
# difficult_frequency = list()
# for i in range(len(annotation)):
#     if i in tmp_confident_position:
#         confident_annotation.append(annotation[i])
#         confident_frequency.append(frequency[i])
#     else:
#         difficult_annotation.append(annotation[i])
#         difficult_frequency.append(frequency[i])


# print('We are working on nsubj')
# tmp_confident_pairs = confident_pairs['nsubj']
# tmp_difficult_pairs = difficult_pairs['nsubj']
# tmp_confident_position = list()
# for pair in tmp_confident_pairs:
#     p_pos = int(pair.split('v')[1].split('_')[0])
#     tmp = pair.split('_')
#     a_pos = int(tmp[-1])
#     tmp_confident_position.append((p_pos-1)*4+a_pos-1)
# annotation = data['nsubj']['annotation']
# frequency = data['nsubj']['frequency']
# confident_annotation = list()
# confident_frequency = list()
# difficult_annotation = list()
# difficult_frequency = list()
# for i in range(len(annotation)):
#     if i in tmp_confident_position:
#         confident_annotation.append(annotation[i])
#         confident_frequency.append(frequency[i])
#     else:
#         difficult_annotation.append(annotation[i])
#         difficult_frequency.append(frequency[i])
#


# print('We are working on amod')
# tmp_confident_pairs = confident_pairs['amod']
# tmp_difficult_pairs = difficult_pairs['amod']
# tmp_confident_position = list()
# for pair in tmp_confident_pairs:
#     p_pos = int(pair.split('n')[1].split('_')[0])
#     tmp = pair.split('_')
#     a_pos = int(tmp[-1])
#     tmp_confident_position.append((p_pos-1)*4+a_pos-1)
# annotation = data['amod']['annotation']
# frequency = data['amod']['frequency']
# confident_annotation = list()
# confident_frequency = list()
# difficult_annotation = list()
# difficult_frequency = list()
# for i in range(len(annotation)):
#     if i in tmp_confident_position:
#         confident_annotation.append(annotation[i])
#         confident_frequency.append(frequency[i])
#     else:
#         difficult_annotation.append(annotation[i])
#         difficult_frequency.append(frequency[i])


#
# print('We are working on dobj_amod')
# tmp_confident_pairs = confident_pairs['dobj_amod']
# tmp_difficult_pairs = difficult_pairs['dobj_amod']
# tmp_confident_position = list()
# for pair in tmp_confident_pairs:
#     p_pos = int(pair.split('v')[1].split('_')[0])
#     tmp = pair.split('_')
#     a_pos = int(tmp[-1])
#     tmp_confident_position.append((p_pos-1)*4+a_pos-1)
# annotation = data['dobj_amod']['annotation']
# frequency = data['dobj_amod']['frequency']
# confident_annotation = list()
# confident_frequency = list()
# difficult_annotation = list()
# difficult_frequency = list()
# for i in range(len(annotation)):
#     if i in tmp_confident_position:
#         confident_annotation.append(annotation[i])
#         confident_frequency.append(frequency[i])
#     else:
#         difficult_annotation.append(annotation[i])
#         difficult_frequency.append(frequency[i])

# print('We are working on nsubj_amod')
tmp_confident_pairs = confident_pairs['nsubj_amod']
tmp_difficult_pairs = difficult_pairs['nsubj_amod']
tmp_confident_position = list()
for pair in tmp_confident_pairs:
    p_pos = int(pair.split('v')[1].split('_')[0])
    tmp = pair.split('_')
    a_pos = int(tmp[-1])
    tmp_confident_position.append((p_pos-1)*4+a_pos-1)
annotation = data['nsubj_amod']['annotation']
frequency = data['nsubj_amod']['frequency']
confident_annotation = list()
confident_frequency = list()
difficult_annotation = list()
difficult_frequency = list()
for i in range(len(annotation)):
    if i in tmp_confident_position:
        confident_annotation.append(annotation[i])
        confident_frequency.append(frequency[i])
    else:
        difficult_annotation.append(annotation[i])
        difficult_frequency.append(frequency[i])



print('spearman:', spearmanr(annotation, frequency)[0])
print('confident spearman:', spearmanr(confident_annotation, confident_frequency)[0])
print('difficult spearman:', spearmanr(difficult_annotation, difficult_frequency)[0])

fig = plt.figure()
ax = plt.gca()
ax.scatter(x=confident_frequency, y=confident_annotation, c='b', s=2)
ax.scatter(x=difficult_frequency, y=difficult_annotation, c='b', s=2)
# plt.plot([0.5, 0.8], [0.5, 0.8], ls='--', c='.3')
plt.xlabel('Natural frequency(log)', fontsize=18)
plt.ylabel('Plausibility', fontsize=18)
ax.set_xscale('log')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0.000001, 1)

plt.show()

print('end')
