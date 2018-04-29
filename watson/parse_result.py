from show_image import show_image
import os

results = {
  "images": [
    {
      "image": "LieOrStand2.zip/IMG_4132.jpg", 
      "classifiers": [
        {
          "classes": [
            {
              "score": 0.784, 
              "class": "Erect"
            }
          ], 
          "classifier_id": "RemoteTriage_482484271", 
          "name": "Remote Triage"
        }, 
        {
          "classes": [
            {
              "score": 0.57, 
              "class": "lever", 
              "type_hierarchy": "/bar/lever"
            }, 
            {
              "score": 0.659, 
              "class": "bar"
            }, 
            {
              "score": 0.538, 
              "class": "handlebar", 
              "type_hierarchy": "/bar/handlebar"
            }, 
            {
              "score": 0.531, 
              "class": "skateboarding", 
              "type_hierarchy": "/sport/skating/skateboarding"
            }, 
            {
              "score": 0.533, 
              "class": "skating"
            }, 
            {
              "score": 0.534, 
              "class": "sport"
            }, 
            {
              "score": 0.5, 
              "class": "stabilizer bar"
            }, 
            {
              "score": 0.599, 
              "class": "weapon"
            }, 
            {
              "score": 0.599, 
              "class": "sports equipment"
            }, 
            {
              "score": 0.893, 
              "class": "gray color"
            }, 
            {
              "score": 0.581, 
              "class": "ash grey color"
            }
          ], 
          "classifier_id": "default", 
          "name": "default"
        }
      ]
    }, 
    {
      "image": "LieOrStand2.zip/C.jpg", 
      "classifiers": [
        {
          "classes": [
            {
              "score": 0.823, 
              "class": "Erect"
            }
          ], 
          "classifier_id": "RemoteTriage_482484271", 
          "name": "Remote Triage"
        }, 
        {
          "classes": [
            {
              "score": 0.851, 
              "class": "Parkour", 
              "type_hierarchy": "/sport/Parkour"
            }, 
            {
              "score": 0.851, 
              "class": "sport"
            }, 
            {
              "score": 0.5, 
              "class": "nylons", 
              "type_hierarchy": "/hosiery/nylons"
            }, 
            {
              "score": 0.508, 
              "class": "hosiery"
            }, 
            {
              "score": 0.793, 
              "class": "footwear"
            }, 
            {
              "score": 0.8, 
              "class": "clothing"
            }, 
            {
              "score": 0.923, 
              "class": "charcoal color"
            }, 
            {
              "score": 0.909, 
              "class": "gray color"
            }
          ], 
          "classifier_id": "default", 
          "name": "default"
        }
      ]
    }, 
    {
      "image": "LieOrStand2.zip/A.jpg", 
      "classifiers": [
        {
          "classes": [
            {
              "score": 0.889, 
              "class": "Erect"
            }
          ], 
          "classifier_id": "RemoteTriage_482484271", 
          "name": "Remote Triage"
        }, 
        {
          "classes": [
            {
              "score": 0.798, 
              "class": "person"
            }, 
            {
              "score": 0.903, 
              "class": "Parkour", 
              "type_hierarchy": "/sport/Parkour"
            }, 
            {
              "score": 0.922, 
              "class": "sport"
            }, 
            {
              "score": 0.5, 
              "class": "skateboarding", 
              "type_hierarchy": "/sport/skating/skateboarding"
            }, 
            {
              "score": 0.502, 
              "class": "skating"
            }, 
            {
              "score": 0.794, 
              "class": "clothing"
            }, 
            {
              "score": 0.964, 
              "class": "gray color"
            }, 
            {
              "score": 0.793, 
              "class": "charcoal color"
            }
          ], 
          "classifier_id": "default", 
          "name": "default"
        }
      ]
    }, 
    {
      "image": "LieOrStand2.zip/D.jpg", 
      "classifiers": [
        {
          "classes": [
            {
              "score": 0.654, 
              "class": "Erect"
            }, 
            {
              "score": 0.622, 
              "class": "Prone"
            }
          ], 
          "classifier_id": "RemoteTriage_482484271", 
          "name": "Remote Triage"
        }, 
        {
          "classes": [
            {
              "score": 0.64, 
              "class": "stocking", 
              "type_hierarchy": "/hosiery/stocking"
            }, 
            {
              "score": 0.725, 
              "class": "hosiery"
            }, 
            {
              "score": 0.561, 
              "class": "boothose", 
              "type_hierarchy": "/hosiery/boothose"
            }, 
            {
              "score": 0.535, 
              "class": "pogo stick"
            }, 
            {
              "score": 0.5, 
              "class": "belt", 
              "type_hierarchy": "/accessory/belt"
            }, 
            {
              "score": 0.501, 
              "class": "accessory"
            }, 
            {
              "score": 0.599, 
              "class": "sport"
            }, 
            {
              "score": 0.599, 
              "class": "knot"
            }, 
            {
              "score": 0.601, 
              "class": "clothing"
            }, 
            {
              "score": 0.633, 
              "class": "maroon color"
            }, 
            {
              "score": 0.512, 
              "class": "purple color"
            }
          ], 
          "classifier_id": "default", 
          "name": "default"
        }
      ]
    }, 
    {
      "image": "LieOrStand2.zip/B.jpg", 
      "classifiers": [
        {
          "classes": [
            {
              "score": 0.868, 
              "class": "Erect"
            }
          ], 
          "classifier_id": "RemoteTriage_482484271", 
          "name": "Remote Triage"
        }, 
        {
          "classes": [
            {
              "score": 0.597, 
              "class": "ramp", 
              "type_hierarchy": "/mechanical device/machine/inclined plane/ramp"
            }, 
            {
              "score": 0.597, 
              "class": "inclined plane"
            }, 
            {
              "score": 0.598, 
              "class": "machine"
            }, 
            {
              "score": 0.602, 
              "class": "mechanical device"
            }, 
            {
              "score": 0.544, 
              "class": "khukuri (knife)", 
              "type_hierarchy": "/weapon/knife/khukuri (knife)"
            }, 
            {
              "score": 0.545, 
              "class": "knife"
            }, 
            {
              "score": 0.556, 
              "class": "weapon"
            }, 
            {
              "score": 0.511, 
              "class": "Repairing"
            }, 
            {
              "score": 0.51, 
              "class": "Earthquake"
            }, 
            {
              "score": 0.5, 
              "class": "stoop", 
              "type_hierarchy": "/porch/stoop"
            }, 
            {
              "score": 0.5, 
              "class": "porch"
            }, 
            {
              "score": 0.597, 
              "class": "lever"
            }, 
            {
              "score": 0.98, 
              "class": "gray color"
            }
          ], 
          "classifier_id": "default", 
          "name": "default"
        }
      ]
    }
  ], 
  "custom_classes": 3, 
  "images_processed": 5
}


for im in results['images']:
    print(' ')
    fileparts = os.path.split(im['image'])
    filename = fileparts[1]
    print(filename)
    overlay = ''
    for clasf in im['classifiers']:
        clasf_name = clasf['name']
        if clasf_name is 'Remote Triage':
            for item in clasf['classes']:
                if item['class'] is 'Prone':
                    overlay = 'Prone person probability (%f%%)' % (item['score'] * 100.0)
                    print('Prone person probability ({}%)'.format(item['score'] * 100.0))
    show_image('LieOrStand2/' + filename, overlay)
            
