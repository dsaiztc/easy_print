# easy_print
Easy print progress or messages on console while executing your python scripts. Different colors, progress bar, etc.

- Inserting a bare `print` statement in your **python** script it's not enough for you?
- Need to see the progress withoug filling your terminal with endless print statements?
- Also... wouldn't you fancy some colouring?
- And how about a progress bar?

## Motivation
I write a number of **python** scripts and adding a `print` statement here and there... it's usually enough.

But for those moments I need a bit *more*, I figured out a *very simple* way of inserting print statements on the same line, adding some colours and maybe a progress bar.

## Install
```
$ python setup.py install
```

## Use
![easy_print](http://g.recordit.co/OouKKeRnwn.gif)

```python
from easy_print import eprint, eprogress

eprint('--- Process started ---', stay=True, color='blue')
eprint('Generating random IDs...', stay=True, color='purple')
import uuid
for i in range(10):
    eprint('New asignated UUID: {}'.format(uuid.uuid4()))
eprint('All IDs correctly assigned!', stay=True, color='green')
for i in range(1000):
    eprogress(i + 1, total=1000, text='Downloading...', color='yellow')
eprint('All tasks done!', stay=True, color='red')
```
