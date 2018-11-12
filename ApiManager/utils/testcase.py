import io
import json
import time

import yaml


def get_time_stamp():
    current_time = time.time()
    local_time = time.localtime(current_time)
    data_head = time.strftime("%Y-%m-%d %H-%M-%S", local_time)
    data_secs = (current_time - int(current_time)) * 1000
    time_stamp = "%s-%03d" % (data_head, data_secs)
    return time_stamp


def dump_yaml_file(yaml_file, data):
    """
    load yaml file and check file content format
    :param yaml_file:
    :param data:
    :return:
    """

    with io.open(yaml_file, 'w', encoding='utf-8') as stream:
        yaml.dump(data, stream, indent=4, default_flow_style=False, encoding='utf-8')


def _dump_json_file(json_file, data):
    """
    load json file and check file content format
    :param json_file:
    :param data:
    :return:
    """

    with io.open(json_file, 'w', encoding='utf-8') as stream:
        json.dump(data, stream, indent=4, separators=(',', ': '), ensure_ascii=False)


def dump_python_file(python_file, data):
    """
    :param python_file:
    :param data:
    :return:
    """

    with io.open(python_file, 'w', encoding='utf-8') as stream:
        stream.write(data)
