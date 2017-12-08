# pylint

[TOC]

## Installation

```bash
pip install virtualenv virtualenvwrapper

mkvirtualenv demo

pip install pylint
```

## Create Python

```bash
# goes python code
```

## Try pylint

```bash
# Generate pylint config file
pylint --generate-rcfile > pylint.conf

# Enable colorized
sed -i 's#^output-format=.*#output-format=colorized#g' pylint.conf

# Check python by pylint
pylint --rcfile pylint.conf demo.py
```

