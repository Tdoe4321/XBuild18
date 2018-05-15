Overview
--------
We created this project in 24 hours for the XBuild 2018 Hackathon. 

Inspiration
-----------

We considered a use case of a trainwreck with hazardous materials and the requirement to do rapid remote triage. This drove us to try and find an innovative way to control a drone with limited dexterity that is common with Hazmat and similar anti-exposure suits.

What it does
------------

*   Drone is launched and controlled using Myo armband interfaced with Flytbase to arrive at disaster site
*   Photos from the drone are tagged with location metadata and sent from mission computer (raspberry pi) via data links to the IBM Cloud (Watson)
*   Watson uses Generic and Remote Triage custom classifier to assess the image for initial triage (prone, sitting, standing)
*   Scene intelligence then pushed to on-scene commander for allocation of resources ## How we built it FlytBase - used Navigation and Telemetry APIs to control and simulate drone
*   IBM Watson Visual Recognition Engine - Trained custom classifier to recognize prone, erect or sitting persons.
*   Python - main programming language used to glue everything together.
*   OpenCV - used to create and display intelligence overlays
*   Myo Armband - used to control drone functions
*   Drone - simulated with FlytBase Sim ## Challenges we ran into Some of the challenges that we ran into were getting the Watson IBM to classify our data correctly. None of us had ever used anything like that before so it was quite a challenge. There is a limited dataset of casualty imagery from drones. We also had a bit of difficulty with programming languages and systems not overlapping. We wanted to do most of our development in the Linux environment, but the Myo Armband's SDK only works in the Windows environment. ## Accomplishments that we're proud of Great team photo! Great teamwork! ## What we learned We learned quite a bit. Watson integration was a huge part of this project and, now that we know how to create classifiers, we can do all kinds of things with that. We also learned all about Quaternions and how to classify rotational data with the Myo Armband. Learning about how emergency response works was also really interesting ## What's next for Drone Dr - Remote Triage
*   Modify Marine Maker (MD5) Nibbler 2 Drone with code to perform rapid remote triage
*   Implement automatic scene segmentation of captured images
*   Update and expand Remote Triage custom classifier
*   Assess purposeful movement from video (SALT Step 1 - Assess 2nd)
*   Perform Individual Assessment (SALT Step 2) with IR camera to ascertain respiration rates and major hemorrhages
*   Report victim locations with triage assessment on map
*   Enable drone swarm control

Built With
----------

*   [python](https://devpost.com/software/built-with/python)
*   flytbase
*   [ibm-watson](https://devpost.com/software/built-with/ibm-watson)
*   [opencv](https://devpost.com/software/built-with/opencv)
*   [myo](https://devpost.com/software/built-with/myo)
*   drone
