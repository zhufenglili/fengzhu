import pytest
import yaml


class Test_data:
    @pytest.mark.parametrize('a,b',yaml.safe_load(open('./data.yml')))
    def test_data(self,a,b):

        print(a+b)
