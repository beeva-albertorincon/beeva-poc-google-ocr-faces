# Proof of concept: People registration

#### Alberto Rincón Borreguero

## Description of the problem

Ferrovial's headquarters are frequently crowded due to the racking of employees and guests. Those who are not registered on the access control system, must show their personal IDs to the recepcionist that will then check if they are allowed to enter the building. Actually, the process requires to store some information on the system that is manually inserted by the recepcionist.

In order to acelerate the access to Ferrovial's headquarters, it is proposed a system that automatically registers a person by taking a picture of a personal ID. Furthermore, if the person is already signed up, there will be a camera that will automatically verify it and allow the person to enter.

```
Two main techniques will be applied:

- OCR (Optimal character recognition)
- Face verification
```

## Proof of concept

The aim is to check the feasibility of the application of OCR techniques over personal IDs.
In addition to this, the system must be able to verify the faces allowed to enter the building.

## Technologies

In order to accomplish the task, the following technologies have been used:

#### Google's Vision API

External service that performs OCR very accurately
In addition, it gives bounding boxes for face recognition.

#### face_recognition

Python's library that helps on face recognition and verification.

## Results

Due to privacy reasons, images will not be shown.

Instead, results are reproducible with the code in the [repository](TODO)


## Outcome

In code folder the generated files can be found.

This is the list of them with a brief explanation:

- [beesion.py](): Helper module that encapsulates many of the main operations
- [demo.py](): Can be run with ```python demo.py``` and will show camera record with face verification activated. Database of face encodings must be is on the folder *encodings*. Press *'q'* to unfreeze the image.
- [run_ocr.py](): Camera record with OCR that runs when the key *'c'* is pressed. Press *'q'* to unfreeze.
- [register.py](): Camera record that stores in database the face encoding detected when pressed *'c'* key.
