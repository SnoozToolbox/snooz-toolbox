# Read me to create the Snooz installer

## On windows 

Install NSIS (full installation) : https://sourceforge.net/projects/nsis/

Install windows-10-sdk : https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/

Add the paths in the variable environments PATH:
- C:\Program Files (x86)\NSIS\Bin
- C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\

Reboot


## Update your python environment for FBS pro
    Purchase, register, and download FBS Pro from the official website.
    If you need more information or assistance, contact us at snooztoolbox.cnmtl@ssss.gouv.qc.ca.
### Activate the virtual environment
    Windows
	$ call path_to_env\snooz_310_env\Scripts\activate.bat
    Linux/MAC
    $ source path_to_env/snooz_310_env/bin/activate
### Install FBS pro in your pyhton environment
	(snooz_310_env) $ pip3 install path_to_fbs_pro\fbs_pro-0.9.8.tar.gz

## Update the snooz version in base.json
    Edit /snooz-toolbox-ceams/src/build/settings/base.json
    and update the version i.e. "version": "1.2.0",

## Remove any __pycache__ folders and .pyc/.pyo files from the packages
### Open a git bash terminal on Windows or a regular terminal on Linux and macOS
    cd snooz-package-ceams
    find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf

## Release a ceams-package if needed
### In the vscode terminal
    (snooz_310_env) $cd snooz-package-ceams
    (snooz_310_env) $python .\main_utils.py
    (snooz_310_env) $6- Create a release package
    Move the packages into snooz-toolbox-ceams/src/main/resources/

## Push your modifications

## Update your Snooz config to set "is_dev" to False
    Open snooz-toolbox-ceams/src/main/python/config.py
    set is_dev=False
    -> the set is_dev=False should not be pushed on the repository.  

## Create the installer (not needed for developers)
    Open a terminal (windows command prompt or native terminal) in your scinode_poc repository
    Activate your python environment snooz_310_env
    (snooz_310_env)$ fbs clean
    (snooz_310_env)$ fbs freeze --debug

## To solve the mne and YASA problem when creating the installer
Please note that those path are not identical in your machines.

### Windows

<details>
Copy manually the mne, lazy_loader and yasa packages (from VScode terminal to have the pyi file and the classification )

```
Remove-Item "C:\Users\klacourse\Documents\snooz_workspace\snooz-toolbox\target\Snooz\_internal\mne" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "C:\Users\klacourse\Documents\snooz_workspace\snooz-toolbox\target\Snooz\_internal\lazy_loader" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "C:\Users\klacourse\Documents\snooz_workspace\snooz-toolbox\target\Snooz\_internal\lspopt" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "C:\Users\klacourse\Documents\snooz_workspace\snooz-toolbox\target\Snooz\_internal\yasa" -Recurse -Force -ErrorAction SilentlyContinue

Copy-Item -Path "C:\Users\klacourse\Documents\snooz_workspace\snooz_310_env\Lib\site-packages\mne" `
        -Destination "C:\Users\klacourse\Documents\snooz_workspace\snooz-toolbox\target\Snooz\_internal\mne" `
        -Recurse -Force
Copy-Item -Path "C:\Users\klacourse\Documents\snooz_workspace\snooz_310_env\Lib\site-packages\lazy_loader" `
        -Destination "C:\Users\klacourse\Documents\snooz_workspace\snooz-toolbox\target\Snooz\_internal\lazy_loader" `
        -Recurse -Force
Copy-Item -Path "C:\Users\klacourse\Documents\snooz_workspace\snooz_310_env\Lib\site-packages\lspopt" `
        -Destination "C:\Users\klacourse\Documents\snooz_workspace\snooz-toolbox\target\Snooz\_internal\lspopt" `
        -Recurse -Force
Copy-Item -Path "C:\Users\klacourse\Documents\snooz_workspace\snooz_310_env\Lib\site-packages\yasa" `
        -Destination "C:\Users\klacourse\Documents\snooz_workspace\snooz-toolbox\target\Snooz\_internal\yasa" `
        -Recurse -Force

```
</details>

### macOS
<details>

Same strategy applied here, remove the dependencies

```
rm -rf /Users/frank/snooz_workspace/snooz-toolbox/target/Snooz/_internal/mne
rm -rf /Users/frank/snooz_workspace/snooz-toolbox/target/Snooz/_internal/lazy_loader
rm -rf /Users/frank/snooz_workspace/snooz-toolbox/target/Snooz/_internal/lspopt
rm -rf /Users/frank/snooz_workspace/snooz-toolbox/target/Snooz/_internal/yasa
```
Copy them back again

