# bash

[TOC]

## 命令行快捷键


```bash
# 查看所有键盘绑定
bind -p
```

### 编辑
* 移动光标
    * 按行
        * `Ctrl + a`: 移动 到行首
        * `Ctrl + e`: 移动 到行尾
        * `Ctrl + x`: 行首及光标处移动
    * 按字符
        * `Ctrl + f`: 前移/右移 一个字符
        * `Ctrl + b`: 后移/左移 一个字符
* 删除
    * 按行
        * `Ctrl + u`: 删除 光标至行首
        * `Ctrl + k`: 删除 光标至行尾
    * 按单词
        * `Ctrl + w`: 删除 光标至词首
    * 按字符
        * `Ctrl + d`: 删除 光标处字符
        * `Ctrl + h`: 删除 光标前字符
* 编辑
    * `Tab`: 自动补全命令或文件名
    * `Ctrl + t`: 交换光标处与前一字符
    * `Ctrl + y`: 粘贴 `Ctrl + w` 或 `Ctrl + k`删除内容

### 执行命令

* `Ctrl + r`: 反向搜索命令历史
* `Ctrl + g`: 从历史搜索模式推出
* `Ctrl + p`: 上一条命令

### 控制命令

* `Ctrl + l`: 清屏
* `Ctrl + c`: 终止命令
* `Ctrl + z`: 挂起命令

### Bang(!)命令

* 命令
    * `!!`: 执行上一条命令
    * `!num`: 执行命令历史中第num条命令
    * `!-n`: 倒数第N条历史命令
    * `!!:p`: **打印**上一条命令
    * `!his`: 执行最近以`his`开头的命令，如：history
    * `!his:p`: **打印**最近以`his`开头的命令，不执行
    * `!?string?`: 执行包含`string`字符串的最近命令
* 参数
    * `!$`: 上一条命令最后一个参数
    * `!$:p`: **打印**上一条命令最后一个参数
    * `!*`: 上一条命令所有参数
    * `!*`: **打印**上一条命令所有参数
* 字符操作
    * `^string`: 删除上条命令中的string
    * `^find^replace`: 将上条命令中的find替换为replace
    * `^find^replace^`: 将上条命令中所有的find替换为replace 
    * `!-n:gs/str1/str2/`: 将倒数第N条命令的str1替换为str2，并执行（若不加g,则仅替换第一个）

## 环境变量

```bash
export 
env
source 
```


