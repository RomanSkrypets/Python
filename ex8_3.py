from cgi import test


def make_shirt(size,text):
    print(f'Your t-shirt size is: {size.upper()}')
    print(f'Your text in t-shirt is: {text}')

# make_shirt("m",'World is yours!')
make_shirt(text="World is yours!", size="xl")