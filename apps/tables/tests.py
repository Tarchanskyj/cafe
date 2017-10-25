from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.tables.models import Table



class LoginViewTest(TestCase):

    def test_view_url_accessible_for_staff(self):
        resp = self.client.get(reverse('tables:tables'))
        self.assertEqual(resp.status_code, 200)

class TableListTest(TestCase):
    def test_table_create(self):
        create_table()
        self.assertEqual(Table.objects.all().count(), 1)


def create_table():
    table = Table.objects.create(number='1', x=50, y=23, length=14, width=20, shape='oval')
    return table