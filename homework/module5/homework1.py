def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()
# Попытка вызова inner_function вне функции: test_function вызовет ошибку, так как inner_function не видна вне test_function
