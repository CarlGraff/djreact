import sys
import subprocess

print("==================")
res = subprocess.check_output(["which", "python"])
# for line in res.splitlines():
#     print(line)
print(res)
print(sys.version)
print(sys.executable)
print("==================")


#print(subprocess.call(["which", "python"])[0])
# print(sys.version)
# print(sys.executable)
# print("hello")

# print("python manage.py runserver")
# print("python manage.py migrate")
# print("python manage.py makemigrations")
# print("python manage.py migrate")
# print("python manage.py startapp articles")
# print("python manage.py createsuperuser")
# seagraph djReact53 double