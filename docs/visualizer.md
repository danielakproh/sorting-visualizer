#class `Visualizer`

## Purpose

This documentation should serve as an introduction to anyone wanting to implement features to the **Visualizer** class or seeking to understand the system at a deeper level. This page covers the class capabilities as well as its function and variable components.  

## Abstract
> The sorting visualizer is a software tool built to help visualize each step of any sorting algorithm's execution. Its main purpose is to help learn sorting algorithms in a more intuitive & visual way. This project is written using the [Pygame](https:www.pygame.org) library as it provides the necessary set of tools to get up and running with drawing graphics in Python. The core of this software tool is the **Visualizer** class which is responsible for mainly handling the application UI.

This class is written in a way that makes customisation easier while maintaining code readability and organization.
 
## Class Variables
class variables are used here to keep track of states throughout the application lifetime. This section will give you a quick overview of how they are used throughout the application. A table giving a generic description of each class variable is as below:

<table>
<!-- head -->
  <tr style="text-align: center">
    <td><h3>Variable<h3></td>
    <td><h3>Description</h3></td>
  </tr>
<!-- screen attributes -->
  <tr style="text-align: center">
    <td colspan="2"><h3>Screen Attributes<h3></td>
  </tr>
  <tr>
    <td><code>SCREEN_WIDTH</code></td>
    <td>an integer representing the width of the main window</td>
  </tr>
  <tr>
    <td><code>SCREEN_HEIGHT</code></td>
    <td>an integer representing the height of the main window</td>
  </tr>
  <tr>
    <td><code>FPS</code></td>
    <td>an integer representing the screen refresh rate in Frames per Second</td>
  </tr>
  <tr>
    <td><code>BACKGROUND_COLOR</code></td>
    <td>the main window's background color</td>
  </tr>
  <tr>
    <td><code>DISPLAY_WIDTH</code></td>
    <td>the width of the main window</td>
  </tr>

<!-- fonts -->
  <tr style="text-align: center; justify-content: center">
    <td colspan="2"><h3>Fonts<h3></td>
  </tr>
  <tr>
    <td><code>ARIAL_20</code></td>
    <td>[Pygame Font] of style Arial and size 20 pixels</td>
  </tr>
  <tr>
    <td><code>ARIAL_30</code></td>
    <td>[Pygame Font] of style Arial and size 30 pixels</td>
  </tr>

<!-- boolean -->
  <tr style="text-align: center">
    <td colspan="2"><h3>Boolean<h3></td>
  </tr>
  <tr>
    <td><code>IS_SORTING</code></td>
    <td>boolean value that's set to <strong>True</strong> when sorting is taking place</td>
  </tr>
  <tr>
    <td><code>UPDATE_TIMER</code></td>
    <td>boolean value acting as a stopwatch for measuring the execution time of an algorithm. <code>True</code> starts the timer and <code>False</code> stops it. It generally <code>IS_SORTING</code> and <code>UPDATE_TIMER</code> generally switch simultaneously</td>
  </tr>

<!-- others -->
  <tr style="text-align: center">
    <td colspan="2"><h3>Others<h3></td>
  </tr>
  <tr>
    <td><code>elapsed_time</code></td>
    <td>an integer representing execution timer in seconds</td>
  </tr>
  <tr>
    <td><code>number_of_rectangles</code></td>
    <td>an integer representing initial number of rectangles to be drawn. Some controls to modify this value are implemented.</td>
  </tr>
  <tr>
    <td><code>algorithm</code></td>
    <td>function caller. When user selects the algorithm of their choice, for example bubble sort, its value goes from <code>None</code> to <code>bubble_sort</code>, which will then call the <a><code>bubble_sort()</code></a> when user presses play.</td>
  </tr>
  <tr>
    <td><code>algorithm_name_display</code></td>
    <td>the name of the algorithm selects, which is dsplayed on the screen</td>
  </tr>
  <tr>
    <td><code>sorting_algorithm_generator</code></td>
    <td>iterator generator. Used to trigger the next iteration in a sequence that <code>Yield</code> a certain value. <a>Learn more</a> about generators in Python.</td>
  </tr>
</table>

<br>

<!-- Class functions  -->
## Class Functions

### **Visualizer.`setup_ui`(*display_width*, *display_height*)**
setup main application window

>### **Parameters**
>* **display_width** (int)
>* **display_height** (int)

<table>
 <tr>
    <td><h4>Return</h4></td>
    <td><h3><code>None</code><h3></td>
  </tr>
</table>

<!-- >#### **References**
><a>https://www.example.com</a> -->

<br>

### **Visualizer.`position_text`(*display*, *font*, *text*, *color*, *pos_x*, *pos_y*)**
quick & easy way to position text onto main display in a single call

>### **Parameters**
>* **display** (pygame.Surface)
>* **font** (pygame.Surface)
>* **text** (str): text to render
>* **color** (pygame.Color)
>* **pos_x** (int): text surface's topleft x position, if None is passed, text will be centered
>* **pos_y** (int): text surface's topleft y position

<table>
 <tr>
    <td><h4>Return</h4></td>
    <td>surface object</td>
  </tr>
  <tr>
    <td><h4>Return type</h4></td>
    <td><h3><code>pygame.Surface</code><h3></td>
  </tr>
</table>

<br>

### **Visualizer.`display_algorithm_menu`(*display*)**
display algorithm selection menu

>### **Parameters**
>* **display** (pygame.Surface)

<table>
 <tr>
    <td><h4>Return</h4></td>
    <td><h3><code>None</code><h3></td>
  </tr>
</table>

<br>

### **Visualizer.`display_app_info`(*algorithm_name*, *runtime*)**
display useful information to the user

>### **Parameters**
>* **algorithm_name** (str): the name of the sorting algorithm
>* **runtime** (int): the total time of execution

<table>
 <tr>
    <td><h4>Return</h4></td>
    <td><h3><code>None</code><h3></td>
  </tr>
</table>

<br>

### **Visualizer.`generate_rectangle_heights`(*number_of_rectangles*)**
generate list of random values which will be used as heights for the rectangles

>### **Parameters**
>* **number_of_rectangles** (int): desired number of rectangles to be drawn

<table>
 <tr>
    <td><h4>Return</h4></td>
    <td>list of random heights values</td>
  </tr>
  <tr>
    <td><h4>Return type</h4></td>
    <td><h3><code>list</code><h3></td>
  </tr>
</table>

<br>

### **Visualizer.`draw_rectangles`(*display*, *screen_width*, *screen_height*, *number_of_rectangles*, *heights_list*, *color_list*)**
draw rectangles onto the screen

>### **Parameters**
>* **display** (pygame.Surface): application's main display surface
>* **screen_width** (int): display surface width
>* **screen_height** (int): display surface height
>* **number_of_rectangles** (int)
>* **heights_list** (list)
>* **color_list** (list[pygame.Color]): variation of colors to fill rectangles

<table>
 <tr>
    <td><h4>Return</h4></td>
    <td>list of random heights values</td>
  </tr>
  <tr>
    <td><h4>Return type</h4></td>
    <td><h3><code>list</code><h3></td>
  </tr>
</table>

<br>

### **Visualizer.`update_display`()**
udpate text data and any change regarding the rectangles such has how many to draw and changes in position

<table>
 <tr>
    <td><h4>Return</h4></td>
    <td><h3><code>None</code><h3></td>
  </tr>
</table>













