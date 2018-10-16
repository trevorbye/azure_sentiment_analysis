import requests
from pprint import pprint
import csv
import jsonpickle
import json

from DocumentEntity import Document
from DocumentsEntity import Documents
import LoadCommentEntity


def build_raw_comment_list(entity_list):
    comment_list = []
    for entity in entity_list:
        comment_list.append(entity.loadComment)

    return comment_list


subscription_key = "300e91bb46e84961b2ccbecdf8595f4c"
base_url = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"

load_comment_entity_list = []

with open("C:\\Users\\s-tbye\\Desktop\\comments.txt", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        size = len(load_comment_entity_list)
        if size == 1000:
            break

        load_comment_entity_list.append(LoadCommentEntity.CommentEntity(row[0], row[1]))

comment_iterator = iter(load_comment_entity_list)
raw_comment_list = build_raw_comment_list(comment_iterator)

documents = []

id_counter = 1
for comment in raw_comment_list:
    doc = Document(id_counter, "en", comment)
    documents.append(doc)
    id_counter = id_counter + 1

document_object = Documents(documents)
json_string = jsonpickle.encode(document_object, unpicklable=False)
json_dict = json.loads(json_string)

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(base_url, headers=headers, json=json_dict)
sentiments = response.json()

pprint(sentiments)



