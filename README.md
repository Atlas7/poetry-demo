Just my own sandpit to play with building Python package with Poetry. Build with Python 3.7.

Installation:

```
pip install git+https://github.com/Atlas7/poetry-demo.git
```

Usage:

```
>>> import poetry_demo
>>> x = poetry_demo.my_version()
>>> print(x)
0.1.0
```

Dev Instruction:

```
git clone https://github.com/Atlas7/poetry-demo.git
```

Then navigate to the root of the repository:

```
cd poetry-demo
```

Dev - Run test:

```
poetry run pytest tests
```