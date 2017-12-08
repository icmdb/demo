# demo

A demo project.

## Clone

```bash
git clone git@github.com:icmdb/demo.git

cd demo

git config user.name teachmyself
git config user.email teachmyself@126.com

cat ~/.gitconfig <<GIT
[push]
    default = matching
[filter "lfs"]
    clean = git-lfs clean %f
    smudge = git-lfs smudge %f
    required = true
[user]
    name = teachmyself
    email = teachmyself@126.com
GIT
```

## Set PS1

```bash
# Add to ~/.bash_profile
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ \(\1\)/'
}

cmd_prompt='$'
[[ $(id -u) -eq 0 ]] && cmd_prompt='#'

PS1='\[\033[0;32m\][\u@\h \[\033[01;31m\]\w\[\033[00;35m\]$(parse_git_branch)\[\033[00m\]\[\033[0;32m\]]'${cmd_prompt}'\[\033[00m\] '
```
