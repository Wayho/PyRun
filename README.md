# PyRun

一个运行在 LeanEngine 的 Python 应用。
可以在线运行 Python 程序，且已安装了常见的依赖。

## 部署

可以通过 Lean 命令行方式部署，也可以在 LeanCloud 直接通过源码部署方式部署。

#### 源码部署：

在 LeanCloud 后台，云引擎处，选设置，把 git@github.com:Wayho/PyRun.git 填入代码库;

把 Delopy Key 复制后在 https://github.com/Wayho/PyRun/settings/keys 处 Add deploy key;

最后在在 LeanCloud 后台，云引擎处，选部署即可开始部署


## 已安装的依赖

gevent>=1.0.2,<2.0.0

gevent-websocket>=0.9.5,<1.0.0

leancloud>=2.0.0,<3.0.0

Werkzeug>=0.11.11,<1.0.0

Flask>=0.10.1,<1.0.0

Flask-Sockets>=0.1,<1.0


requests>=2.13.0,<=2.18.4

flask-wtf>=0.14.2

lxml>=3.0.0, <=4.0.0

numpy>=1.13.0

pandas>=0.21.0

BeautifulSoup==3.2.1

BeautifulSoup4>=4.6.0

python-dateutil>=2.6.1


## DEMO
http://pyrun.leanapp.cn

## 相关文档

* [LeanEngine 指南](https://leancloud.cn/docs/leanengine_guide.html)
* [Python SDK 指南](https://leancloud.cn/docs/python_guide.html)
* [Python SDK API](https://leancloud.cn/docs/api/python/index.html)
* [命令行工具详解](https://leancloud.cn/docs/cloud_code_commandline.html)
* [LeanEngine FAQ](https://leancloud.cn/docs/cloud_code_faq.html)
* [ACE Editor](https://github.com/ajaxorg/ace-builds)
* [Flask 如何响应 JSON 数据](https://www.tuicool.com/articles/6vYbU3)
* [JQuery Dialog](http://jqueryui.com/dialog/#modal-form)
* [Font Awesome 图标字体库和CSS框架](http://fontawesome.dashgame.com/)
