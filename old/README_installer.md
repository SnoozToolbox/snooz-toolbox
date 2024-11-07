# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration


## Download FBS pro 
#### You need to have the fbs pro package, download our version from the link below.
https://drive.google.com/file/d/1U_W8x-fiWi13Y_TlVHNeQ8SQAnFnbKcd/view?usp=sharing

## Install using pip requirements files in a virtual environment
### On linux

#### Install python
Check for the installed version
    $ python --version
    $ sudo apt update
    $ sudo apt install python3.9
File path : /usr/bin/python3.9
Install pip if not already installed
    $ sudo apt install python3-pip

#### Create virtual environment
    $ sudo pip3 install virtualenv
    $ sudo apt install python3.9-venv
Go where your are going to save all your virtual environments, for example:
    /media/DATADRIVE/virtual_env
    $ /usr/bin/python3.9 -m venv ./snooz_venv

#### Activate the environment
    $ source snooz_venv/bin/activate
    $ (snooz_venv)

#### Install all package from the requirements
Go to your scinode_poc repository, for example:
    /media/DATADRIVE/scinodes_poc
    $ (snooz_venv) pip install -r requirements/linux.txt
    ! If it does not work install all packages manually

the fbs installation needs to be excluded from the requirements/linux.txt since there a dependency conflict
pyinstaller does not see the pro version of fbs, then it needs to be install at the end
    $ (snooz_venv) pip install path_to_fbs_pro/fbs_pro-0.9.8.tar.gz
    example : (snooz_venv) pip install /media/DATADRIVE/software/fbs_pro-0.9.8.tar.gz


### On windows
python3 -m venv .\snooz_venv
call .\snooz_venv\scripts\activate.bat
pip install -r requirements\windows.txt


### Tested on Linux
    pip install QtPy~=2.3.1
    pip install PySide2~=5.15.2.1
    pip install ascii-canvas~=1.3.5
    pip install pyEDFlib~=0.1.32
    pip install scikit-learn~=1.2.2
    pip install pandas~=2.0.1
    pip install matplotlib~=3.7.1
    pip install tqdm~=4.65.0

To install QT designer you have an option:
    conda install -c anaconda pyqt
    sudo apt-get install qttools5-dev

You need fsb pro the create the installer
fbs 0.9.8 works only with pyinstaller 3.4 but *pro* works with pyinstaller
    pip install path_to_fbs_pro/fbs_pro-0.9.8.tar.gz

### Tested on MAC
pip install QtPy~=2.3.1
pip install PySide2~=5.15.2.1
pip install ascii-canvas~=1.3.5
pip install pyEDFlib~=0.1.32
pip install scikit-learn~=1.2.2
pip install pandas~=2.0.1
pip install matplotlib~=3.7.1
pip install tqdm~=4.65.0



## Install from scratch in a new pip virtual environment
### On windows 
#### Install NSIS : https://sourceforge.net/projects/nsis/
#### Install: https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/
python3 -m venv .\snooz_venv
call .\snooz_venv\scripts\activate.bat
pip install QtPy~=2.3.1
pip install PySide2~=5.15.2.1
pip install ascii-canvas~=1.3.5
pip install pyEDFlib~=0.1.32
pip install scikit-learn~=1.2.2
pip install pandas~=2.0.1
pip install matplotlib~=3.7.1
pip install tqdm~=4.65.0


## Export the requirements.txt for pip
pip3 freeze > requirements\windows.txt

* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Generating the docs
Install sphinx to generate the docs: https://www.sphinx-doc.org/en/master/usage/installation.html
pip install -U sphinx
pip install sphinx_rtd_theme

## Generate the docs in HTML
cd docs
make html


### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact

# How to use?
## How to add a package to Scinode

1. Go in Menu Tools->Settings->Packages
2. Press "Add from folder"
3. Then select the root folder of the package where the package description.json is located.

The package is now added to Scinode and if it's the latest version it will be selected automatically in the process tab when designing a process.
