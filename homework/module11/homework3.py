import inspect


def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    info['module'] = obj.__class__.__module__
    if isinstance(obj, int):
        info['value'] = obj
    elif isinstance(obj, str):
        info['length'] = len(obj)
    elif isinstance(obj, list):
        info['length'] = len(obj)
        info['first_element'] = obj[0] if obj else None
    return info


number_info = introspection_info(42)
print(number_info)


class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")


my_obj = MyClass(10)
my_obj_info = introspection_info(my_obj)
print(my_obj_info)
