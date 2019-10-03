'''Переход на новую вкладку'''

browser.switch_to.window(window_name)
'''
Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, 
который возвращает массив имён всех вкладок. Зная, что в браузере теперь 
открыто две вкладки, выбираем вторую вкладку:
'''
new_window = browser.window_handles[1]

'''Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:'''
first_window = browser.window_handles[0]
'''
После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить 
уже на новой странице.

Текущую вкладку можно узнать так:
'''
current_window = browser.current_window_handle

'''
закрыть вкладку
'''
browser.close()

'''
Chrome вроде бы возвращает страницы в том порядке, в котором они были открыты. 
Но лучше на это не рассчитывать и запоминать идентификатор текущей открытой вкладки '''
first_window = browser.window_handles[0] 
'''и затем использовать его, чтобы вернуться к странице с помощью switch_to.window
'''