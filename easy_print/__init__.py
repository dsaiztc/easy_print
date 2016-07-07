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

def eprint(text, newline=False, color=None):
    stdout.write(''.join(['\r', ' ' * 100])
    if color is not None:
        stdout.write('\r' + colors[color] + text + colors['endc'])
    else:
        stdout.write('\r' + text)
    stdout.flush()
    if newline:
        stdout.write('\n')
