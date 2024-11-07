# How to setup your environment to develop within the Snooz platform
There are two repositories to setup for development, Snooz and your own package repository where you'll be doing your work. This procedure will help you setup both and configure them to work together.

Steps summary:
1. Install Python
2. Install Windows 10 SDK
3. Install Git for windows
4. Clone Snooz repository
5. Create the python virtual environment
6. Install all python packages
7. Create and prepare your work repository.
8. Install and configure Microsoft Visual Studio Code


## Install python 3.10.11
Download the binary installer from: https://www.python.org/downloads/release/python-31011/

* Download and execute the executable installer from python.org/downloads/windows/
* Keep the python 3.10 file location
	* to know the exe file location:
		* type "python 3.10" in the windows search
		* right click on the app found -> open file location
		* right click on the link -> open file location
	* Usually C:\Users\UserName\AppData\Local\Programs\Python\Python310
		* example : C:\Users\klacourse\AppData\Local\Programs\Python\Python310\python
* Reboot   

> **_NOTE:_** Note that once the virtual environment will be created, the python path will be linked to the virtual environment:
	example : C:\Users\klacourse\Documents\NGosselin\python_virtual_env\snooz_venv\Scripts\python.exe

## Install Windows 10 SDK
* Install: https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/
* make sure the path is added in the variable environments PATH:
	* C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\
* Reboot

## Install git for windows
* Download and install gitforwindows from : https://gitforwindows.org/

## Clone the Snooz repository (scinode_poc)
This will install the source code for Snooz.
> Make sure you have a bitbucket account: https://bitbucket.org
> Make sure your are added as a team worker (collaborator) on the scinodes_poc repository : 
	https://bitbucket.org/ceamscarsm/workspace/settings/groups

### Download the source code for Snooz (from scinode_poc)
* Launch Git Bash
* In the git bash terminal create your local repository, clone the repository:
	* Go to the remote repository on BitBucket : https://bitbucket.org/ceamscarsm/scinodes_poc/src/master/
	* Click on Clone on the top right corner.
	* Copy the https command line and paste it on the git bash prompt examples : 

			$ cd /c/Users/klacourse/Documents
			$ git clone https://klacourse@bitbucket.org/ceamscarsm/scinodes_poc.git

* Run the script to add the local settings to your git ignore.
		
		$ ./gitignore_local_settings.sh

### Download the source code for plugins in development for Snooz (from ceams_package)
* Launch Git Bash
* In the git bash terminal create your local repository, clone the repository:
	* Go to the remote repository on BitBucket : https://bitbucket.org/ceamscarsm/ceams_package/src/master/
	* Click on Clone on the top right corner.
	* Copy the https command line and paste it on the git bash prompt examples : 

			$ cd /c/Users/klacourse/Documents
			$ git clone https://klacourse@bitbucket.org/ceamscarsm/ceams_package.git

## Create a Pip virtual environment for Snooz
In any other parent folder (not the one from the git repositories), create a python virtual environment.

### 1. Using the Windows Command Prompt
* Go where your are going to save all your virtual environments, for example:

		$ cd C:\Users\klacourse\Documents\NGosselin\python_virtual_env\

* Create the virtual environment with the python 3.10 path:

		$ path_to_python -m venv .\env_name

	For example:

		$ C:\Users\klacourse\AppData\Local\Programs\Python\Python310\python -m venv .\snooz_venv
	> Make sure the snooz_venv has been created (a folder named snooz_venv should be created)

* Activate the virtual environment
	
		$ call path_to_env\activate.bat
	
	examples :
			
		$ call .\snooz_venv\scripts\activate.bat
		$ call C:\Users\klacourse\Documents\NGosselin\python_virtual_env\snooz_venv\scripts\activate.bat  

	> Once the virtual environment is activated, the python exe will be taken from the virtual environment afterwards  
	
	You should see (snooz_venv) in the Command Prompt    
  
