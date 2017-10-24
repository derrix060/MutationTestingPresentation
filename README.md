# Practical Mutation Test

This repository was create to show how mutation test works, and to discuss about when and how to use it.

Is it possible also comparing this approach with code coverage (more popular)

## Instructions
## Installation

Here will be shown how to install this repository to a beginer user. Probably there are few steps that you don't need to do. This session will be show in a Linux Enviroment

### Installing `Git`

This repository is versioned using `git`. The first step is install the `git`. 

```bash
$ sudo apt-get install git
```

### Download this repository

If you don't know how to download this repository, just use the command above.

```bash
# Go to the folder that you wanna download this, for example the folder Projects
$ cd ~/Projects

# Dowload, or "clone", the repository
$ git clone https://github.com/derrix060/MutationTestingPresentation.git

# Go to the folder
$ cd MutationTestingPresentation
```

### Installing Python3

As this repository was written in `python3`, you need it installed.

The first step is check if you have `python3` installed, and if no, download it.

```bash
$ python3 --version
Python 3.X.X

# If this message appear, you need to install the python3
command not found: python3
$ sudo apt-get install python3

...

# Now you can check again the installation
$ python3 --version
Python 3.X.X
```

### Virtual Environment

This step is not essencial, but is recommended.


#### Download and install `conda`


Please follow [this tutorial](https://conda.io/docs/user-guide/install/linux.html) to install it on your PC.

After install, check if is it working

```bash
$ conda list
# packages in environment at /home/{user}/miniconda3:
#
asn1crypto                0.22.0                   py36_0  
cffi                      1.10.0                   py36_0  
conda                     4.3.21                   py36_0  
conda-env                 2.6.0                         0  

... 

yaml                      0.1.6                         0  
zlib                      1.2.8                         3

# If this message appear, you need to add the folder in your PATH or copy it to /home/bin
command not found: conda

# To copy it
$ sudo cp {conda folder}/bin/conda /home/bin
$ sudo cp {conda folder}/bin/activate /home/bin
$ sudo cp {conda folder}/bin/deactivate /home/bin

# Now you can test again
$ conda list
```

#### Creating a new virtualenv

Now create a new virtualenv. I will show how to do with `conda`

```bash
# The sintax is this one: $ conda create -n {nameOfEnv} python={version}
# For example:
$ conda create -n mutationTestEnv python=3.6

Fetching package metadata .........
Solving package specifications: .

Package plan for installation in environment /home/mario/miniconda3/envs/mutationTestEnv:

The following NEW packages will be INSTALLED:

    certifi:    2016.2.28-py36_0
    openssl:    1.0.2l-0        
    pip:        9.0.1-py36_1    
    python:     3.6.2-0         
    readline:   6.2-2           
    setuptools: 36.4.0-py36_1   
    sqlite:     3.13.0-0        
    tk:         8.5.18-0        
    wheel:      0.29.0-py36_0   
    xz:         5.2.3-0         
    zlib:       1.2.11-0        

Proceed ([y]/n)? 

#
# To activate this environment, use:
# > source activate mutationTestEnv
#
# To deactivate this environment, use:
# > source deactivate mutationTestEnv
#
```

#### Activating a virtualenv

After create you can "enter" in this env

```bash

$ source activate mutationTestEnv
(mutationTestEnv)  {user}@{group} {folder} $
```

### Installing `PIP`

`PIP` is a package manager. To get the latest `pip` from source, run command
```bash
# Download pip installation script from official site using wget.

$ wget -O- https://bootstrap.pypa.io/get-pip.py | sudo python3
```

### Installing the dependencies)

If you want to use any virtualenv, please make sure that it's activated. 

```bash
$ pip install -r requirements.txt
```

