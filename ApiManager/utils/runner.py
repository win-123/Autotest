import os

from django.core.exceptions import ObjectDoesNotExist
from ApiManager.utils.testcase import dump_python_file, dump_yaml_file
from ApiManager.models import (
    TestCaseInfo,
    ModuleInfo,
    ProjectInfo,
    DebugTalk,
    TestSuite
)


def run_by_single(index, base_url, path):
    """
    对于当个测试用例的运行
    :param index: int or str：用例索引
    :param base_url: str：环境地址 ： http://47.94.172.250:33334
    :param path: api接口名字   /api/v1/account/login
    :return:
    """

    test_case_list = []
    config = {
        'config': {
            'name': '',
            'request': {
                'base_url': base_url
            }
        }
    }
    test_case_list.append(config)

    try:
        obj = TestCaseInfo.objects.get(id=index)
    except ObjectDoesNotExist:
        return test_case_list

    include = eval(obj.include)
    request = eval(obj.request)
    name = obj.name
    project = obj.belong_project
    module = obj.belong_module.module_name

    config['config']['name'] = name

    test_case_dir_path = os.path.join(path, project)

    if not os.path.exists(test_case_dir_path):
        os.makedirs(test_case_dir_path)

        try:
            debugtalk = DebugTalk.objects.get(belong_project__project_name=project).debugtalk
        except ObjectDoesNotExist:
            debugtalk = ''
        # 添加dubugtalk.py文件的路径
        dump_python_file(os.path.join(test_case_dir_path, 'debugtalk.py'), debugtalk)
    # 单个测试用例的运行路径
    test_case_dir_path = os.path.join(test_case_dir_path, module)

    if not os.path.exists(test_case_dir_path):
        os.mkdir(test_case_dir_path)

    for test_info in include:
        try:
            if isinstance(test_info, dict):
                config_id = test_info.pop('config')[0]
                config_request = eval(TestCaseInfo.objects.get(id=config_id).request)
                config_request.get('config').get('request').setdefault('base_url', base_url)
                config_request['config']['name'] = name
                test_case_list[0] = config_request
            else:
                pk = test_info[0]
                pre_request = eval(TestCaseInfo.objects.get(id=pk).request)
                test_case_list.append(pre_request)

        except ObjectDoesNotExist:
            return test_case_list

    if request['test']['request']['url'] != '':
        test_case_list.append(request)

    dump_yaml_file(os.path.join(test_case_dir_path, name + '.yml'), test_case_list)


def run_by_suite(index, base_url, path):
    """
    组件的运行
    :param index: 索引
    :param base_url: 网址
    :param path: 路径
    :return:
    """
    obj = TestSuite.objects.get(id=index)

    include = eval(obj.include)

    for val in include:
        run_by_single(val[0], base_url, path)


def run_by_batch(test_list, base_url, path, model=None, mode=False):
    """
    批量的运行
    :param test_list: 测试列表
    :param base_url: str: 环境地址
    :param path: api地址
    :param model: str：用例级别
    :param mode: boolean：True 同步 False: 异步
    :return:
    """
    """
    里面代码为源代码
        if mode:
            for index in range(len(test_list) - 2):
                form_test = test_list[index].split('=')
                value = form_test[1]
                if model == 'project':
                    run_by_project(value, base_url, path)
                elif model == 'module':
                    run_by_module(value, base_url, path)
                elif model == 'suite':
                    run_by_suite(value, base_url, path)
                else:
                    run_by_single(value, base_url, path)

        else:
            if model == 'project':
                for value in test_list.values():
                    run_by_project(value, base_url, path)

            elif model == 'module':
                for value in test_list.values():
                    run_by_module(value, base_url, path)
            elif model == 'suite':
                for value in test_list.values():
                    run_by_suite(value, base_url, path)

            else:
                for index in range(len(test_list) - 1):
                    form_test = test_list[index].split('=')
                    index = form_test[1]
                    run_by_single(index, base_url, path)

    """

    dispatch_dic = {
        'project': run_by_project,
        'module': run_by_module,
        'suite': run_by_suite,
    }
    if not mode:
        for value in test_list.values():
            dispatch_dic.get(model, run_by_single)(value, base_url, path)
    else:

        for index in range(len(test_list) - 2):
            form_test = test_list[index].split('=')
            value = form_test[1]
            dispatch_dic.get(model, run_by_single)(value, base_url, path)


def run_by_module(pk, base_url, path):
    """
    模块的运行
    :param pk: int or str：模块索引
    :param base_url: str：环境地址
    :param path:  str：api地址
    :return:
    """
    obj = ModuleInfo.objects.get(id=pk)
    test_index_list = TestCaseInfo.objects.filter(belong_module=obj, type=1).values_list('id')
    for index in test_index_list:
        run_by_single(index[0], base_url, path)


def run_by_project(pk, base_url, path):
    """
    组装项目用例
    :param pk: int or str：项目索引
    :param base_url: 环境地址
    :param path: api地址
    :return:
    """

    obj = ProjectInfo.objects.get(id=pk)
    module_index_list = ModuleInfo.objects.filter(belong_project=obj).values_list('id')
    for index in module_index_list:
        module_id = index[0]
        run_by_module(module_id, base_url, path)


def run_test_by_type(pk, base_url, path, model):
    """
    按照类型运行
    :param pk: 索引
    :param base_url: 环境地址
    :param path: api地址
    :param model: 类型
    :return:
    """

    """
    if type == 'project':
        run_by_project(id, base_url, path)
    elif type == 'module':
        run_by_module(id, base_url, path)
    elif type == 'suite':
        run_by_suite(id, base_url, path)
    else:
        run_by_single(id, base_url, path)

    """
    dispatch_dic = {
        'project': run_by_project,
        'module': run_by_module,
        'suite': run_by_suite,
    }

    dispatch_dic.get(model, run_by_single)(pk, base_url, path)
