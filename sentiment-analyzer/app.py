import json
import gzip

g = gzip.open('All_Beauty_5.json.gz', 'r')
dataset = []
for l in g:
  dataset_json = json.loads(l)
  dataset.append(dataset_json)

reviews = []
for i in range(len(dataset)):
  if "reviewText" in dataset[i].keys():
    review = []
    review.append(dataset[i]['reviewText'])
    
    reviews.append(review)

print(reviews)