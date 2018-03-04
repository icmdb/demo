# Compose file v2 参考

[TOC]

> 原文地址：[https://docs.docker.com/compose/compose-file/compose-file-v2/](https://docs.docker.com/compose/compose-file/compose-file-v2/)

## [参考指南](https://docs.docker.com/compose/compose-file/compose-file-v2/#reference-and-guidelines)

这些主题描述了Compose文件格式的第2版。

## [Compose 和 Docker兼容性清单](https://docs.docker.com/compose/compose-file/compose-file-v2/#compose-and-docker-compatibility-matrix)

有几种版本的编排文件格式：1, 2, 2.x, 和 3.x。下表可快速查看。每个版本包含的所有细节以及如何升级，查看[关于版本和升级](https://docs.docker.com/compose/compose-file/compose-versioning/)。

此表显示哪些编排文件版本支持特定的Docker版本。

```
Compose file format	    Docker Engine release
3.3	17.06.0+
3.2	17.04.0+
3.1	1.13.1+
3.0	1.13.0+
2.3	17.06.0+
2.2	1.13.0+
2.1	1.12.0+
2.0	1.10.0+
1.0	1.9.1.+
```

除了表中展示的编排文件格式版本以外，编排文件本身也有发布时间表，如`Compose`发布日志所示，但是文件格式版本不一定随每个发布增加。例如：`Compose`文件版本格式`3.0`在`Compose`  发布`1.10.0`时被首次介绍，但是在随后的发布中逐渐版本化。

## [Service 配置参考](https://docs.docker.com/compose/compose-file/compose-file-v2/#service-configuration-reference)

编排文件是一个定义[服务](https://docs.docker.com/compose/compose-file/compose-file-v2/#service-configuration-reference)，[网络](https://docs.docker.com/compose/compose-file/compose-file-v2/#network-configuration-reference)，[卷](https://docs.docker.com/compose/compose-file/compose-file-v2/#volume-configuration-reference)的[YAML](http://yaml.org/)文件。编排文件的默认路径是`./docker-compose.yml`。

> 注：你可以使用`.yml`或`.yaml`作为文件扩展名。两种格式都生效。

### [blkio_config](https://docs.docker.com/compose/compose-file/compose-file-v2/#blkio_config)

一组为该服务限制IO块的配置集。

```yaml
version: '2.2'
services:
  foo:
    image: busybox
    blkio_config:
      weight: 300
      weight_device:
        - path: /dev/sda
          weight: 400
      device_read_bps:
        - path: /dev/sdb
          rate: '12mb'
      device_read_iops:
        - path: /dev/sdb
          rate: 120
      device_write_bps:
        - path: /dev/sdb
          rate: '1024k'
      device_write_iops:
        - path: /dev/sdb
          rate: 30
```

#### DEVICE_READ_BPS, DEVICE_WRITE_BPS

为给定设备上的读/写操作设置每秒字节数限制。列表中每项必须包含两个键：

* `path`，定义受影响设备的符号路径
* `rate`，作为表示字节数的整数值，或作为表示字节值的字符串

#### DEVICE_READ_IOPS, DEVICE_WRITE_IOPS

为给定的设备设置每秒操作数限制。列表中每项必须包含两个键：

* `path`，定义受影响设备的符号路径
* `rate`，作为表示每秒操作数限制的整数值

#### WEIGHT

修改分配给该服务的带宽相对于其他服务比例。使用10到1000的整数值，默认值为500.

#### WEIGHT_DEVICE

通过设备微调分配带宽。列表中的每项必须有两个键：

* `path`，定义受影响设备的符号路径
* `weight`，10到1000之间的一个整数值

### [build](https://docs.docker.com/compose/compose-file/compose-file-v2/#build)

构建时应用的配置选项。

`build`可以作为被指定 作为包含构建上下文路径的字符串，或一个在上下文中指定路径对象，或可选的`dockerfile`和`args`。

```yaml
build: ./dir

build:
  context: ./dir
  dockerfile: Dockerfile-alternate
  args:
    buildno: 1
```

如果你同时指定了`image`和`build`，compose给构建的镜像命名为`webapp`和`image`中指定的任意`tag`:

```yaml
build: ./dir
image: webapp:tag
```

这将导致从`./dir`构建出一个以`tag`为tag的`webapp`镜像。

#### [CONTEXT](https://docs.docker.com/compose/compose-file/compose-file-v2/#context)

> [V2版本的文件格式](https://docs.docker.com/compose/compose-file/compose-versioning/#version-2)有效。在V1中，只用`build`。

包含Dockerfile的一个目录路径，或者一个git仓库url。

当给出的路径是一个相对路径，它相对Compose file被解释。该目录也是发送给Docker Daemon的构建上下文。


```yaml
build:
  context: ./dir
```

#### [DOCKERFILE](https://docs.docker.com/compose/compose-file/compose-file-v2/#dockerfile)

替换 Dockerfile。

编排文件将使用替换文件构建。构建路径也必须指定。

```yaml
build:
  context: .
  dockerfile: Dockerfile-alternate
```


#### [ARGS](https://docs.docker.com/compose/compose-file/compose-file-v2/#args)

> [V2版本文件格式](https://docs.docker.com/compose/compose-file/compose-versioning/#version-2)有效。

增加构建参数，这些参数作为环境变量只能在构建过程中访问。
首先，在你的Dockerfile中指定参数：

```yaml
ARG buildno
ARG password

RUN echo "Build number: $buildno"
RUN script-requireing-password.sh "$password"
```

然后在`build`下指定参数。你可以通过一个列表或映射：

```yaml
build:
  context:
  args:
    buildno: 1
    password: secret
    
build:
  context: .
  args:
    - buildno=1
    - password=secret
```

> 注：YAML布尔值（true, false, yes, no, on, off）必须用引号引起来，以使解析器会把他们作为字符串解析。

#### [EXTRA_HOSTS](https://docs.docker.com/compose/compose-file/compose-file-v2/#extra_hosts)

构建时添加主机名映射。与docker客户端`--add-host`参数使用相同的值。


```yaml
extra_hosts:
  - "somehost:162.242.195.82"
  - "otherhost:50.31.209.229"
```

#### [LABELS](https://docs.docker.com/compose/compose-file/compose-file-v2/#labels)

> 增加于[2.1版本文件格式](https://docs.docker.com/compose/compose-file/compose-versioning/#version-21)

使用`Docker labels`增加元数据到最终镜像。你可以使用一个数组或字典。

建议你使用反向DNS标记防止你的标签与其他软件使用的标签冲突。

```yaml
build:
  context: .
  labels:
    com.example.description: "Accounting webapp"
    com.example.department: "Finace"
    com.example.label-with-empty-value: ""
  
build:
  context: .
  labels:
    - "com.example.description=Accounting webapp"
    - "com.example.department=Finace"
    - "com.example.label-with-empty-value"
```

#### [NETWORK](https://docs.docker.com/compose/compose-file/compose-file-v2/#networks)

> 增加于2.2版本文件格式

设置在构建过程中`RUN`指令将会链接的网络容器。

```yaml
build:
  context: .
  network: host

build:
  context: .
  network: custom_network_1
```

### [SHM_SIZE](https://docs.docker.com/compose/compose-file/compose-file-v2/#shm_size)

> 增加于2.3文件格式

为构建容器设置`/dev/shm`分区大小。指定一个整数值表示字节数据或一个字符串表示字节值。

```yaml
build:
  context: .
  shm_size: '2gb'
  
build:
  context: .
  shm_size: 10000000
```

#### [ALIASES](https://docs.docker.com/compose/compose-file/compose-file-v2/#aliases)

#### [IPV4_ADDRESS, IPV6_ADDRESS](https://docs.docker.com/compose/compose-file/compose-file-v2/#ipv4_address-ipv6_address)

#### [LINK_LOCAL_IPS](https://docs.docker.com/compose/compose-file/compose-file-v2/#link_local_ips)

### [ulimits](https://docs.docker.com/compose/compose-file/compose-file-v2/#ulimits)

覆盖容器默认`ulimits`。您可以将单个`limit`指定为整数或为`soft/hard`指定`limits`映射。

```bash
ulimits:
  nproc: 65535
  nofile:
    soft: 20000
    hard: 40000
```

### [command](https://docs.docker.com/compose/compose-file/compose-file-v2/#command)

覆盖默认命令。

```bash
command: bundle exec thin -p 3000
```

命令也可以是一个列表，跟`dockerfile`里的形式类似：

```bash
command: ["bundle", "exec", "thin", "-p", "3000"]
```

### [environment](https://docs.docker.com/compose/compose-file/compose-file-v2/#environment)

增加环境变量。你可以使用一个数组或者一个字典。任意布尔值；true, false, yes no, 需要用括号括起来确保他们不会呗`YML`解析器解析为`True`或者`False`。

一个只有`key`的环境变量会被解析为正在运行主机上的值，这对于密钥或者主机专用值（的场景）非常有帮助。

```yml
environment:
  RACK_ENV: development
  SHOW: 'true'
  SESSION_SECRET:

environment:
  - RACK_ENV=development
  - SHOW=true
  - SESSION_SECRET
```

> **注意：** 如果你的服务指定了`build`选项，在`environment`中定义的变量不会在`build`期间自动可见。使用构建子选项`args`定义构建时环境变量。

### [healthcheck](https://docs.docker.com/compose/compose-file/compose-file-v2/#healthcheck)

> [2.1版文件格式](https://docs.docker.com/compose/compose-file/compose-versioning/#version-21) 和启动。

配置检测确定该服务的容器是否"健康"。

监控检查工作细节查看文档[Dockerfile HEALTHCHECK 指令](https://docs.docker.com/engine/reference/builder/#healthcheck)

```bash
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost"]
  interval: 1m30s
  timeout: 10s
  retries: 3
  start_period: 40s
```

`interval`, `timeout`和`start_period`被指定为时间间隔。

`test`必须是一个字符串或者是一个列表。如果是一个列表，第一个元素必须是`NONE`, `CMD` 或 `CMD-SHELL`之一。如果是一个字符串，它等价于指定`CMD-SHELL`，字符串跟随之后。

```bash
# Hit the local web app
test: ["CMD", "curl", "-f", "http://localhost"]

# As above, but wrapped in /bin/sh. Both forms below are equivalent.
test: ["CMD-SHELL", "curl -f http://localhost && echo 'cool, it works'"]
test: curl -f https://localhost && echo 'cool, it works'
```

禁用镜像指定的默认健康检查，可以使用`disable: true`。这等价于指定一个`test: ["NONE"]`。

```bash
healthcheck:
  disable: true
```

> 注：`start_period`选项是最近更新的功能，且只有2.3版本的文件格式可用。


### [logging](https://docs.docker.com/compose/compose-file/compose-file-v2/#logging)

服务日志配置。

```bash
logging:
  driver: syslog
  options:
    syslog-address: "tcp://192.168.0.42:123"
```

`driver`为容器指定一个日志驱动，正如`docker run`命令的`--log-file`选项一样[文档](https://docs.docker.com/engine/admin/logging/overview/)。

默认值为`json-file`。

```bash
driver: "json-file"
driver: "syslog"
driver: "none"
```

> 注：只有`json-file`和`journald`驱动可直接用于`docker-compose up`和`docker-compose logs`。使用其他驱动将不会打印任何日志。

使用选项值为日志驱动指定日志选项，如：`docker run`命令的`--log-opt`。

日志选项是一个键值对。一个`syslog`选项如下：

```bash
driver: "syslog"
options:
  syslog-address: "tcp://192.168.0.42:123"
```

### [volumes, volume_driver](https://docs.docker.com/compose/compose-file/compose-file-v2/#volumes-volume_driver)



### [volumes_from](https://docs.docker.com/compose/compose-file/compose-file-v2/#volumes_from)



## [Volume 配置参考](https://docs.docker.com/compose/compose-file/compose-file-v2/#volume-configuration-reference)

