import xml.etree.ElementTree as ET
import os
import json

sentences = list()
root_folder = '/home/hzhangal/NYT_annotated_corpus/data'
tree = ET.parse('test_NYT.xml')
root = tree.getroot()
for children in root:
    if children.tag == 'body':
        for body_children in children:
            if body_children.tag == 'body.content':
                for content_children in body_children:
                    if content_children.attrib['class'] == 'full_text':
                        for sentence in content_children:
                            print(sentence.text)
                    # print(content_children.attrib)
                    # print(content_children.tag)
            # print(body_children.tag)
    # print(children.tag)

for year in os.listdir(root_folder):
    print('We are working on year:', year)
    tmp_year_folder = root_folder + '/' + year
    for month in os.listdir(tmp_year_folder):
        print('We are working on month:', month)
        tmp_sentences = list()
        tmp_month_folder = tmp_year_folder + '/' + month
        for day in os .listdir(tmp_month_folder):
            print('We are working on day:', day)
            tmp_day_folder = tmp_month_folder + '/' + day
            for file_name in os.listdir(tmp_day_folder):
                tmp_file_name = tmp_day_folder + '/' + file_name
                tmp_tree = ET.parse(tmp_file_name)
                tmp_root = tmp_tree.getroot()
                for children in tmp_root:
                    if children.tag == 'body':
                        for body_children in children:
                            if body_children.tag == 'body.content':
                                for content_children in body_children:
                                    if content_children.attrib['class'] == 'full_text':
                                        for sentence in content_children:
                                            print(sentence.text)
        with open('prepared_NYT_data/' + year + '_' + month + '.json', 'w') as f:
            json.dump(tmp_sentences, f)

print('end')
