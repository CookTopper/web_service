# CookTopper Web Service

This is a web application provided by Django, to provide all the data to intelligent stove. The features of this application relate to the mobile and display application, also available in this repository: [CookTopper Mobile](https://github.com/CookTopper/cooktopper_app), [CookTopper Display](https://github.com/CookTopper/display_app)

## Getting Started

### Prerequisites

#### Python

To install Python 3 just update your environment
```shell
    $ sudo apt-get update
    $ sudo apt-get -y upgrade
```

Verify your Python version:
```shell
    $ python3 -V
```

You should see some output like this, but the version of Python 3 depends on your Operational System, (Debian 8 upgrades python to version 3.4.2)

```python
Output
Python 3.4.2
```

#### PIP

The project uses pip to manage python software packages. To install it, just run

```shell
    $ sudo apt-get install -y python3-pip
```

We recommend using pip only in VirtualEnv mode, see more [here]()

Install few more packages to support your python development
```shell
    $ sudo apt-get install build-essential libssl-dev libffi-dev python-dev
```

To verify your pip version, type
```shell
    $ pip3 --version
```

#### VirtualEnv

Virtual environments enable you to have an isolated space on your computer for Python projects, ensuring that each of your projects can have its own set of dependencies that won’t disrupt any of your other projects.

Setting up a programming environment provides us with greater control over our Python projects and over how different versions of packages are handled. This is especially important when working with third-party packages.

To install **venv** run command:

```shell
    $ sudo apt-get install -y python3-venv
```

With this installed, we are ready to create environments. Let’s choose which directory we would like to put our Python programming environments in, or we can create a new directory with mkdir, as in:

```shell
    $ mkdir environments
    $ cd environments
```
Once you are in the directory where you would like the environments to live, you can create an environment by running the following command:

```shell
    $ python3 -m venv my_env
```

To use this envornment, you need to activate it, just do it typing:
```shell
    $ source my_env/bin/activate
```

Your prompt will now be prefixed with the name of your environment, in this case it is called my_env. Depending on what version of Debian Linux you are running, your prefix may look somewhat different, but the name of your environment in parentheses should be the first thing you see on your line:

```shell
(my_env) user@debian:~/environments
```

## Installation

Before we install Django, make sure your Virtual Environment is active (in the above topic).
 
* Clone the repository in a folder
   
* Enter the repository folder
     
Run pip command to install python project dependencies
```shell
    $ pip3 install -r requirements.txt
```
              
A lot of python packages will be installed **_ONLY_** in your virtual environment, including Django.

## Running Project

With all dependencies installed, you must run the application. 

Inside repository folder, (at root) run command
```shell
    $ python3 manage.py runserver 8000
```

You can access the web service at (localhost:8000)

## Built With

* Django REST Framework v3.6.4: [REST Framework](http://www.django-rest-framework.org/)

## Authors

* **Izabela Cristina** [izacristina](https://github.com/izacristina)
* **Igor Ribeiro** [igorribeiroduarte](https://github.com/igorribeiroduarte)
* **Pedro Ivo de Andrade** [freemanpivo](https://github.com/freemanpivo)
