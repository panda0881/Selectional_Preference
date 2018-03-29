sample_verbs = list()
for i in range(100):
    sample_verbs.append('verb' + str(i+1))

relation_dict = dict()
for verb in sample_verbs:
    relation_dict[verb] = dict()
    relation_dict[verb]['nsubj'] = list()
    relation_dict[verb]['nsubj_amod'] = list()
    relation_dict[verb]['dobj'] = list()
    relation_dict[verb]['dobj_amod'] = list()

print('end')
