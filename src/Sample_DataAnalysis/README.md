# Python application - Data analysis and visualization

We have tried to present an example, where we connect to a public remote server, fetch Covid-19 data for a month for cities across the globe.
After this, we explore multiple things - writing this data in a table like format to excel, or manipulating this data in python itself by filtering based on certain values. We then present an example to generate some graphs to show how you could do some form of analysis using python
as a tool.

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

To run this, please run the [main.py](./Day%203/data-analysis/main.py) in Python as `python3 main.py`. If this fails, try `python main.py`.
