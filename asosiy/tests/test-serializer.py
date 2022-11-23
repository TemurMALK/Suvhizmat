from unittest import *
from water.models import *





from asosiy.water.serializers import *


class TestMijozSer(TestCase):
    def setUP(self) -> None:
        self.data = {
            "id": 1, "ism": "Ali",
            "manzil": "Marg'ilon, markaz",
            "tel": "+998916693704", "qarz": 0,  "user":User.objects.get(id=1)}

    def test_mijoz_ser(self):
        assert self.data['ism']=="Ali"
        assert self.data['manzil'] == "Marg'ilon, markaz"
        assert self.data['qarz'] == 0
        assert self.data['id'] == 1

