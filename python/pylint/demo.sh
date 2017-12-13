#!/usr/bin/env bash
#

#set -xue

msg() {
    echo "[$(date '+%F %T%z')] ${@}"
}

_red() {
    echo -e "\033[0;31m${@}\033[0m"
}

_green() {
    echo "\033[0;32m${@}\033[0m"
}


is_installed() {
    which "$1" > /dev/null 2>&1
    return $?
}


if is_installed pylint; then 
    pylint --rcfile pylint.conf demo.py
else
    is_installed pylint || \
        msg $(_red "pylint is not installed, installing...") && \
        pip install pylint 

    [[ -f pylint.conf ]] || \
        pylint --generate-rcfile > pylint.conf 

    [[ "$(uname -s)" == "Darwin" ]] && \
        sed -i '' 's#^output-format=.*#output-format=colorized#g' pylint.conf
    [[ "$(uname -s)" == "Linux" ]] && \
        sed -i 's#^output-format=.*#output-format=colorized#g' pylint.conf
fi

