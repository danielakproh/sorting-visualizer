# Setting up

This guide is to quickly get started using the sorting visualizer app from a fresh machine perspective. If for some reason things aren't working out, please feel free to [open an issue](https://github.com/danielakproh/sorting-visualizer/issues).

## Download & Install Python 3

Feel free to skip this step if you already have Python 3+ installed on your machine.

### Download
You can download Python for free on the Python official website [here](https://www.python.org/downloads/). To ensure that you don't run into issues, it is recommended to download a version above `3.5`

### Install
Having Python downloaded, now we need to install it.

* Run the Python executable installer file (downloaded in previous step)
* Add Python to PATH and launch installation

### verification
To verify that Python was installed successfully:

Open Command Prompt and run the following

```
$python
```
if you followed everything correctly you should see the following output

```
Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Python comes with a package management system called `pip` which will help with installing third-party libraries. To Ensure that it was was successfully installed, run `$ pip --version` into your terminal window. The following output confirms that pip is installed on your system:

```
$ pip --version
pip 21.2.4 from c:\users\admin\programs\python\python39\lib\site-packages\pip (python 3.9)
```

### debugging
If you encounter any error when following this guide, I have linked some helpful resources down below that you can check out, hopefully they will help you troubleshoot and solve the issue.

## Clone the repo

Run the following command in your Git Bash terminal to clone the project

```
$ cd path/to/folder
$ git clone https://github.com/danielakproh/sorting-visualizer.git .
```

## Install the dependencies
This is an important step. Run the following command in order to install the dependencies required to run the application:

```shell
$ pip install -r requirements/requirements.txt
```


## Running the app
You can now run the app and even be creative and add your own features! Run the following command to run the app

```
$ cd path/to/folder
$ python main.py
```

