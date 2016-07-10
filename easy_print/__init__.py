# -*- coding: utf-8 -*-

from sys import stdout

# http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
colors = {
    'header': '\033[95m',
    'okblue': '\033[94m',
    'okgreen': '\033[92m',
    'warning': '\033[93m',
    'fail': '\033[91m',
    'endc': '\033[0m',
    'bold': '\033[1m',
    'underline': '\033[4m'
}
colors['red'] = colors['fail']
colors['green'] = colors['okgreen']
colors['blue'] = colors['okblue']
colors['purple'] = colors['header']
colors['yellow'] = colors['warning']

def eprint(text, stay=False, color=None):
    stdout.write('\r' + ' ' * 64)
    stdout.write('\r{text}\r'.format(
        text=colors[color] + str(text) + colors['endc'] if color else str(text)
    ))
    stdout.flush()
    if stay:
        stdout.write('\n')
        stdout.flush()

def eprogress(progress=0, total=100, width=64, color=None):
    n_completed = int(progress * width / float(total))
    completed = '█' * n_completed
    to_complete = '-' * (width - n_completed)
    text = '{completed}{to_complete} {percentage}'.format(
        completed=completed,
        to_complete=to_complete,
        percentage='{num} %'.format(num=round(progress * 100 / float(total), 2))
    )
    eprint(text=text, color=color)
