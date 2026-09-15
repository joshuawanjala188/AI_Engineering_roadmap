#it manages resources automatically
#creating a context manager
#python uses _enter_() _exit_() example

"""class Resource:


    def _enter_(self):

        print("Opening resource")

        return self

    def _exit_(self, exec_type, exec_value, traceback):
        print("Closing resource")


with Resource():
    print("Using resource")"""


#contextlib- python also provides an easier way to create context managers

from contextlib import contextmanager

@contextmanager

def resource():

    print("Opening")

    try:
        yield

    finally:
        print("Closing") 


with resource():
    print("Working")
