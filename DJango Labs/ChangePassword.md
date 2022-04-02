```console
C:\Users\jarom\AppData\Local\Programs\Python\Python39\python.exe "C:\Program Files\JetBrains\PyCharm 2021.3\plugins\python\helpers\pydev\pydevconsole.py" --mode=client --port=60639
import sys; print('Python %s on %s' % (sys.version, sys.platform))
import django; print('Django %s' % django.get_version())
sys.path.extend(['C:\\Users\\jarom\\PycharmProjects\\hollymovies_pt5', 'C:\\Program Files\\JetBrains\\PyCharm 2021.3\\plugins\\python\\helpers\\pycharm', 'C:\\Program Files\\JetBrains\\PyCharm 2021.3\\plugins\\python\\helpers\\pydev'])
if 'setup' in dir(django): django.setup()
import django_manage_shell; django_manage_shell.run("C:/Users/jarom/PycharmProjects/hollymovies_pt5")
Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.28.0 -- An enhanced Interactive Python. Type '?' for help.
PyDev console: using IPython 7.28.0
Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Django 4.0.2
from django.contrib.auth import get_user_model
get_user_model()
Out[3]: django.contrib.auth.models.User
user = get_user_model().objects.all()
user
Out[5]: <QuerySet []>
user.change_password('admin12345')
Traceback (most recent call last):
  File "C:\Users\jarom\AppData\Local\Programs\Python\Python39\lib\site-packages\IPython\core\interactiveshell.py", line 3444, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-6-f956f2438a82>", line 1, in <module>
    user.change_password('admin12345')
AttributeError: 'QuerySet' object has no attribute 'change_password'
user.set_password('admin12345')
Traceback (most recent call last):
  File "C:\Users\jarom\AppData\Local\Programs\Python\Python39\lib\site-packages\IPython\core\interactiveshell.py", line 3444, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-7-c317f00a6fdd>", line 1, in <module>
    user.set_password('admin12345')
AttributeError: 'QuerySet' object has no attribute 'set_password'
user = get_user_model().objects.all()
user
Out[9]: <QuerySet [<User: admin>]>
user.set_password('admin54321')
Traceback (most recent call last):
  File "C:\Users\jarom\AppData\Local\Programs\Python\Python39\lib\site-packages\IPython\core\interactiveshell.py", line 3444, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-10-8a07e1901eb5>", line 1, in <module>
    user.set_password('admin54321')
AttributeError: 'QuerySet' object has no attribute 'set_password'
user = get_user_model().objects.all().first()
user
Out[12]: <User: admin>
user.set_password('admin54321')
user.save()
```
