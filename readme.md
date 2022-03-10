# Toy Robot

A simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no other obstructions on the table surface. The robot is free to roam around the surface of the table, but is prevented from falling to destruction. Any movement that would result in the robot falling from the table is prevented,
however further valid movement commands are still allowed.

## Build

### Install [Python 3](https://www.python.org/) (and [pip](http://www.pip-installer.org))

[Python 3.10 is required for using *match*.](https://medium.com/short-bits/python-3-10-match-a-new-way-to-find-patterns-8452d1460407) 

### Start a Python [virtual environment](https://virtualenv.pypa.io/en/latest/) and Install the Requirements

```sh
pip3 install virtualenv
virtualenv env
source env/bin/activate
# or '. env/bin/activate' if running sh as shell with FreeBSD for example
# or 'env\Scripts\activate' with Windows
pip3 install -r requirements.txt
```

## Test

```sh
python test.py
```

## Run

### Run the Console App Interactively

```sh
python .
```

### Run the Console App with Commands from Text Files

```sh
python . input/a.txt
python . input/b.txt
python . input/c.txt
```
