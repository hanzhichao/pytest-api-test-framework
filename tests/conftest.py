import os
from datetime import datetime
from pprint import pprint

import pytest

from utils.mysql_client import MySQLClient
from utils.http_client import HttpClient


def pytest_configure(config):
    """将日志配置的生成绝对路径输出到reports目录"""
    rootdir = config.rootdir  # 项目根目录
    now = datetime.now()

    htmlpath = config.getoption('--html')
    log_file = config.getoption('--log-file') or config.getini('log_file')

    if log_file:
        if not os.path.isabs(log_file):
            log_file = os.path.join(rootdir, log_file)
        config.option.log_file = now.strftime(log_file)

    if htmlpath:
        if not os.path.isabs(htmlpath):
            htmlpath = os.path.join(rootdir, htmlpath)
        config.option.htmlpath = now.strftime(htmlpath)


@pytest.fixture
def base_url(env_vars) -> str:
    return env_vars.get('base_url')


@pytest.fixture
def db(env_vars) -> str:
    return env_vars.get('db')


@pytest.fixture
def mysql_client(db_config) -> MySQLClient:
    return MySQLClient(db_config)
