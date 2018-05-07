import json
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

with open('natural_frequency_result.json', 'r') as f:
    data = json.load(f)

print('We are working on amod')
annotation = data['amod']['annotation']
frequency = data['amod']['frequency']
print('spearman:', spearmanr(annotation, frequency)[0])

# print('We are working on nsubj')
# annotation = data['nsubj']['annotation']
# frequency = data['nsubj']['frequency']
# print('spearman:', spearmanr(annotation, frequency)[0])
#
# print('We are working on dobj')
# annotation = data['dobj']['annotation']
# frequency = data['dobj']['frequency']
# print('spearman:', spearmanr(annotation, frequency)[0])

# print('We are working on nsubj_amod')
# annotation = data['nsubj_amod']['annotation']
# frequency = data['nsubj_amod']['frequency']
# print('spearman:', spearmanr(annotation, frequency)[0])
#
# print('We are working on dobj_amod')
# annotation = data['dobj_amod']['annotation']
# frequency = data['dobj_amod']['frequency']
# print('spearman:', spearmanr(annotation, frequency)[0])

fig = plt.figure()
ax = plt.gca()
ax.scatter(x=frequency, y=annotation, s=2)
# plt.plot([0.5, 0.8], [0.5, 0.8], ls='--', c='.3')
plt.xlabel('Natural frequency(log)', fontsize=18)
plt.ylabel('Plausibility', fontsize=18)
ax.set_xscale('log')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0.000001, 1)

plt.show()

print('end')
