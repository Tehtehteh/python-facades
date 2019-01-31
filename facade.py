class FacadeMeta(type):

    def __new__(mcs, name, bases, dct):
        facade: Facade = super().__new__(mcs, name, bases, dct)
        facade.resolved_instances = mcs.resolved_instances
        mcs.__getattr__ = facade.resolve_facade_instance
        return facade


class Facade(metaclass=FacadeMeta):
    application = None
    resolved_instances = {}

    @staticmethod
    def set_facade_application(application):
        Facade._application = application

    @staticmethod
    def get_facade_application():
        return Facade.application

    @staticmethod
    def call_static(method: str, *args, **kwargs):
        instance = Facade.get_facade_root()
        if not instance:
            raise Exception("A facade root has not been set.")
        return instance.get(method, *args, **kwargs)

    @staticmethod
    def get_facade_root():
        accessor = Facade.get_facade_accessor()
        return Facade.resolve_facade_instance(None, accessor)

    @staticmethod
    def get_facade_accessor():
        raise Exception("Facade does not implement `get_facade_accessor` method.")

    @staticmethod
    def resolve_facade_instance(meta, name: str):
        facading_service = meta.get_facade_accessor()
        if Facade.resolved_instances[facading_service]:
            return getattr(Facade.resolved_instances[facading_service], name)
        elif Facade.application[name]:
            Facade.resolved_instances[name] = Facade.application[name]
            return getattr(Facade.resolved_instances[facading_service], name)
        else:
            raise Exception(f"No instance for facading service {facading_service} found.")
