import os
import io
from google.cloud import vision
from google.cloud.vision import types


class OCR(object):
    """docstring fo OCR."""
    def __init__(self):
        super(OCR, self).__init__()

    def detect_text(path):
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
