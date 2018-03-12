from pycorenlp import StanfordCoreNLP
import json
nlp = StanfordCoreNLP('http://localhost:9000')

# path = '/home/data/corpora/wikipedia/enwiki-20131101'

parsed_relations = list()
tmp_relation_list = list()
f = open('/home/data/corpora/yelp_dataset_challenge_round11/dataset/review.json', 'r')
counter = 0
for line in f:
    tmp_data = json.loads(line)
    text = tmp_data['text']
    counter += 1
    if counter % 1000 == 0:
        print('We have analyzed ', counter, 'sentences')
        print('We have collected', len(tmp_relation_list), 'sentences')
    output = nlp.annotate(text, properties={'annotators': 'tokenize,depparse,lemma', 'outputFormat': 'json'})
    if counter % 1000000 == 0:
        print('We are storing parsing result for', counter, 'sentences')
        file_name = 'parsed_yelp_data_with_stanford/' + str(counter) + '.json'
        file = open(file_name, 'w')
        json.dump(parsed_relations, file)
        file.close()
        parsed_relations = list()
        tmp_relation_list = list()
    tmp_parsed_sentence = list()
    try:
        for sentence in output['sentences']:
            enhanced_dependency_list = sentence['enhancedPlusPlusDependencies']
            stored_dependency_list = list()
            for relation in enhanced_dependency_list:
                if relation['dep'] == 'ROOT':
                    continue
                governor_position = relation['governor']
                dependent_position = relation['dependent']
                stored_dependency_list.append(((governor_position, sentence['tokens'][governor_position-1]['lemma']), relation['dep'], (dependent_position, sentence['tokens'][dependent_position-1]['lemma'])))
            tmp_relation_list.append(stored_dependency_list)
            tmp_parsed_sentence.append(stored_dependency_list)
        parsed_relations.append(tmp_parsed_sentence)
    except:
        parsed_relations.append(tmp_parsed_sentence)
        continue

print('end')
