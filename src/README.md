# Source code section

This area will be used to store all the source code for our Python bootcamp.

## How to read code here?

Please open source code files and read through them. Source code is added, and sufficiently annotated with comments. All files are runnable out of the box.

## Day 1

Please look at some source code checked in for Day 1 related items

- [Basics](./python-sample-0.py)
- [Input and output](./python-sample-1-1.py)
- [Conditions, loops and functions](./python-sample-1-2.py)
- [Sample programs - physics and math quantities](./python-sample-1-3.py)

One you are done with this, please take a look at the [practice sheet](python-practice-1-1.py).

## Day 2

Please find the day 2 source code illustrating how a dodging game could look in python using pygame, [here](python-sample-2-1.py).
I would strongly suggest reading up content on Day 1 and practicing some code. Otherwise a lot of syntax will feel very strange and alien to you.
Please follow the instructions in the code file. After you have installed `pygame`, you can then run the module as

`python3 python-sample-2-1.py`. If this fails, run `python python-sample-2-1.py`

## Day 3

Day 3 deals with another real life use of Python, and currently an extremely popular one - data analysis and visualization.
We have tried to present an example, where we connect to a public remote server, fetch covid data for a month for cities across the globe.
After this, we explore multiple things - writing this data in a table like format to excel, or manipulating this data in python itself by filtering based on certain values. We then present an example to generate some graphs to show how you could do some form of analysis using python
as a tool.

You can find all of the code and some data files [here](./data-analysis/).
You need to install some packages for it to work. Namely
1. `matplotlib`
2. `xlsxwriter`
3. `requests`
4. `xlrd`
5. `pandas`
6. `numpy`

To quickly install all of these in one go, please run this command.

```bash
python3 -m pip install pandas matplotlib numpy requests xlsxwriter xlrd
```

or the following if the above one fails.

```bash
python -m pip install pandas matplotlib numpy requests xlsxwriter xlrd
```

To run this, please run the [main.py](./data-anaysis/main.py) in Python as `python3 main.py`. If this fails, try `python main.py`.
