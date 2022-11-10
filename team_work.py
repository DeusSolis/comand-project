
# привіт командо!!! Давайте разом попрацюємо.
# якщо Ви не проти, то ідея така:
"""
Ви пишете любу функцію, яка повертає, що завгодно. НА Ваш смак.
А я напишу декоратор, який виводить командою print результат роботи функції.
Ніхто не проти? function_1 - буде декоратором.

"""
# створюємо декоратор
def func_print(func):

    def wrapper():
        print('результат виконання функції {0}  = {1}'.format(func.__name__, func()))

    return wrapper


@func_print
def function_2():
    pass

@func_print
def function_3():
    pass

def html_special_chars(data):
    """Функція яка перетворює 'потенційно небезпечні символи :)' """
    a = {"<" : "&lt;",">" : "&gt;","\"": "&quot;","&" : "&amp;"}
    return "".join((a.get(i,i)) for i in data)

if __name__ == '__main__':
    function_3()