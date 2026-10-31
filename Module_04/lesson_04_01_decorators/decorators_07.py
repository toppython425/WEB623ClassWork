from functools import wraps


def authorise_admin(func):
    @wraps(func)
    def wrapper(user):
        if user == 'admin':
            return func()
        else:
            print(f'Доступ запрещен!')
            return False

    return wrapper


@authorise_admin
def secret():
    print(f'Секретная информация!')


if __name__ == '__main__':
    secret('user')
    secret('admin')
