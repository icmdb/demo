#!/bin/bash
#
export PATH=.:$PATH

export ANSIBLE_HOSTS=/etc/ansible/hosts
export ANSIBLE_HOST_KEY_CHECKING=False

echo "ln -s $(pwd)/etc /etc/ansible"

