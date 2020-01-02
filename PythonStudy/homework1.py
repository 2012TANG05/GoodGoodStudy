name = input('请输入您的姓名：')
gender = input('请输入您的性别：')
age = input('请输入您的年龄：')
school = input('请输入您的学校：')
info = '''
正在生成您的简历......

******************************
             简历

姓名：{_name}
性别：{_gender}
年龄：{_age}
学校：{_school}
'''.format(_name = name, _gender = gender, _age = age, _school = school)
print(info)