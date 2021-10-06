


def printter(**kwargs):
    for x,y in kwargs.items():
        print(f'{x} - {y}')

printter(language='Python')

printter(name='Bill Gates',company='Microsoft')
