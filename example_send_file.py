import os 

print(os.path.abspath(__file__)) # /home/grig/environments/selenium_course/example_send_file.py
print(os.path.abspath(os.path.dirname(__file__))) # /home/grig/environments/selenium_course
print(os.getcwd()) # текущий каталог пользователя который запустил скрипт


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
# вариант: os.getcwd() текущий
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
'''
Элемент в форме, который выглядит, как кнопка добавления файла, имеет атрибут type="file".
Мы должны сначала найти этот элемент с помощью селектора, а затем применить к нему 
метод send_keys(file_path)
'''
element.send_keys(file_path)
'''
для создания временных файлов:
https://docs.python.org/3/library/tempfile.html#module-tempfile
https://docs.python.org/3/library/tempfile.html#tempfile.mkstemp
'''