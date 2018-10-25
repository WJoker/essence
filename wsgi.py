#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname
import app


sys.path.insert(0, abspath(dirname(__file__)))
application = app.app


"""
配置 supervisor
ln -s /var/www/essence/configs/essence.conf /etc/supervisor/conf.d/bbs.conf

配置 Nginx 服务器
ln -s /var/www/essence/configs/essence.nginx /etc/nginx/sites-enabled/essence
配置重启 Nginx 之后，更新代码只需要重启 gunicorn
"""