import unittest

from api.crawler import PokeAPI

class TestPokeApi(unittest.TextCase)

    def test_poke_api(self):
        print(PokeAPI().get_basic_information)