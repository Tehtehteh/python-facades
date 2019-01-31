from facade import Facade


class Cache(Facade):

    @staticmethod
    def get_facade_accessor() -> str:
        return 'cache'


if __name__ == '__main__':
    heh = Cache.get('Heh')
    print(heh)
