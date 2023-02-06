def hello(name = ''):
    if len(name) > 0:
        return 'Hello, ' + name + '!'
    else:
        return 'Hello, World!'