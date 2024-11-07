# MAC


# Install Python 3.10 via python.org
https://www.python.org/downloads/macos/# Move to your python virtual environment directory 

# Move to your virtual environment directory
```
cd /Users/karine/Documents/virtual_env

# create a new one for Snooz:
```
python3.10 -m venv snooz_310_env
```

# Activate it
```
source snooz_310_env/bin/activate
```

# Move to your scinode_poc repository directory 
```
cd /Users/karine/Documents/gitRepos/ceams-carsm/Stand_alone_apps/scinodes_poc
```

>From this point all pip command will install the python packages within your new virtual environment

# From the root of the Snooz directory install all python package from the requirements file.
> If you need to create an installer.
```
pip install /Users/karine/Documents/software/fbs-0.9.8.tar
pip install -r ./requirements/mac.txt
```

# Manual install of pip modules

```
pip install QtPy~=2.3.1
pip install PySide2~=5.15.2.1
pip install ascii-canvas~=1.3.5
pip install pyEDFlib~=0.1.32
pip install scikit-learn~=1.2.2
pip install pandas~=2.0.1
pip install matplotlib~=3.7.1
pip install tqdm~=4.65.0
```

# Create the installer
```
fbs clean
fbs freeze
fbs installer
```
## to try the executable
target/Snooz.app/Contents/MacOS/Snooz

## Possible errors
ImportError: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.29' not found
```
sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test
sudo apt install -y g++-11
```

Could not find any of the following files:

 * libpython3.10m.so.1.0
 * libpython3.10.so
 * libpython3.10m.so
 * libpython3.10mu.so.1.0
 * libpython3.10.so.1.0
```
sudo apt install -y libpython3.10
```
FileNotFoundError: fbs could not find executable 'fpm'. Please install fpm using the instructions at https://fpm.readthedocs.io/en/latest/installing.html.

https://fpm.readthedocs.io/en/v1.15.1/installation.html

```
sudo gem install fpm
fpm --version

