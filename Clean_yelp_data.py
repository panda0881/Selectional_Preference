import json

review_data_location = '/home/data/corpora/yelp_dataset_challenge_round11/dataset'

with open(review_data_location, 'r') as f:
    round11_data = json.load(f)

sampled_round11_data = round11_data[:100]
with open('sampled_yelp_round11.json', 'w') as f:
    json.dump(sampled_round11_data, f)

print('end')
