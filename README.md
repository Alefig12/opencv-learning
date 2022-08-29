# OpenCV learning roadmap

Here I will document my OpenCV learning path, feel free to follow this roadmap for you to learn OpenCV! 

## Table of contents
* [Day 1: Learning the basics of image, video and color in OpenCV](#Day-1)
* [Day 2: Learning about contours, drawing functions and color tracking](#Day-2)
* [Day 3: Image operations and object counter with different methods](#Day-3)
* [Day 4: Object counter with another method, movement detector and making myself invisible](#Day-4)
* [Day 5: Face detector and shape-color detector](#Day-5)
* [Day 6: Blurring faces with haar cascades](#Day-6)
* [Day 7: Bulk saving images of faces and training a face recognizer model](#Day-7)
* [Day 8: Virtual pen to draw on screen](#Day-8)
* [Day 9: Color highlighter, perspective transformation and OCR document scanner](#Day-9)
* [Day 10: Area movement detector and counting cars on a highway with background subtraction](#Day-10)
* [Day 11: ](#Day-11)

## Description of what I learnt each day.

**NOTE**: You can read in detail each day by opening each folder of the corresponding day or clicking the day down below. 

### [Day 1](day01)

This day I went through the basics of reading, writing and showing image and video from a source or webcam, also an introduction to color spaces and how color works in openCV as well as thresholding and color detection.

### [Day 2](day02)

This day I learnt about how to get the contours of an image and draw them into the main frame, also about the different drawing functions like text, circle, lines and rectangles and finally a little program that can tell if a specific color is on the screen and draw its border.

### [Day 3](day03)

Today was about some image operations like adding images, substracting them and the bitwise methods, ending with 2 programs that count objects applying different methods like binary thresholding or edge detection with canny.

### [Day 4](day04)

These programs were all about experimentations of the many things we can achieve using OpenCV with simple image manipulation. Following the last day, I made an object counter but this time based on color detection then a basic movement detector and finally a program that can make myself invisible using an invisibility cloak!


### [Day 5](day05)

An introduction to haar cascades and OpenCV's pre-trained models, this one is a face detector, also a program that identifies shape and its color and writes it on top of it.

### [Day 6](day06)

We take haar cascades from last day and apply them to a program that identifies faces from an image or video and blurs them according to a trackbar 

### [Day 7](day07)

We keep using face detection with haar cascades to make a program that automatically recognize, crop and save images of each individual face from people in the picture or video, lastly we train a model with those faces saved to now be able to recognize and label them in different pictures or videos.


### [Day 8](day08)

Creating a program that recognizes a certain color to be able to draw on screen with its movement, basically a virtual pen.

### [Day 9](day09)

First we create a program that only highlights the color blue on a grayscale output, then we learn about perspective transformation and use it to finally build a program that scans for documents and apply OCR to it to get the content inside of it!

### [Day 10](day10)

Today we learn about the different background subtractor methods available in OpenCV and use them to create a movement detector on a selected area and a counter of cars passing by on a highway
