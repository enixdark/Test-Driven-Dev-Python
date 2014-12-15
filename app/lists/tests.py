from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import index_page,home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
# Create your tests here.
from .models import Item

class ItemTest(TestCase):

    def test_save_and_retrive(self):
        first_item = Item()
        first_item.text = "The first item on list"
        first_item.save()

        second_item = Item()
        second_item.text = "the second item"
        second_item.save()

        _list_item = Item.objects.all()
        self.assertEquals(_list_item.count(),2)
        first_saved_item = _list_item[0]
        second_saved_item = _list_item[1]

        self.assertEqual(first_saved_item.text, u'The first item on list')
        self.assertEqual(second_saved_item.text, u'the second item')
        _list_item.delete()
        self.assertEquals(_list_item.count(),0)


class SmokeTest(TestCase):
    def test_bad_math(self):
        self.assertEquals(1+1,2)

    # def test_root_home_url(self):
    #     found = resolve('/')
    #     self.assertEquals(found.func,index_page)
    #     self.assertEquals(found.func,home_page)

    def test_index_return(self):
        request = HttpRequest()
        response = index_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>',response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

    def test_home_return(self):
        request = HttpRequest()
        response = home_page(request);
        _home = render_to_string("lists/home.html")
        _index = render_to_string('lists/index.html')
        _content = response.content.decode()
        self.assertEquals(_content,_home)
        self.assertNotEquals(_content,_index)



    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        response = index_page(request)
        self.assertIn('A new list item', response.content.decode())

        expected_html = render_to_string(
            'lists/home.html',
            {'new_item_text': 'A new list item'}
        )
        # self.check_for_row_in_list_table('1: Buy peacock feathers')
        # def test_atomic_transaction(self):
    #     request = HttpRequest()
    #     response = example_non_atomic(request,1,"OK")
    #     print response
    #     self.assertIn("OK",response.content)
