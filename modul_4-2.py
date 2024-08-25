def test_function():
    def  inner_function():
        print('Я в области видимости функции test_function')


    inner_function ()
test_function()

#inner_function ()- при вызове функции inner_function() вне функции test_function() появляется сообщение об ошибке: "Имя функции не попределено