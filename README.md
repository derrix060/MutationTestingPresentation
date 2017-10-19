# Practical Mutation Test

This repository was create to show how mutation test works, and to discuss about when and how to use it.

Is it possible also comparing this approach with code coverage (more popular)

## Instructions

As it was written in Python3, it needs it installed. I will demonstrate the installation to a Linux Enviroment.

### Installing Python3

The first step is check if you have python3 installed, and if no, download it.

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

### Virtual Enviroment

This step is not essencial, but is recommended.

I will show how to install the conda virtualenv (more specific the Miniconda)

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

#### Creating a new virtual env

Now create a new virtualenv. I will show how to do with conda

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



#### Activating this virtual env

After create you can "enter" in this env

```bash

$ source activate mutationTestEnv
(mutationTestEnv)  {user}@{group} {folder} $
```

