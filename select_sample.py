import json

tmp_file_name = '/home/data/corpora/wikipedia/stanford_enhanced++_parsed_data/1000000.json'

with open(tmp_file_name, 'r') as original_f:
    all_data = json.load(original_f)
    sample_data = all_data[:100]

with open('sampled_example.json', 'w') as sample_f:
    json.dump(sample_data, sample_f)

print('end')
