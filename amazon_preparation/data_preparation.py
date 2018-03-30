sample_verbs = list()
for i in range(100):
    sample_verbs.append('verb' + str(i+1))

relation_dict = dict()
for verb in sample_verbs:
    relation_dict[verb] = dict()
    relation_dict[verb]['nsubj'] = ['noun1', 'noun2', 'noun3', 'noun4', 'noun5']
    relation_dict[verb]['nsubj_amod'] = ['adj1', 'adj2', 'adj3', 'adj4', 'adj5']
    relation_dict[verb]['dobj'] = ['noun1', 'noun2', 'noun3', 'noun4', 'noun5']
    relation_dict[verb]['dobj_amod'] = ['adj1', 'adj2', 'adj3', 'adj4', 'adj5']

tmp_pairs = list()
for tmp_verb in sample_verbs:
    related_words = relation_dict[tmp_verb]['dobj']
    for w in related_words:
        tmp_pairs.append((tmp_verb, w))


print('end')
