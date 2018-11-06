# Create your tasks here
from __future__ import absolute_import, unicode_literals

import os
import shutil

from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist

from ApiManager.models import ProjectInfo
from ApiManager.utils.common import timestamp_to_datetime
from ApiManager.utils.emails import send_email_reports
from ApiManager.utils.operation import add_test_reports
from ApiManager.utils.runner import run_by_project, run_by_module, run_by_suite
from ApiManager.utils.testcase import get_time_stamp
from httprunner import HttpRunner, logger


@shared_task
def main_hrun(test_set_path, report_name):
    """
    用例运行
    :param test_set_path: dict or list
    :param report_name: str
    :return:
    """
    logger.setup_logger('INFO')
    kwargs = {
        "failfast": False,
    }
    runner = HttpRunner(**kwargs)
    runner.run(test_set_path)
    shutil.rmtree(test_set_path)

    runner.summary = timestamp_to_datetime(runner.summary)
    report_path = add_test_reports(runner, report_name=report_name)
    os.remove(report_path)


@shared_task
def project_hrun(env_name, base_url, project, receiver):
    """
    异步运行整个项目
    :param env_name: str: 环境地址
    :param project: str
    :return:
    """
    logger.setup_logger('INFO')
    kwargs = {
        "failfast": False,
    }
    runner = HttpRunner(**kwargs)
    pk = ProjectInfo.objects.get(project_name=project).id

    test_case_dir_path = os.path.join(os.getcwd(), "suite")
    test_case_dir_path = os.path.join(test_case_dir_path, get_time_stamp())

    run_by_project(pk, base_url, test_case_dir_path)

    runner.run(test_case_dir_path)
    shutil.rmtree(test_case_dir_path)

    runner.summary = timestamp_to_datetime(runner.summary)
    report_path = add_test_reports(runner, report_name=env_name)

    if receiver != '':
        send_email_reports(receiver, report_path)
    os.remove(report_path)


@shared_task
def module_hrun(env_name, base_url, module, receiver):
    """
    异步运行模块
    :param env_name: str: 环境地址
    :param project: str：项目所属模块
    :param module: str：模块名称
    :return:
    """
    logger.setup_logger('INFO')
    kwargs = {
        "failfast": False,
    }
    runner = HttpRunner(**kwargs)
    module = list(module)

    test_case_dir_path = os.path.join(os.getcwd(), "suite")
    test_case_dir_path = os.path.join(test_case_dir_path, get_time_stamp())

    try:
        for value in module:
            run_by_module(value[0], base_url, test_case_dir_path)
    except ObjectDoesNotExist:
        return '找不到模块信息'

    runner.run(test_case_dir_path)

    shutil.rmtree(test_case_dir_path)
    runner.summary = timestamp_to_datetime(runner.summary)
    report_path = add_test_reports(runner, report_name=env_name)

    if receiver != '':
        send_email_reports(receiver, report_path)
    os.remove(report_path)


@shared_task
def suite_hrun(env_name, base_url, suite, receiver):
    """
    异步运行模块
    :param env_name: str: 环境地址
    :param project: str：项目所属模块
    :param module: str：模块名称
    :return:
    """
    logger.setup_logger('INFO')
    kwargs = {
        "failfast": False,
    }
    runner = HttpRunner(**kwargs)
    suite = list(suite)

    test_case_dir_path = os.path.join(os.getcwd(), "suite")
    test_case_dir_path = os.path.join(test_case_dir_path, get_time_stamp())

    try:
        for value in suite:
            run_by_suite(value[0], base_url, test_case_dir_path)
    except ObjectDoesNotExist:
        return '找不到Suite信息'

    runner.run(test_case_dir_path)

    shutil.rmtree(test_case_dir_path)

    runner.summary = timestamp_to_datetime(runner.summary)
    report_path = add_test_reports(runner, report_name=env_name)

    if receiver != '':
        send_email_reports(receiver, report_path)
    os.remove(report_path)
