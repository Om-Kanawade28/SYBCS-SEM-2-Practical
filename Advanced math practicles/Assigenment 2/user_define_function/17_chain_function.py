# Write a Python program to create a chain of function decorators (bold, italic, underline etc.).
def make_bold(fn):
    def wrapped(*args, **kwargs):
        return "<b>" + fn(*args, **kwargs) + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped(*args, **kwargs):
        return "<i>" + fn(*args, **kwargs) + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped(*args, **kwargs):
        return "<u>" + fn(*args, **kwargs) + "</u>"
    return wrapped

@make_bold
@make_italic
@make_underline
def get_message():
    return "Hello World"

print(get_message())

#output:-
# <b><i><u>Hello World</u></i></b>
