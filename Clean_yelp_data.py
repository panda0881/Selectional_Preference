import json

review_data_location = '/home/data/corpora/yelp_dataset_challenge_round11/dataset/review.json'
# sampled_round11_data = list()
# with open(review_data_location, 'r') as f:
#     counter = 0
#     for line in f:
#         tmp_data = json.loads(line)
#         sampled_round11_data.append(tmp_data)
#         counter += 1
#         if counter >= 100:
#             break

with open('sampled_yelp_round11.json', 'r') as f:
    sampled_round_data = json.load(f)

print('end')