### 2. Using the powershell (default terminal in vscode )
* Create your virtual environment (same commands as Windows Command Prompt), example :

		$ cd C:\Users\klacourse\Documents\NGosselin\python_virtual_env\  
		$ C:\Users\klacourse\AppData\Local\Programs\Python\Python310\python -m venv .\snooz_venv  

* activate the virtual environment

		$ .\snooz_venv\scripts\activate  

	If not working try the command below and activate again:  

		$ Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser  

### 3. Using the git bash command prompt  
* Create your virtual environment, example :  

	$ cd /c/Users/klacourse/Documents/NGosselin/python_virtual_env/  
	$ /c/Users/klacourse/AppData/Local/Programs/Python/Python310/python -m venv snooz_venv  

* activate the virtual environment  
	$ source /snooz_venv/Scripts/activate  

> **_NOTE:_** To deactivate (only useful to change the environment)  
	(snooz_venv) $ deactivate  

## Install all python packages manually
* Install all packages with pip:

		(snooz_venv) $ pip3 install QtPy~=2.3.1
		(snooz_venv) $ pip3 install PySide2~=5.15.2.1
		(snooz_venv) $ pip3 install ascii-canvas~=1.3.5
		(snooz_venv) $ pip3 install pyEDFlib~=0.1.32
		(snooz_venv) $ pip3 install scikit-learn~=1.2.2
		(snooz_venv) $ pip3 install pandas~=2.0.1
		(snooz_venv) $ pip3 install matplotlib~=3.7.1
		(snooz_venv) $ pip3 install tqdm~=4.65.0
		(snooz_venv) $ pip3 install fbs~=1.2.1
		(snooz_venv) $ pip3 install PyWavelets~=1.4.1

	> **_NOTE:_** If you install a new package, let us know, to add it in the virtual environment and in the requirements.
		(snooz_venv) $ pip3 freeze > .\path_to_scinode_poc\requirements\windows.txt


## Install all python packages from the requirements
* Install all packages from requirements:  
		(snooz_venv) $ pip3 install pip install -r .\path_to_scinode_poc\requirements\windows.txt  


##  Install and configure Microsoft Visual Studio Code
* Download, install and launch Visual Studio Code from: https://code.visualstudio.com/
* Launch VS Code
* Open folder to the Snooz repository

		File -> Open Folder...

### Create a workspace in VS Code
To be able to debug your code, VS Code needs to know where it's located. 
To do that you need to create a workspace.
* In VS Code, Save your workspace
		File -> Save Workspace as ...
### Add the ceams_package as a folder in the workspace
* In VS Code, add your ceams_package repository folder to the workspace
		File -> Add Folder to Workspace...
* Save your workspace
		File -> Save Workspace ...

### Install VS Code plugins
In VS Code, on the left navigation bar, select the extensions icon that looks like four little boxes.
Search and install the following plugins:
* Python from Microsoft : The pythin interpreter
* Pylance from Microsoft : To see error in the code before running

### Select python interpreter
* View menu -> Command Palette
* Type : Python Select interpreter
* Select at workspace level
* Enter interpreter path ... path_to_snooz\\snooz_venv\\Scripts\\python.exe
* Select the python interpreter for each folder of the workspace

Now you should see your interpreter in the blue line below.	
Click on it and make sure the right python is selected for the scinodes_poc and your package.

### Modify the .vscode/setting.json for your settings
Here an example of settings.json:
	
	{
		"python.defaultInterpreterPath": "C:\\Users\\klacourse\\Documents\\NGosselin\\python_virtual_env\\snooz_venv\\Scripts\\python.exe",
		"python.linting.pylintEnabled": true,
		"python.linting.enabled": true,
		"python.analysis.extraPaths": ["./src/main/python/"],
		"editor.rulers": [80],
		"qtForPython.uic.liveExecution": false,
	}

