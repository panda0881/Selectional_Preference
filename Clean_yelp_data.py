import json

review_data_location = '/home/data/corpora/yelp_dataset_challenge_round11/dataset/review.json'
# sampled_round11_data = list()
with open(review_data_location, 'r') as f:
    counter = 0
    for line in f:
        counter += 1

print('Total number of review: ', counter)

print('end')
