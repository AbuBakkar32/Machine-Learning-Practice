from unittest import TestCase

import samples1
from mock import patch, Mock, MagicMock, call, sentinel
from samples1 import Customer


class MyTestCase(TestCase):

    def setUp(self):
        sentinel.attribute = "FOO"

    def test_passing_mock_object(self):
        """
        Test if method was called on mock object which was passed as argument
        to some method. Pass an object into a method (or some part of the system under test)
        and then check that it is used in the correct way.

        The ProductionClass has a closer method. Validate using mocks that
        ProductionClass.closer() actually called close() method of its argument
        """

        real = samples1.ProductionClass()
        mock = Mock()
        real.closer(mock)
        mock.close.assert_called_with()

    def test_mocking_classes(self):
        """
        A common use case is to mock out classes instantiated by your code under
        test. When you patch a class, then that class is replaced with a mock.
        Instances are created by calling the class. This means you access the
        'mock instance' by looking at the return value of the mocked class.
        In the example below we have a function some_function that instantiates Foo
        and calls a method on it. The call to patch() replaces the class Foo with a
        mock. The Foo instance is the result of calling the mock, so it is configured
        by modifying the mock return_value
        """
        import samples2
        with patch('samples1.Customer') as mock:
            instance = mock.return_value
            instance.get_data.return_value = 'the result'
            result = samples2.some_function()
            assert result == 'the result'

    def test_tracking_all_calls(self):
        """
        Often you want to track more than a single call to a method. The mock_calls attribute records all calls
        to child attributes of the mock - and also to their children.
        """
        mock = MagicMock()
        mock.my_method()  # one call without args
        mock.my_method(10, x=53)  # another call with args
        mock.some_attr.my_method(999)  # yet another dummy call to dummy obj
        calls = mock.mock_calls
        # print calls
        expected = [call.my_method(), call.my_method(10, x=53), call.some_attr.my_method(999)]
        assert calls == expected

    def test_naming_your_mocks(self):
        """
        It can be useful to give your mocks a name.
        The name is shown in the repr of the mock and can be helpful when
        the mock appears in test failure messages.
        The name is also propagated to attributes or methods of the mock
        """
        mock = MagicMock(name='foo')
        assert mock.__repr__().find("name='foo'") > 0
        assert mock.method.__repr__().find("name='foo.method'") > 0

    def test_setting_return_values_and_attributes(self):
        # Setting the return values on a mock object is trivially easy
        mock = Mock()
        mock.return_value = 3
        v = mock()
        assert v == 3

        # Of course you can do the same for methods on the mock
        mock = Mock()
        mock.my_dummy_method.return_value = 3
        v = mock.my_dummy_method()
        assert v == 3

        # The return value can also be set in the constructor
        mock = Mock(return_value=3)
        assert mock() == 3

        # If you need an attribute setting on your mock, just do it
        mock = Mock()
        mock.x = 3
        assert mock.x == 3

    def test_create_mock_from_existing_object(self):
        """
        Creating a Mock from an Existing Object
        """
        from samples1 import Customer
        mock = MagicMock(spec=Customer)
        mock.my_method(1, 2)
        mock.my_method.assert_called_with(1, 2)
        mock.my_method(arg1=1, arg2=2)
        mock.my_method.assert_called_with(arg1=1, arg2=2)

    @patch.object(Customer, '_some_data', "hehehe")
    def test_patch_decorators(self):
        """
        Patch Decorators
        """
        assert Customer._some_data == "hehehe"  # the attributed is patched
        Customer.init()  # calling real class method resets attribute to its real state
        assert Customer._some_data == [1, 2, 3]  # And for real Customer class it should be [1,2,3]

    @patch('samples1.my_module_attribute', "FOO")
    def test_patch_decorators(self):
        """
        Patch Decorators
        """
        # the attribute is patched, the patch value will disapear on exit from this method
        from samples1 import my_module_attribute
        assert my_module_attribute == "FOO"


Customer.init()
original = Customer._some_data


@patch.object(Customer, '_some_data', sentinel._some_data)
def test():
    assert Customer._some_data == sentinel._some_data


test()
assert Customer._some_data == original