### Test your installation Snooz
Test the installation by launching the application, in VS Code, press F5 to start Snooz.
#### Add the ceams_package to Snooz
	1. Go in Menu (of Snooz) Tools->Settings->Packages
	2. Press "Add from folder"
	3. Select the root folder of the ceams_package for modules (ceams_package/modules) and ok
	4. Select the root folder of the ceams_package for tools (ceams_package/tools) and ok 


## Setup your work repository for your Modules and Tools package
At this point you can launch and debug Snooz but this is not where your actual work will usually take place. 
You need to create another repository with your own modules and packages and link Snooz to them.

* Fork the "snooz_package_template" repository
	go to : https://bitbucket.org/ceamscarsm/snooz_package_template/src/master/
	click on the ... and fork this repository
	You can rename the repository
* Clone your forked "snooz_package_template" repository
	go to : https://bitbucket.org/[YOUR_USERNAME]/snooz_package_template/src/master/
	* Click on Clone on the top right corner.
	* Copy the https command line and paste it on the git bash prompt examples : 
		$ cd /c/Users/klacourse/Documents
		$ git clone https://klacourse@bitbucket.org/klacourse/snooz_package_template.git
	* Read the README.md in this repository to know how to use it. In short you will:
		* Create an empty package.
		* Add your first module.
		* Add your first step-by-step tool.

### Add your work repository folder to the VS code workspace
* In VS Code, add your work repository folder to the workspace
		File -> Add Folder to Workspace...
* Save your workspace
		File -> Save Workspace as ...

> **_NOTE:_** The next time you launch VS Code, be sure to open your workspace and not just the Snooz folder.

> **_NOTE:_** Pro tips: When debugging a module, it usually work better if you turn off the multithread. 
		
		In the file MainWindow.py of Snooz, set this parameter to False:
		self._use_multithread = False

### Add your package to Snooz
The last step is to add your work packages to Snooz.
* Start Snooz: Run menu -> Start debugging (press F5) or Run without debugging (press ctrl+F5)
* Add your package in Snooz
	1. Go in Menu (of Snooz) Tools->Settings->Packages
	2. Press "Add from folder"
	3. Then select the root folder of the package where the package description.json is located,
		either [YOUR_PACKAGE]/modules or [YOUR_PACKAGE]/tools

The package is now added to Snooz and if it's the latest version it will be selected automatically in the process tab when designing a process.


## Setup VSCODE for the UI

### Install VS Code plugins for UI
In VS Code, on the left navigation bar, select the extensions icon that looks like four little boxes.
Search and install the following plugins:
* Qt For Python from Shuang Wu : User Interface

		Now you should be able to edit and compile .UI files.
		right click on the UI_x.ui -> edit form
		right click on the UI_x.ui -> compile form

### Modify VS code UI settings
In the VSCODE File menu -> preference -> settings
	1. Choose "workspace" tab 
	2. Choose extension in the left panel
	3. Go to "QT for Python "
		Make sure the qtForPython.uic.options is 
			"${resourceDirname}${pathSeparator}${resourceBasenameNoExtension}.py"
			without UI_ in the middle otherwise your UI pyhton file will be renamed
			with an extra UI_ each time you compile the UI.

The command line to compile a ui file
	$ pyside2-uic Ui_X.ui -o Ui_X.py

The compile recursively all the .ui files.
You can create a bash file, i.e. compil_ui.bat
and call it from the windows prompt command line.
	compil_ui.bat:
		@echo off
		for /r %%i in (*.ui) do (
			call :generate_py_file "%%i"
		)
		exit /b

		:generate_py_file
		set "ui_file=%~1"
		set "output_file=%~dpn1.py"
		pyside2-uic "%ui_file%" -o "%output_file%"
		exit /b
	$ call ./ceams_package/toolsCEAMSTools/compil_ui.bat

# How to clean your scinode register key
When you launch Snooz from the Programs Files your package paths are saved in the register keys.
    1. Open Registry Editor (from windows search)
    2. Remove the folder SciNode under HKEY_CURRENT_USER\Software\CEAMS


