import json
import os

print('We are working on detailed information about wiki')
if os.path.isfile('verb_nsubj_amod_dict_wiki.json'):
    with open('verb_nsubj_amod_dict_wiki.json', 'r') as f:
        verb_nsubj_amod_dict = json.load(f)

if os.path.isfile('verb_dobj_amod_dict_wiki.json'):
    with open('verb_dobj_amod_dict_wiki.json', 'r') as f:
        verb_dobj_amod_dict = json.load(f)

if os.path.isfile('verb_nsubj_dict_wiki.json'):
    with open('verb_nsubj_dict_wiki.json', 'r') as f:
        verb_nsubj_dict = json.load(f)

if os.path.isfile('verb_dobj_dict_wiki.json'):
    with open('verb_dobj_dict_wiki.json', 'r') as f:
        verb_dobj_dict = json.load(f)

if os.path.isfile('noun_amod_dict_wiki.json'):
    with open('noun_amod_dict_wiki.json', 'r') as f:
        noun_amod_dict = json.load(f)

dobj_number = 0
nsubj_number = 0
amod_number = 0
dobj_amod_number = 0
nsubj_amod_number = 0

for verb in verb_dobj_dict:
    for noun in verb_dobj_dict[verb]:
        dobj_number += verb_dobj_dict[verb][noun]
print('Number of dobj:', dobj_number)

for verb in verb_nsubj_dict:
    for noun in verb_nsubj_dict[verb]:
        nsubj_number += verb_nsubj_dict[verb][noun]
print('Number of nsubj:', nsubj_number)

for noun in noun_amod_dict:
    for adj in noun_amod_dict[noun]:
        amod_number += noun_amod_dict[noun][adj]
print('Number of amod:', amod_number)

for verb in verb_dobj_amod_dict:
    for adj in verb_dobj_amod_dict[verb]:
        dobj_amod_number += verb_dobj_amod_dict[verb][adj]
print('Number of dobj_amod:', verb_dobj_amod_dict)

for verb in verb_nsubj_amod_dict:
    for adj in verb_nsubj_amod_dict[verb]:
        nsubj_amod_number += verb_nsubj_amod_dict[verb][adj]
print('Number of nsubj_amod:', verb_nsubj_amod_dict)

print('We are working on detailed information about yelp')
if os.path.isfile('verb_nsubj_amod_dict_yelp.json'):
    with open('verb_nsubj_amod_dict_yelp.json', 'r') as f:
        verb_nsubj_amod_dict = json.load(f)

if os.path.isfile('verb_dobj_amod_dict_yelp.json'):
    with open('verb_dobj_amod_dict_yelp.json', 'r') as f:
        verb_dobj_amod_dict = json.load(f)

if os.path.isfile('verb_nsubj_dict_yelp.json'):
    with open('verb_nsubj_dict_yelp.json', 'r') as f:
        verb_nsubj_dict = json.load(f)

if os.path.isfile('verb_dobj_dict_yelp.json'):
    with open('verb_dobj_dict_yelp.json', 'r') as f:
        verb_dobj_dict = json.load(f)

if os.path.isfile('noun_amod_dict_yelp.json'):
    with open('noun_amod_dict_yelp.json', 'r') as f:
        noun_amod_dict = json.load(f)

dobj_number = 0
nsubj_number = 0
amod_number = 0
dobj_amod_number = 0
nsubj_amod_number = 0

for verb in verb_dobj_dict:
    for noun in verb_dobj_dict[verb]:
        dobj_number += verb_dobj_dict[verb][noun]
print('Number of dobj:', dobj_number)

for verb in verb_nsubj_dict:
    for noun in verb_nsubj_dict[verb]:
        nsubj_number += verb_nsubj_dict[verb][noun]
print('Number of nsubj:', nsubj_number)

for noun in noun_amod_dict:
    for adj in noun_amod_dict[noun]:
        amod_number += noun_amod_dict[noun][adj]
print('Number of amod:', amod_number)

for verb in verb_dobj_amod_dict:
    for adj in verb_dobj_amod_dict[verb]:
        dobj_amod_number += verb_dobj_amod_dict[verb][adj]
print('Number of dobj_amod:', verb_dobj_amod_dict)

for verb in verb_nsubj_amod_dict:
    for adj in verb_nsubj_amod_dict[verb]:
        nsubj_amod_number += verb_nsubj_amod_dict[verb][adj]
print('Number of nsubj_amod:', verb_nsubj_amod_dict)

print('We are working on detailed information about NYT')
if os.path.isfile('verb_nsubj_amod_dict_nyt.json'):
    with open('verb_nsubj_amod_dict_nyt.json', 'r') as f:
        verb_nsubj_amod_dict = json.load(f)

if os.path.isfile('verb_dobj_amod_dict_nyt.json'):
    with open('verb_dobj_amod_dict_nyt.json', 'r') as f:
        verb_dobj_amod_dict = json.load(f)

if os.path.isfile('verb_nsubj_dict_nyt.json'):
    with open('verb_nsubj_dict_nyt.json', 'r') as f:
        verb_nsubj_dict = json.load(f)

if os.path.isfile('verb_dobj_dict_nyt.json'):
    with open('verb_dobj_dict_nyt.json', 'r') as f:
        verb_dobj_dict = json.load(f)

if os.path.isfile('noun_amod_dict_nyt.json'):
    with open('noun_amod_dict_nyt.json', 'r') as f:
        noun_amod_dict = json.load(f)

dobj_number = 0
nsubj_number = 0
amod_number = 0
dobj_amod_number = 0
nsubj_amod_number = 0

for verb in verb_dobj_dict:
    for noun in verb_dobj_dict[verb]:
        dobj_number += verb_dobj_dict[verb][noun]
print('Number of dobj:', dobj_number)

for verb in verb_nsubj_dict:
    for noun in verb_nsubj_dict[verb]:
        nsubj_number += verb_nsubj_dict[verb][noun]
print('Number of nsubj:', nsubj_number)

for noun in noun_amod_dict:
    for adj in noun_amod_dict[noun]:
        amod_number += noun_amod_dict[noun][adj]
print('Number of amod:', amod_number)

for verb in verb_dobj_amod_dict:
    for adj in verb_dobj_amod_dict[verb]:
        dobj_amod_number += verb_dobj_amod_dict[verb][adj]
print('Number of dobj_amod:', verb_dobj_amod_dict)

for verb in verb_nsubj_amod_dict:
    for adj in verb_nsubj_amod_dict[verb]:
        nsubj_amod_number += verb_nsubj_amod_dict[verb][adj]
print('Number of nsubj_amod:', verb_nsubj_amod_dict)
