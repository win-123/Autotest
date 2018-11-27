from django.db import models


class UserTypeManager(models.Manager):
    """
    用户类型表操作
    """
    def insert_user_type(self, user_type):
        """
        添加用户类型
        :param user_type:
        :return:
        """
        self.create(user_type=user_type)

    def insert_type_name(self, type_name):
        """
        添加类型名
        :param type_name:
        :return:
        """
        self.create(type_name=type_name)

    def insert_type_desc(self, type_desc):
        """
        类型描述
        :param type_desc:
        :return:
        """
        self.create(type_desc=type_desc)

    def get_objects(self, user_type_id):  # 根据user_type得到一条数据
        return self.get(user_type_id=user_type_id)


class UserInfoManager(models.Manager):
    """
    用户信息表操作
    """
    def insert_user(self, username, password, email, object):  # 创建用户
        self.create(username=username, password=password, email=email, user_type=object)

    def query_user(self, username, password):  #
        return self.filter(username__exact=username, password__exact=password).count()


class ProjectInfoManager(models.Manager):
    """
    项目信息表操作
    """
    def insert_project(self, **kwargs):
        self.create(**kwargs)

    def update_project(self, id, **kwargs):  # 如此update_time才会自动更新！！
        obj = self.get(id=id)
        obj.project_name = kwargs.get('project_name')
        obj.responsible_name = kwargs.get('responsible_name')
        obj.test_user = kwargs.get('test_user')
        obj.dev_user = kwargs.get('dev_user')
        obj.publish_app = kwargs.get('publish_app')
        obj.simple_desc = kwargs.get('simple_desc')
        obj.other_desc = kwargs.get('other_desc')
        obj.save()

    def get_pro_name(self, pro_name, type=True, id=None):
        if type:
            return self.filter(project_name__exact=pro_name).count()
        else:
            if id is not None:
                return self.get(id=id).project_name
            return self.get(project_name__exact=pro_name)

    def get_pro_info(self, type=True):
        if type:
            return self.all().values('project_name')
        else:
            return self.all()


class ModuleInfoManager(models.Manager):
    """
    模块信息表操作
    """
    def insert_module(self, **kwargs):
        self.create(**kwargs)

    def update_module(self, id, **kwargs):
        obj = self.get(id=id)
        obj.module_name = kwargs.get('module_name')
        obj.test_user = kwargs.get('test_user')
        obj.simple_desc = kwargs.get('simple_desc')
        obj.other_desc = kwargs.get('other_desc')

        obj.save()

    def get_module_name(self, module_name, type=True, id=None):
        if type:
            return self.filter(module_name__exact=module_name).count()
        else:
            if id is not None:
                return self.get(id=id).module_name
            else:
                return self.get(id=module_name)


class TestCaseInfoManager(models.Manager):
    """
    用例信息表操作
    """
    def insert_case(self, belong_module, **kwargs):
        case_info = kwargs.get('test').pop('case_info')
        self.create(name=kwargs.get('test').get('name'), belong_project=case_info.pop('project'),
                    belong_module=belong_module,
                    author=case_info.pop('author'), include=case_info.pop('include'), request=kwargs)

    def update_case(self, belong_module, **kwargs):
        """
        更新操作
        :param belong_module:
        :param kwargs:
        :return:
        """
        case_info = kwargs.get('test').pop('case_info')
        obj = self.get(id=case_info.pop('test_index'))
        obj.belong_project = case_info.pop('project')
        obj.belong_module = belong_module
        obj.name = kwargs.get('test').get('name')
        obj.author = case_info.pop('author')
        obj.include = case_info.pop('include')
        obj.request = kwargs
        obj.save()

    def insert_config(self, belong_module, **kwargs):
        config_info = kwargs.get('config').pop('config_info')
        self.create(name=kwargs.get('config').get('name'), belong_project=config_info.pop('project'),
                    belong_module=belong_module,
                    author=config_info.pop('author'), type=2, request=kwargs)

    def update_config(self, belong_module, **kwargs):
        config_info = kwargs.get('config').pop('config_info')
        obj = self.get(id=config_info.pop('test_index'))
        obj.belong_module = belong_module
        obj.belong_project = config_info.pop('project')
        obj.name = kwargs.get('config').get('name')
        obj.author = config_info.pop('author')
        obj.request = kwargs
        obj.save()

    def get_case_name(self, name, module_name, belong_project):
        return self.filter(belong_module__id=module_name).filter(name__exact=name).filter(
            belong_project__exact=belong_project).count()

    def get_case_by_id(self, index, type=True):
        if type:
            return self.filter(id=index).all()
        else:
            return self.get(id=index).name


class EnvInfoManager(models.Manager):
    """
    环境变量管理
    """
    def insert_env(self, **kwargs):
        self.create(**kwargs)

    def update_env(self, index, **kwargs):
        obj = self.get(id=index)
        obj.env_name = kwargs.pop('env_name')
        obj.base_url = kwargs.pop('base_url')
        obj.simple_desc = kwargs.pop('simple_desc')
        obj.save()

    def get_env_name(self, index):
        return self.get(id=index).env_name

    def delete_env(self, index):
        self.get(id=index).delete()
