# Mutation Testing Presentation

This repository shows one example of mutation test, compare with code coverage metric and finish with a question: [Is the code perfect?](#is-the-code-perfect). It also shows how to install the complete enviroment to run this example from scratch.


## Contents

- [Installation](#installation)
    - [Installing `Git`](#installing-git)
    - [Download this repository](#download-this-repository)
    - [Installing `Python3`](#installing-python3)
    - [Virtual Environment](#virtual-environment)
        - [Download and install `conda`](#download-and-install-conda)
        - [Creating a new virtualenv](#creating-a-new-virtualenv)
        - [Activating a virtualenv](#activating-a-virtualenv)
    - [Installing `PIP`](#installing-pip)
    - [Installing the dependencies](#installing-the-dependencies)
- [Explanation of BankAccount class](#explanation-of-bankaccount-class)
- [Explanation of `Mutation Test`](#explanation-of-mutation-test)
- [Uses](#uses)
    - [Code `coverage`](#code-coverage)
    - [`Mutation`](#mutation)
    - [Eliminating the mutants](#eliminating-the-mutants)
    - [Is the code perfect?](#is-the-code-perfect)

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

### Installing the dependencies

If you want to use any virtualenv, please make sure that it's activated. 

```bash
$ pip install -r requirements.txt
```


## Explanation of BankAccount class

The BankAccount class is a simple class that resume (a lot) how a bank account works. It is able to do some operations:

- Deposit: put money on account
- Withdraw: get the money from the account
- Transfer: from one account to another

This is not the best implementation of one bank account, but is fine enough to show some concepts of the `Mutation Tests`

## Explanation of `Mutation Test`

I will not explain the concepts of `mutation test`, because there are a lot of material online that do this. I recomend see [this pdf, from Stuart Anderson](http://www.inf.ed.ac.uk/teaching/courses/st/2011-12/Resource-folder/09_mutation.pdf) to learn about or [one article from Frank Appel](http://www.codeaffine.com/2015/10/05/what-the-heck-is-mutation-testing/) that show the concepts and some examples using [`JUnit`](http://junit.org) and [`EclEmma`](http://www.eclemma.org/) (really good), frameworks to `Java` language.

## Uses

To generate the mutants, this repository is using the [`cosmic-ray`](https://github.com/sixty-north/cosmic-ray) and [`coverage.py`](https://coverage.readthedocs.io) framework. If you haven't installed this yet, go to [this](#installing-the-dependencies) section.

### Code `coverage`

A code 100% covered is always good? No, this is only one (good) metric, and if is combined with others metrics and techniques, the code will be better.

Use this command to run the tests and generate the report

```bash
# Run the coverage.py

$ coverage run test.py

test_deposit_negative_amount (__main__.BadTestBankAccount) ... ok
test_deposit_positive_amount (__main__.BadTestBankAccount) ... ok
test_transfer_positive_amount (__main__.BadTestBankAccount) ... ok
test_withdraw_from_empty_account (__main__.BadTestBankAccount) ... ok
test_withdraw_negative_amount (__main__.BadTestBankAccount) ... ok
test_withdraw_positive_amount (__main__.BadTestBankAccount) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s


# Now generate the report
$ coverage report

Name      Stmts   Miss  Cover
-----------------------------
bank.py      20      0   100%
test.py      63     22    65%
-----------------------------
TOTAL        83     22    73%
```

As you can see on report, the our BankAccout class (bank py) is 100% covered.

### `Mutation`

Now is the moment that show why this repository was created. If you have any question about this command, please read the [`cosmic-ray` manual](cosmic-ray.readthedocs.io).

```bash
$ cosmic-ray init --test-runner=unittest --baseline=10 example.json bank -- . && cosmic-ray exec example.json && cosmic-ray dump example.json | cr-report
```

The result will be something like this: 

```python
job ID ceb227c5b8394138a0ba82ccdcf83a44:survived:bank
command: cosmic-ray worker bank mutate_comparison_operator 2 unittest -- .
--- mutation diff ---
--- a{your folder}/practical/bank.py
+++ b{your folder}/practical/bank.py
@@ -10,7 +10,7 @@
 
     def deposit(self, amount):
         '\n            Deposit some money in this account.\n        '
-        if (amount <= 0):
+        if (amount < 0):
             raise ValueError('Deposit must be greater than zero!')
         self._balance += amount
 

job ID a935eb2bb00446f9af4e9a1206880ac2:survived:bank
command: cosmic-ray worker bank mutate_comparison_operator 11 unittest -- .
--- mutation diff ---
--- a{your folder}/practical/bank.py
+++ b{your folder}/practical/bank.py
@@ -16,7 +16,7 @@
 
     def withdraw(self, amount):
         '\n            Withdraw some money for this account.\n        '
-        if (amount <= 0):
+        if (amount < 0):
             raise ValueError('Withdraw must be greater than zero!')
         if (amount <= self._balance):
             self._balance -= amount

job ID 9e1ceb756747497f868f00f0010caea5:survived:bank
command: cosmic-ray worker bank mutate_comparison_operator 20 unittest -- .
--- mutation diff ---
--- a{your folder}/practical/bank.py
+++ b{your folder}/practical/bank.py
@@ -18,7 +18,7 @@
         '\n            Withdraw some money for this account.\n        '
         if (amount <= 0):
             raise ValueError('Withdraw must be greater than zero!')
-        if (amount <= self._balance):
+        if (amount < self._balance):
             self._balance -= amount
             return True
         else:

job ID 2e68a9f0ddc3430486833dc42e480ad4:survived:bank
command: cosmic-ray worker bank number_replacer 0 unittest -- .
--- mutation diff ---
--- a{your folder}/practical/bank.py
+++ b{your folder}/practical/bank.py
@@ -10,7 +10,7 @@
 
     def deposit(self, amount):
         '\n            Deposit some money in this account.\n        '
-        if (amount <= 0):
+        if (amount <= 1):
             raise ValueError('Deposit must be greater than zero!')
         self._balance += amount
 

job ID 55f9c09099eb491a97c40d8091ac3c51:survived:bank
command: cosmic-ray worker bank number_replacer 1 unittest -- .
--- mutation diff ---
--- a{your folder}/practical/bank.py
+++ b{your folder}/practical/bank.py
@@ -16,7 +16,7 @@
 
     def withdraw(self, amount):
         '\n            Withdraw some money for this account.\n        '
-        if (amount <= 0):
+        if (amount <= 1):
             raise ValueError('Withdraw must be greater than zero!')
         if (amount <= self._balance):
             self._balance -= amount

total jobs: 34
complete: 34 (100.00%)
survival rate: 14.71%

```

As you can see at the last line, the survival rate is 14.71%, in other words, this amount was the number of mutants that was not detected by the tests.

If you don't know about the concepts, please look [here](#explanation-of-mutation-test). Resuming, this number is saying that there are some "mistakes" that any programmer can do in the code, that will not be catched on the tests. One of the use from tests, is take this kind of situations, and, as you could see, didn't work.

#### Eliminating the mutants

I've already done this job for you. Just comment the [line 42](https://github.com/derrix060/MutationTestingPresentation/blob/master/test.py#L42) and uncomment the [line 43](https://github.com/derrix060/MutationTestingPresentation/blob/master/test.py#L43) of the test file.

If you run again the command for `cosmic-ray`, you can see that the result now is different.

```bash
$ cosmic-ray init --test-runner=unittest --baseline=10 example.json bank -- . && cosmic-ray exec example.json && cosmic-ray dump example.json | cr-report

total jobs: 34
complete: 34 (100.00%)
survival rate: 0.00%
```

### Is the code perfect?

Now, our code is with 100% of coverage and 100% of mutants killeds. Is our code perfect? No, and I will show why.

If we write one test that try to transfer more money that one account has, we can see that it will happen (not expected) !!

One example is write this function on [test.py](https://github.com/derrix060/MutationTestingPresentation/blob/master/test.py):

```python
def test_transfer_more_than_available_balance(self):
    self.account_1.transfer_to(self.account_2, 150)

    self.assertEqual(self.account_1._balance, 100)
    self.assertEqual(self.account_2._balance, 10)
```

If you try to run the `cosmic-ray`, one error will be shown. To check the error, is easier try to do only the unittest:

```bash
$ python test.py


test_deposit_negative_amount (__main__.BadTestBankAccount) ... ok
test_deposit_positive_amount (__main__.BadTestBankAccount) ... ok
test_transfer_positive_amount (__main__.BadTestBankAccount) ... ok
test_withdraw_from_empty_account (__main__.BadTestBankAccount) ... ok
test_withdraw_negative_amount (__main__.BadTestBankAccount) ... ok
test_withdraw_positive_amount (__main__.BadTestBankAccount) ... ok
test_blank (__main__.GoodTestBankAccount) ... ok
test_deposit_minimum_amount (__main__.GoodTestBankAccount) ... ok
test_deposit_zero_amount (__main__.GoodTestBankAccount) ... ok
test_transfer_more_than_available_balance (__main__.GoodTestBankAccount) ... FAIL
test_transfer_negative_amount (__main__.GoodTestBankAccount) ... ok
test_withdraw_maximum_amount (__main__.GoodTestBankAccount) ... ok
test_withdraw_positive_amount_max (__main__.GoodTestBankAccount) ... ok
test_withdraw_positive_amount_min (__main__.GoodTestBankAccount) ... ok
test_withdraw_zero_amount (__main__.GoodTestBankAccount) ... ok

======================================================================
FAIL: test_transfer_more_than_available_balance (__main__.GoodTestBankAccount)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test.py", line 93, in test_transfer_more_than_available_balance
    self.assertEqual(self.account_2._balance, 10)
AssertionError: 160 != 10

----------------------------------------------------------------------
Ran 15 tests in 0.003s

FAILED (failures=1)
```

We can see that the test has failed, even with 100% of coverage and mutants killed.