from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException
from show_image import show_image
import os

visual_recognition = VisualRecognitionV3('2018-03-19', api_key='')

# To print the list of available classifiers:
#classifiers = visual_recognition.list_classifiers(verbose=True)
#print(json.dumps(classifiers, indent=2))

lieorstand_path = join(dirname(__file__), 'LieOrStand2.zip')
with open(lieorstand_path, 'rb') as images_file:

    parameters = json.dumps({'threshold': 0.5, 
                             'classifier_ids': ['RemoteTriage_198583496', 'default']})
    global results
    results = visual_recognition.classify(images_file=images_file,
                                          parameters=parameters)
    results = json.dumps(results)
    results = json.loads(results)
#    print(results)                                      
#    results = {u'images': [{u'image': u'LieOrStand2.zip/C.jpg', u'classifiers': [{u'classes': [{u'score': 0.851, u'class': u'Parkour', u'type_hierarchy': u'/sport/Parkour'}, {u'score': 0.851, u'class': u'sport'}, {u'score': 0.5, u'class': u'nylons', u'type_hierarchy': u'/hosiery/nylons'}, {u'score': 0.508, u'class': u'hosiery'}, {u'score': 0.793, u'class': u'footwear'}, {u'score': 0.8, u'class': u'clothing'}, {u'score': 0.923, u'class': u'charcoal color'}, {u'score': 0.909, u'class': u'gray color'}], u'classifier_id': u'default', u'name': u'default'}, {u'classes': [{u'score': 0.823, u'class': u'Erect (3)'}], u'classifier_id': u'RemoteTriage_198583496', u'name': u'Remote Triage'}]}, {u'image': u'LieOrStand2.zip/B.jpg', u'classifiers': [{u'classes': [{u'score': 0.868, u'class': u'Erect (3)'}], u'classifier_id': u'RemoteTriage_198583496', u'name': u'Remote Triage'}, {u'classes': [{u'score': 0.597, u'class': u'ramp', u'type_hierarchy': u'/mechanical device/machine/inclined plane/ramp'}, {u'score': 0.597, u'class': u'inclined plane'}, {u'score': 0.598, u'class': u'machine'}, {u'score': 0.602, u'class': u'mechanical device'}, {u'score': 0.544, u'class': u'khukuri (knife)', u'type_hierarchy': u'/weapon/knife/khukuri (knife)'}, {u'score': 0.545, u'class': u'knife'}, {u'score': 0.556, u'class': u'weapon'}, {u'score': 0.511, u'class': u'Repairing'}, {u'score': 0.51, u'class': u'Earthquake'}, {u'score': 0.5, u'class': u'stoop', u'type_hierarchy': u'/porch/stoop'}, {u'score': 0.5, u'class': u'porch'}, {u'score': 0.597, u'class': u'lever'}, {u'score': 0.98, u'class': u'gray color'}], u'classifier_id': u'default', u'name': u'default'}]}, {u'image': u'LieOrStand2.zip/A.jpg', u'classifiers': [{u'classes': [{u'score': 0.889, u'class': u'Erect (3)'}], u'classifier_id': u'RemoteTriage_198583496', u'name': u'Remote Triage'}, {u'classes': [{u'score': 0.798, u'class': u'person'}, {u'score': 0.903, u'class': u'Parkour', u'type_hierarchy': u'/sport/Parkour'}, {u'score': 0.922, u'class': u'sport'}, {u'score': 0.5, u'class': u'skateboarding', u'type_hierarchy': u'/sport/skating/skateboarding'}, {u'score': 0.502, u'class': u'skating'}, {u'score': 0.794, u'class': u'clothing'}, {u'score': 0.964, u'class': u'gray color'}, {u'score': 0.793, u'class': u'charcoal color'}], u'classifier_id': u'default', u'name': u'default'}]}, {u'image': u'LieOrStand2.zip/IMG_4132.jpg', u'classifiers': [{u'classes': [{u'score': 0.784, u'class': u'Erect (3)'}], u'classifier_id': u'RemoteTriage_198583496', u'name': u'Remote Triage'}, {u'classes': [{u'score': 0.57, u'class': u'lever', u'type_hierarchy': u'/bar/lever'}, {u'score': 0.659, u'class': u'bar'}, {u'score': 0.538, u'class': u'handlebar', u'type_hierarchy': u'/bar/handlebar'}, {u'score': 0.531, u'class': u'skateboarding', u'type_hierarchy': u'/sport/skating/skateboarding'}, {u'score': 0.533, u'class': u'skating'}, {u'score': 0.534, u'class': u'sport'}, {u'score': 0.5, u'class': u'stabilizer bar'}, {u'score': 0.599, u'class': u'weapon'}, {u'score': 0.599, u'class': u'sports equipment'}, {u'score': 0.893, u'class': u'gray color'}, {u'score': 0.581, u'class': u'ash grey color'}], u'classifier_id': u'default', u'name': u'default'}]}, {u'image': u'LieOrStand2.zip/D.jpg', u'classifiers': [{u'classes': [{u'score': 0.64, u'class': u'stocking', u'type_hierarchy': u'/hosiery/stocking'}, {u'score': 0.725, u'class': u'hosiery'}, {u'score': 0.561, u'class': u'boothose', u'type_hierarchy': u'/hosiery/boothose'}, {u'score': 0.535, u'class': u'pogo stick'}, {u'score': 0.5, u'class': u'belt', u'type_hierarchy': u'/accessory/belt'}, {u'score': 0.501, u'class': u'accessory'}, {u'score': 0.599, u'class': u'sport'}, {u'score': 0.599, u'class': u'knot'}, {u'score': 0.601, u'class': u'clothing'}, {u'score': 0.633, u'class': u'maroon color'}, {u'score': 0.512, u'class': u'purple color'}], u'classifier_id': u'default', u'name': u'default'}, {u'classes': [{u'score': 0.654, u'class': u'Erect (3)'}, {u'score': 0.622, u'class': u'Prone (1)'}], u'classifier_id': u'RemoteTriage_198583496', u'name': u'Remote Triage'}]}], u'custom_classes': 3, u'images_processed': 5}
                                        
