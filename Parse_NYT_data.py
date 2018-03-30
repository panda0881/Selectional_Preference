import xml.etree.ElementTree as ET
import os
import json

sentences = list()
root_folder = '~/NYT_annotated_corpus/data'
tree = ET.parse('test_NYT.xml')
root = tree.getroot()

for year in os.listdir(root_folder):
    print('We are working on year:', year)
    tmp_year_folder = root_folder + '/' + year
    for month in os.listdir(tmp_year_folder):
        print('We are working on month:', month)
        tmp_month_folder = tmp_year_folder + '/' + month
        tmp_sentences = list()
        for file_name in os.listdir(tmp_month_folder):
            tmp_file_name = tmp_month_folder + '/' + file_name
            tmp_tree = ET.parse(tmp_file_name)
            tmp_root = tmp_tree.getroot()
            for children in tmp_root[1][1][1]:
                tmp_sentences.append(children.text)
        with open('prepared_NYT_data/' + year + '_' + month + '.json', 'w') as f:
            json.dump(tmp_sentences, f)

print('end')
