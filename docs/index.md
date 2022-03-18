# Welcome to Sorting Visualizer documentation

## Source Code

See [the Github repository]()

## Purpose

This guide is meant to be a mix between formal and explanatory documentation. 

## Synopsis

A Pygame application that helps you understand sorting algorithms in a visual way.

## Introduction

Out of all computer science challenges, sorting happens to be one of the most common a programmer may face. Sorting itself can be done in many different ways going from least to super efficient. The sorting visualizer is a project which purpose is to, as its name states, visualize various types of sorting algorithms. As a programmer it is important to understand the difference in their execution, what makes one better than the other and develop an intuitive way of describing and implementing them, which is what this sorting algorithm project is attempting to deliver to its users.

## Software Requirements & Specifications

To get a general idea of how what the first versions will have as base functionalities, the sorting visualizer consists of a display on which n rectangles of various heights are drawn onto it; they can be rearranged in a new random order when user presses on a defined key. User has the ability to increase and decrease n with a control input (mouse/keyboard). All these controls should be displayed onto the screen in order to make it easy for users to figure out how to use the application. These rectangles will then be able to be sorted in one of the many algorithms we have at our disposal. The selected algorithm name as well as a dynamic chrono of the algorithm’s execution time should be displayed in one of the screen’s corners as a tracker. At each step of the sorting process, the involved elements need to be displayed in different colors to make the execution easy to follow; for example, if two pieces need swapping, they can both be highlighted in red, making it easy for the watcher to notice what is happening. After each sorting execution, user should have access to all the controls from the beginning: generating random list and freedom to shuffle them, ability to increase or decrease their number, run the algorithm on the newly-generated list without having to close and reopen the program.  
This visualizer tool is going to be purely developed in the Python programming language with the Pygame framework. The development process is broken down into the following milestones:


* Setup the main display of the application where all the graphics is going to be drawn
* Draw 2 rectangles on the screen and making sure they center dynamically onto the screen
* Scale number of rectangles up and implement scrolling control for user to increase and decrease them
* Implement a simple swap of two elements without color highlighting
* Implement color highlighting
* Increase number of rectangles and swap more items using simple conditions
* Implement a sorting algorithm and test that it works on a regular list
* Test the algorithm with more inputs
* Implement the algorithm to the GUI
* Abstract the application into classes then test the application
* Add comments and docstrings to clarify ambiguous functions/variables



## Contributing

See [the Github repository]()

## License
[MIT License]()
