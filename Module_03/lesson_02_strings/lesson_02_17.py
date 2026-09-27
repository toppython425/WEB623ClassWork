from string import Template

my_template = Template("$user_login имеет права: $user_access, в приложении $app_name")

users_list = [["Admin", 'superuser', 'E-Shop'],
              ["User1787", 'guest', 'E-Shop'],
              ["Moderator", 'is_staff', 'E-Shop']]
users_list_formatted = []

for login, access, app in users_list:
    user_info = my_template.substitute(
        user_login=login,
        user_access=access,
        app_name=app
    )
    users_list_formatted.append(user_info)

for user in users_list_formatted:
    print(user)
