__author__ = 'mucang'

#-*- coding:utf-8 -*-
from common import logging_config
import pytest
from common import file_path

pytest.main([
             "-m login",
             "--html={0}/report.html".format(file_path.test_report_path),
             "--junitxml={0}/report.xml".format(file_path.test_report_path),
             "--alluredir={0}".format(file_path.test_allureReport_path),
             "--reruns","2","--reruns-delay","5"
])