```
cp -R /Users/frank/snooz_workspace/snooz_310_env/lib/python3.10/site-packages/mne /Users/frank/snooz_workspace/snooz-toolbox/target/Snooz.app/Contents/Frameworks/mne
cp -R /Users/frank/snooz_workspace/snooz_310_env/lib/python3.10/site-packages/lazy_loader /Users/frank/snooz_workspace/snooz-toolbox/target/Snooz.app/Contents/Frameworks/lazy_loader
cp -R /Users/frank/snooz_workspace/snooz_310_env/lib/python3.10/site-packages/lspopt /Users/frank/snooz_workspace/snooz-toolbox/target/Snooz.app/Contents/Frameworks/lspopt
cp -R /Users/frank/snooz_workspace/snooz_310_env/lib/python3.10/site-packages/yasa /Users/frank/snooz_workspace/snooz-toolbox/target/Snooz.app/Contents/Frameworks/yasa

```
</details>
    (snooz_310_env)$ fbs installer

### To run Scinode and keep logs (usefull when exe does not work properly)
    windows
    (snooz_310_env)$ cmd /K target\Snooz\Snooz.exe
    Mac
    (snooz_310_env)$ target/Snooz.app/Contents/MacOS/Snooz 
    Linux
    (snooz_310_env)$ target/Snooz/Snooz

## The final installer should not be in debug mode, once it is working
    (snooz_310_env)$ fbs clean
    (snooz_310_env)$ fbs freeze
### On macOS manual modification needs to be done before
    (snooz_310_env)$ fbs installer

## Update the about file
    The file "about_notes.txt" is read by Snooz to display the About information.
    The file is saved on backblaze to have the release notes outside the repository :
        to inform the user of a new Snooz release (the latest released version is updated automatically on the installed Snooz)
        to provide an easy way to download the new installer (links are updated automatically on the installed Snooz)
    * For now, the download links are from Karine's google drive.
    
    Sign in to https://www.backblaze.com/
    Update about_notes.txt 
        Update the latest version released : <b>beta-0.3.0</b>
        Update the 3 links to the installer

## To run the installed app in debug mode 
### MAC
    Drag and drop technic
        Locate the application in Finder.
        Right-click the application and select "Show Package Contents."
        Locate the executable file. Typically, this is in Contents → MacOS → Snooz
        Drag that file onto your blank Terminal command line. Hit Enter to launch that program.
        Leave your Terminal window open while you use the application. Quit the application to return to regular Terminal operations.
    Command line
    $ /Applications/Snooz.app/Contents/MacOS/Snooz

# Update the doc
    Update the links to download
        SnoozDoc/user_guide/getting_started.rst


# Specific bug

### On Mac   

#### NSRequiresAquaSystemAppearance  
    You need to manually add the option NSRequiresAquaSystemAppearance at true  
    in Info.plist located in target\Snooz.app\Contents\Info.plist  
    The code is these 2 lines :     
    <key>NSRequiresAquaSystemAppearance</key>
    <string>true</string>

#### Enable secure coding
    You need to manually add the option NSRequiresAquaSystemAppearance at true  
    in Info.plist located in target\Snooz.app\Contents\Info.plist  
    The code is these 2 lines :     
    <key>NSApplicationSupportsSecureRestorableState</key>
    <string>true</string>

Then you can run the installer   
(snooz_310_env)$ fbs installer  

#### DontUseNativeDialog
    The option 'QFileDialog.DontUseNativeDialog' must be off otherwise the linked folder are not well managed in Snooz.

#### Roboto-Regular
missing font family "Roboto-Regular", on macOS, the font family has to be used and it's : Roboto
The famility name "Roboto" also works on windows and linux.

### On linux
#### fpm missing
    FileNotFoundError: fbs could not find executable 'fpm'. Please install fpm using the instructions at https://fpm.readthedocs.io/en/latest/installing.html.
    (snooz_310_env)$ sudo gem install fpm
    (snooz_310_env)$ fpm --version
    if the gem is missing install it before installing the fpm
    (snooz_310_env)$ sudo apt-get update
    (snooz_310_env)$ sudo apt-get install rubygems

    
# Update the requirements when the virtual environment has been updated
go to your local repository of scinode
    (snooz_venv) $ pip3 freeze > requirements.txt

# General information
https://www.learnpyqt.com/tutorials/packaging-pyqt5-apps-fbs/

# How to install on macOS
> download from google drive SnoozSetp_xxx.dmg
> double click on the downloaded SnoozSetp_xxx.dmg
> drag and drop the Snooz application in the Applications folder
> type in the terminal 
`xattr -cr /Applications/Snooz.app`
> type in the terminal 
`/Applications/Snooz.app/Contents/MacOS/Snooz`
warning : wait until Snooz is launched


