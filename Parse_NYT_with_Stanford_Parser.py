from pycorenlp import StanfordCoreNLP
import json
import os
nlp = StanfordCoreNLP('http://localhost:9000')

# path = '/home/data/corpora/wikipedia/enwiki-20131101'

parsed_relations = list()
tmp_relation_list = list()
folder = 'prepared_NYT_data'
# counter = 0
for file_name in os.listdir(folder):
    print('We are working on file:', file_name)
    tmp_file_name = folder + '/' + file_name
    parsed_relations = list()
    with open(tmp_file_name, 'r') as f:
        tmp_sentences = json.load(f)
        for text in tmp_sentences:
            output = nlp.annotate(text, properties={'annotators': 'tokenize,depparse,lemma', 'outputFormat': 'json'})
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
    with open('parsed_NYT_data/' + file_name, 'w') as f:
        json.dump(parsed_relations, f)


print('end')
