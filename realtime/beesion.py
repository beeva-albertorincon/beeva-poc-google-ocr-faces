# encode:utf8
import os
import io
from google.cloud import vision
from google.cloud.vision import types

import pylab as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

import face_recognition as fk
from skimage.transform import resize

import time
import re

import logging
logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

def detect_text_front(encoded_image):
    """Detects text in the captured video."""
    res = None
    client = vision.ImageAnnotatorClient()
    image = types.Image(content=encoded_image)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    if texts:
        text = texts[0].description
        logging.info(text.split())
        if 'APELLIDOS' in text:
            surname1,surname2 = text.split("APELLIDOS")[1].split()[0:2]
        else:
            surname1 = text.split("PRIMER APELLIDO")[1].split()[0]
            surname2 = text.split("SEGUNDO APELLIDO")[1].split()[0]
        name = text.split("NOMBRE")[1].split()[0]
        # birth = "-".join(text.split("FECHA DE NACIMIENTO")[1].split()[0:3])
        # dni = text.split("DNI")[1].split()[0:10]
        logging.info(name)
        logging.info('%s %s' %(surname1, surname2))
        res = name,surname1,surname2 #,birth, dni
    else:
        print("No text detected!")
    return res

def detect_text_real_time(encoded_image):
    """Detects text in the captured video."""
    client = vision.ImageAnnotatorClient()
    image = types.Image(content=encoded_image)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    name_info = None
    if texts:
        logging.info(texts[0].description)
        text = texts[0].description.replace('0','O', -1)
        words = text.split()
        regex = re.compile('[^a-zA-Z]')
        name_info = regex.sub(" ", words[-1]).split()
        logging.info(name_info)
    else:
        logging.info("No text detected!")
    return name_info

def detect_text_in_file(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    for text in texts:
        print('\n"{}"'.format(text.description))

def detect_faces(encoded_image):
    """Detects faces in an image."""
    client = vision.ImageAnnotatorClient()

    image = types.Image(content=encoded_image)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    res = list()
    for face in faces:

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])
        vertices_int = [(vertex.x,vertex.y) for vertex in face.bounding_poly.vertices]

        x = int(vertices_int[0][0])
        y = int(vertices_int[0][1])
        width = np.absolute(int(vertices_int[0][0]) - int(vertices_int[1][0]))
        height = np.absolute(int(vertices_int[0][1]) - int(vertices_int[2][1]))
        res.append((x,y,width,height))
    return res

def verify_face(image1,image2):
    """
    Check if detected faces belongs to the same person.
    """
    res = None
    try:
        encoding1 = fk.face_encodings(image1)[0]
        encoding2 = fk.face_encodings(image2)[0]
        res = fk.compare_faces([encoding1], encoding2, tolerance=0.6)
    except Exception as e:
        logging.error("Error: %s" %e)
    return res

def detect_faces_offline(encoded_image):
    """
    Detect faces without calling any external service.
    """
    locations = fk.face_locations(encoded_image)
    return locations
