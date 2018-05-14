import pandas
import os
import numpy as np
import matplotlib.pyplot as plt

tmp_folder_position = 'annotation_result/dobj/'
dobj_time_list = list()
for f_name in os.listdir(tmp_folder_position):
    tmp_file_name = tmp_folder_position + f_name
    tmp_table = pandas.read_csv(tmp_file_name)
    dobj_time_list += tmp_table['WorkTimeInSeconds'].tolist()
dobj_time = sum(dobj_time_list)/len(dobj_time_list)
dobj_std = np.asarray(dobj_time_list).std()
print('dobj:', dobj_time, dobj_std)

tmp_folder_position = 'annotation_result/nsubj/'
nsubj_time_list = list()
for f_name in os.listdir(tmp_folder_position):
    tmp_file_name = tmp_folder_position + f_name
    tmp_table = pandas.read_csv(tmp_file_name)
    nsubj_time_list += tmp_table['WorkTimeInSeconds'].tolist()
nsubj_time = sum(nsubj_time_list)/len(nsubj_time_list)
nsubj_std = np.asarray(nsubj_time_list).std()
print('nsubj:', nsubj_time, nsubj_std)

tmp_folder_position = 'annotation_result/amod/'
amod_time_list = list()
for f_name in os.listdir(tmp_folder_position):
    tmp_file_name = tmp_folder_position + f_name
    tmp_table = pandas.read_csv(tmp_file_name)
    amod_time_list += tmp_table['WorkTimeInSeconds'].tolist()
amod_time = sum(amod_time_list)/len(amod_time_list)
amod_std = np.asarray(amod_time_list).std()
print('amod:', amod_time, amod_std)

tmp_folder_position = 'annotation_result/dobj_amod/'
dobj_amod_time_list = list()
for f_name in os.listdir(tmp_folder_position):
    tmp_file_name = tmp_folder_position + f_name
    tmp_table = pandas.read_csv(tmp_file_name)
    dobj_amod_time_list += tmp_table['WorkTimeInSeconds'].tolist()
dobj_amod_time = sum(dobj_amod_time_list)/len(dobj_amod_time_list)
dobj_amod_std = np.asarray(dobj_amod_time_list).std()
print('dobj_amod:', dobj_amod_time, dobj_amod_std)

tmp_folder_position = 'annotation_result/nsubj_amod/'
nsubj_amod_time_list = list()
for f_name in os.listdir(tmp_folder_position):
    tmp_file_name = tmp_folder_position + f_name
    tmp_table = pandas.read_csv(tmp_file_name)
    nsubj_amod_time_list += tmp_table['WorkTimeInSeconds'].tolist()
nsubj_amod_time = sum(nsubj_amod_time_list)/len(nsubj_amod_time_list)
nsubj_amod_std = np.asarray(nsubj_amod_time_list).std()
print('nsubj_amod:', nsubj_amod_time, nsubj_amod_std)

times = np.asarray([dobj_time/60, nsubj_time/60, amod_time/60, dobj_amod_time/60, nsubj_amod_time/60])
stds = np.asarray([dobj_std/60, nsubj_std/60, amod_std/60, dobj_amod_std/60, nsubj_amod_std/60])
relations = ['dobj', 'nsubj', 'amod', 'dobj_amod', 'nsubj_amod']

width = 0.35
ind = np.arange(5)
fig, ax = plt.subplots()

rects1 = ax.bar(ind, times, width, color='b')


ax.set_ylabel('Avg. Time', fontsize=25)
ax.set_xticks(ind)
ax.set_xticklabels(('dobj', 'nsubj', 'amod', 'dobj_amod', 'nsubj_amod'))

# ax.legend((rects1[0], rects2[0]), ('IAA-1', 'IAA-2'), fontsize=20)
times_in_minute = ['25m28s', '29m22s', '18m21s', '23m29s', '29m52s']
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for i, rect in enumerate(rects):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                times_in_minute[i],
                ha='center', va='bottom', fontsize=20)

autolabel(rects1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylim([10.00, 33.00])
plt.show()


print('end')

