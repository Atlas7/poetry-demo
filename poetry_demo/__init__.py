__version__ = '0.1.0'


def my_version():
    return __version__


if __name__ == "__main__":
    x = my_version()
    print("You are running poetry-demo version: {}".format(x))