with open(lieorstand_path, 'rb') as images_file:
    global faces
    faces = visual_recognition.detect_faces(images_file=images_file)
#    print(faces)
    faces = json.dumps(faces)
    faces = json.loads(faces)
#    faces = {u'images': [{u'image': u'LieOrStand2.zip/B.jpg', u'faces': [{u'gender': {u'gender': u'MALE', u'score': 0.9846315}, u'age': {u'max': 28, u'score': 0.83206326, u'min': 24}, u'face_location': {u'width': 136, u'top': 757, u'left': 1296, u'height': 146}}]}, {u'image': u'LieOrStand2.zip/A.jpg', u'faces': [{u'gender': {u'gender': u'MALE', u'score': 0.99685293}, u'age': {u'max': 40, u'score': 0.2921676, u'min': 32}, u'face_location': {u'width': 135, u'top': 747, u'left': 1730, u'height': 137}}]}, {u'image': u'LieOrStand2.zip/D.jpg', u'faces': [{u'gender': {u'gender': u'MALE', u'score': 0.9732676}, u'age': {u'max': 28, u'score': 0.99969834, u'min': 25}, u'face_location': {u'width': 175, u'top': 644, u'left': 1170, u'height': 205}}]}, {u'image': u'LieOrStand2.zip/IMG_4132.jpg', u'faces': []}, {u'image': u'LieOrStand2.zip/C.jpg', u'faces': [{u'gender': {u'gender': u'MALE', u'score': 0.8604275}, u'age': {u'max': 41, u'score': 0.23711067, u'min': 32}, u'face_location': {u'width': 179, u'top': 794, u'left': 724, u'height': 190}}]}], u'images_processed': 5}

     
if results:
    for im in results[u'images']:
        print(' ')
        fileparts = os.path.split(im[u'image'])
        filename = fileparts[1]
        print(filename)
        situation = []
        face_type = []
        face_pos = []
        for clasf in im[u'classifiers']:
            clasf_name = clasf[u'name']
            if u'Triage' in clasf_name:
                print('The classifier is Remote Triage')
                for item in clasf[u'classes']:
                    if u'Prone' in item[u'class']:
                        situation.append('Prone person probability (%0.0f%%)' % (item['score'] * 100.0))
                    else:
                        print(item[u'class'])
                        print(item[u'score'])
        # Find the right face information
        for face_im in faces[u'images']:
            if filename in face_im[u'image']:
                for face in face_im[u'faces']:
                    face_type.append('%s (age %d-%d)' % (face[u'gender'][u'gender'], face[u'age'][u'min'], face[u'age'][u'max'])) 
                    pos = (face[u'face_location'][u'left'], face[u'face_location'][u'top'], face[u'face_location'][u'width'], face[u'face_location'][u'height'])
                    face_pos.append(pos)
             
        show_image(filename, 'LieOrStand2/' + filename, situation, face_type, face_pos)

