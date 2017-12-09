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

## Test

```bash
./demo.sh
```

## 错误提示

```
(C) 惯例。违反了编码风格标准

(R) 重构。写得非常糟糕的代码。

(W) 警告。某些 Python 特定的问题。

(E) 错误。很可能是代码中的错误。

(F) 致命错误。阻止 Pylint 进一步运行的错误。
```
