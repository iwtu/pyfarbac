import contextvars
from pydantic import BaseModel, root_validator
from pydantic.main import ModelMetaclass

rbac_model_roles = {"pyfarbac.models.foo.OutputFoo": {"arole": ["f1"]}}


class Meta(ModelMetaclass):
    def __new__(cls, name, bases, dct):
        _cls = super().__new__(cls, name, bases, dct)
        if name != "RBACBase":
            assert hasattr(_cls, "_path"), f"_path attribute needs to be set in class: {name}"
        return _cls

context_role = contextvars.ContextVar("context_role", default=None)


class RBACBase(BaseModel, metaclass=Meta):
    @root_validator(pre=True)
    def rbac(cls, values):
        # print(pydantic.utils.version_info())
        print(cls)
        print(cls.__class__)
        role = context_role.get()
        print(rbac_model_roles)
        print(f"class fullname: {cls._path}.{cls.__name__}")
        fields = rbac_model_roles[f"{cls._path}.{cls.__name__}"][role]
        values = {k: v for k, v in values.items() if k in fields}

        return values


def set_context_role(role: str):
    context_role.set(str(role))


def _get_test_role_fields():
    return
