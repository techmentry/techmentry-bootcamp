# Development environment setup for Python based modules

## Overview

This document will highlight how to setup your local computer and get started with python based development. This setup will invite you to follow a few steps, and it is recommended that you follow them exactly. However, it is not mandated that you use the same set of tools as this document describes. This document is geared towards people starting out with Python programming or python sub-modules in general. If you already are fluent with your own setup, please continue using that and adjust parameters and settings based on your development tools.

## Setting up python

Setting up python can be different based on the operating system that you use. Please scroll down and find out the operating system you use, and the recommended installation procedure

### Windows and OSX (macOS)

Please visit [the official python website](https://www.python.org/downloads/) to get the latest version of Python. If you face any issues, please contact your instructor for help. For the most part, you should be able to click and download the installer for your OS directly from the above page.

Please run the installer and follow the instructions to install Python on your system.

### Linux/ Unix derivative

Chances are you already have Python 3 on your system. You can quickly check this by opening terminal > type `python3 --version` > check output. If running this command results in an error, it is likely you have an older version of python. In this case, please read [this guide](https://docs.python-guide.org/starting/install3/linux/), and install python on your Linux machine. __Try and install the latest version__. If you want to get more in to details of your system i.e. if you don't use Ubuntu Linux, please follow the instructions to build and install python from source. Please read and follow [these instructions](https://realpython.com/installing-python/#how-to-install-python-on-linux) carefully to do so.

## Post installation

Once that is done, _please reboot your machine_.
>Although it is not required, it sometimes allows the installer to setup environment variables and other parameters correctly. This is especially true on Windows.

Once you have rebooted your computer, please open a command prompt/ Powershell window on your Windows computer, or open terminal on your Mac/ Linux/ Nix system, and type the following command.

```bash
python3 --version
```

If this does not work, please remove the 3 suffix and just run

```bash
python --version
```

This should print something like the following on the next line. Please note at the time of writing this, I am on version 3.9.5. Your minor version (3.minor.feature) might vary (it may be higher or lower, but that is fine.)

```bash
(base) sarthaktickoo@Sarthaks-MBP general % python3 --version
Python 3.9.5
```

>Please note that the bash/ profile will be different in your case. In simpler terms, the text, `(base) sarthaktickoo@Sarthaks-MBP general %` will vary machine to machine, and user to user.

## Updating `pip`

Python has a package manager called **pip** which allows you to install some cool modules and packages, like pygame. Keeping pip up to date is recommended, unless there is a good reason to not update it (there are some cases where certain packages won't fetch if pip is latest. So don't do this unless your instructor has asked you to do so.)

To upgrade pip, please run the following command on your machine

```bash
python3 -m pip install --upgrade pip
```

If `python3` does not work on your machine, please remove the leading 3 from python and just type

```bash
python -m pip install --upgrade pip
```

You can then go ahead and install some packages to test things. E.g. try and install the `uuid` package, which allows you to generate some cool UUIDs. To do so, please use one the following commands

```bash
python3 -m pip install uuid
```

OR

```bash
python -m pip install uuid
```

While it installs, you may see something like this -

```bash
(base) sarthaktickoo@Sarthaks-MBP general % python3 -m pip install uuid
Collecting uuid
  Downloading uuid-1.30.tar.gz (5.8 kB)
Building wheels for collected packages: uuid
  Building wheel for uuid (setup.py) ... done
  Created wheel for uuid: filename=uuid-1.30-py3-none-any.whl size=6501 sha256=f8c25b5a80285f3bc5ff57995430b7fa8cc9bf31b8fa3c0762b5b0ca24667c40
  Stored in directory: /Users/sarthaktickoo/Library/Caches/pip/wheels/05/d7/b4/4795d29c6decfffbf64c63e58b6c8b8bbfd4751488617dcd7a
Successfully built uuid
Installing collected packages: uuid
Successfully installed uuid-1.30
(base) sarthaktickoo@Sarthaks-MBP general %
```

## Notes

* This is a one time setup. Do not repeat this every time, or else you will end up with multiple and conflicting versions of python.
* Please make sure you are using Python 3. If the above commands give you an output like `2.ab.cd`, please upgrade to Python 3 by following the instructions above. **Python 2 support has ended and will be removed in the future.**
* Please get used to running python code from the command line. To do so, please read our command line usage guide. It will be extremely useful and will help you to run your programs better.
* Please check your course details for more information on any specific set of modules/ setup that you might have to do. Please write to dev.techmentry@gmail.com for reporting any issues.
* We recommend using VS Code to program in python. You are however, free to use any other form of IDE, source code editor or live code editors. If you are interested in using VS code, please follow our VS code setup guide to obtain it for your system.
