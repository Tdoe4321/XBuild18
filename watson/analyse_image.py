# https://gateway-a.watsonplatform.net/visual-recognition/api
# 8b88ac2bb3bd7daef956e79c8cdd68b9aa592144
# 960658f4802f8d5d1454717447a044f75c9e8d71

from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException

visual_recognition = VisualRecognitionV3('2018-03-19', api_key='960658f4802f8d5d1454717447a044f75c9e8d71')

#classifiers = visual_recognition.list_classifiers(verbose=True)
#print(json.dumps(classifiers, indent=2))

lieorstand_path = join(dirname(__file__), 'LieOrStand2.zip')
with open(lieorstand_path, 'rb') as images_file:
#    parameters = json.dumps({'threshold': 0.5, 'classifier_ids': ['RemoteTriage_2043407675', 'default']})
#    parameters = json.dumps({'threshold': 0.5, 'classifier_ids': ['RemoteTriage_482484271', 'default']})
    parameters = json.dumps({'threshold': 0.1, 'classifier_ids': ['faces']})
    lieorstand_results = visual_recognition.classify(images_file=images_file,
                                              parameters=parameters)
    print(json.dumps(lieorstand_results, indent=2))
    #results_dict = json.load(lieorstand_results)
    #for item in lieorstand_results['images'][0]['classifiers'][0]['classes']:
     #   print '{} ({})'.format(item['class'], item['score'])

# Interpret the result
str = 'I might have seen a '
 