# Debug variable content so Watson does not get a query for every development iteration
#    results = {u'images': [{u'image': u'LieOrStand2.zip/A.jpg', u'classifiers': [{u'classes': [{u'score': 0.889, u'class': u'Erect'}], u'classifier_id': u'RemoteTriage_482484271', u'name': u'Remote Triage'}, {u'classes': [{u'score': 0.798, u'class': u'person'}, {u'score': 0.903, u'class': u'Parkour', u'type_hierarchy': u'/sport/Parkour'}, {u'score': 0.922, u'class': u'sport'}, {u'score': 0.5, u'class': u'skateboarding', u'type_hierarchy': u'/sport/skating/skateboarding'}, {u'score': 0.502, u'class': u'skating'}, {u'score': 0.794, u'class': u'clothing'}, {u'score': 0.964, u'class': u'gray color'}, {u'score': 0.793, u'class': u'charcoal color'}], u'classifier_id': u'default', u'name': u'default'}]}, {u'image': u'LieOrStand2.zip/D.jpg', u'classifiers': [{u'classes': [{u'score': 0.907, u'class': u'Prone'}], u'classifier_id': u'RemoteTriage_482484271', u'name': u'Remote Triage'}, {u'classes': [{u'score': 0.64, u'class': u'stocking', u'type_hierarchy': u'/hosiery/stocking'}, {u'score': 0.725, u'class': u'hosiery'}, {u'score': 0.561, u'class': u'boothose', u'type_hierarchy': u'/hosiery/boothose'}, {u'score': 0.535, u'class': u'pogo stick'}, {u'score': 0.5, u'class': u'belt', u'type_hierarchy': u'/accessory/belt'}, {u'score': 0.501, u'class': u'accessory'}, {u'score': 0.599, u'class': u'sport'}, {u'score': 0.599, u'class': u'knot'}, {u'score': 0.601, u'class': u'clothing'}, {u'score': 0.633, u'class': u'maroon color'}, {u'score': 0.512, u'class': u'purple color'}], u'classifier_id': u'default', u'name': u'default'}]}, {u'image': u'LieOrStand2.zip/C.jpg', u'classifiers': [{u'classes': [{u'score': 0.907, u'class': u'Prone'}], u'classifier_id': u'RemoteTriage_482484271', u'name': u'Remote Triage'}, {u'classes': [{u'score': 0.851, u'class': u'Parkour', u'type_hierarchy': u'/sport/Parkour'}, {u'score': 0.851, u'class': u'sport'}, {u'score': 0.5, u'class': u'nylons', u'type_hierarchy': u'/hosiery/nylons'}, {u'score': 0.508, u'class': u'hosiery'}, {u'score': 0.793, u'class': u'footwear'}, {u'score': 0.8, u'class': u'clothing'}, {u'score': 0.923, u'class': u'charcoal color'}, {u'score': 0.909, u'class': u'gray color'}], u'classifier_id': u'default', u'name': u'default'}]}, {u'image': u'LieOrStand2.zip/B.jpg', u'classifiers': [{u'classes': [{u'score': 0.88, u'class': u'Prone'}], u'classifier_id': u'RemoteTriage_482484271', u'name': u'Remote Triage'}, {u'classes': [{u'score': 0.597, u'class': u'ramp', u'type_hierarchy': u'/mechanical device/machine/inclined plane/ramp'}, {u'score': 0.597, u'class': u'inclined plane'}, {u'score': 0.598, u'class': u'machine'}, {u'score': 0.602, u'class': u'mechanical device'}, {u'score': 0.544, u'class': u'khukuri (knife)', u'type_hierarchy': u'/weapon/knife/khukuri (knife)'}, {u'score': 0.545, u'class': u'knife'}, {u'score': 0.556, u'class': u'weapon'}, {u'score': 0.511, u'class': u'Repairing'}, {u'score': 0.51, u'class': u'Earthquake'}, {u'score': 0.5, u'class': u'stoop', u'type_hierarchy': u'/porch/stoop'}, {u'score': 0.5, u'class': u'porch'}, {u'score': 0.597, u'class': u'lever'}, {u'score': 0.98, u'class': u'gray color'}], u'classifier_id': u'default', u'name': u'default'}]}, {u'image': u'LieOrStand2.zip/IMG_4132.jpg', u'classifiers': [{u'classes': [{u'score': 0.784, u'class': u'Erect'}], u'classifier_id': u'RemoteTriage_482484271', u'name': u'Remote Triage'}, {u'classes': [{u'score': 0.57, u'class': u'lever', u'type_hierarchy': u'/bar/lever'}, {u'score': 0.659, u'class': u'bar'}, {u'score': 0.538, u'class': u'handlebar', u'type_hierarchy': u'/bar/handlebar'}, {u'score': 0.531, u'class': u'skateboarding', u'type_hierarchy': u'/sport/skating/skateboarding'}, {u'score': 0.533, u'class': u'skating'}, {u'score': 0.534, u'class': u'sport'}, {u'score': 0.5, u'class': u'stabilizer bar'}, {u'score': 0.599, u'class': u'weapon'}, {u'score': 0.599, u'class': u'sports equipment'}, {u'score': 0.893, u'class': u'gray color'}, {u'score': 0.581, u'class': u'ash grey color'}], u'classifier_id': u'default', u'name': u'default'}]}], u'custom_classes': 3, u'images_processed': 5}
#    faces = {u'images': [{u'image': u'LieOrStand2.zip/B.jpg', u'faces': [{u'gender': {u'gender': u'MALE', u'score': 0.9846315}, u'age': {u'max': 28, u'score': 0.83206326, u'min': 24}, u'face_location': {u'width': 136, u'top': 757, u'left': 1296, u'height': 146}}]}, {u'image': u'LieOrStand2.zip/A.jpg', u'faces': [{u'gender': {u'gender': u'MALE', u'score': 0.99685293}, u'age': {u'max': 40, u'score': 0.2921676, u'min': 32}, u'face_location': {u'width': 135, u'top': 747, u'left': 1730, u'height': 137}}]}, {u'image': u'LieOrStand2.zip/D.jpg', u'faces': [{u'gender': {u'gender': u'MALE', u'score': 0.9732676}, u'age': {u'max': 28, u'score': 0.99969834, u'min': 25}, u'face_location': {u'width': 175, u'top': 644, u'left': 1170, u'height': 205}}]}, {u'image': u'LieOrStand2.zip/IMG_4132.jpg', u'faces': []}, {u'image': u'LieOrStand2.zip/C.jpg', u'faces': [{u'gender': {u'gender': u'MALE', u'score': 0.8604275}, u'age': {u'max': 41, u'score': 0.23711067, u'min': 32}, u'face_location': {u'width': 179, u'top': 794, u'left': 724, u'height': 190}}]}], u'images_processed': 5}

 
