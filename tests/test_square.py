'''
Created on 05-Jul-2020

@author: venkateshwara D
'''
import pytest
import math

@pytest.mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

@pytest.mark.others
def test_equality():
    assert 10 == 11
