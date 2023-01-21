import pytest
import main

def test_Phibonachi_Correct ():
    assert main.Phibonachi(6) == [1, 1, 2, 3, 5, 8]
def test_Phibonachi_InCorrect ():
    assert main.Phibonachi(7) == [1, 1, 2, 3, 5, 8]
def test_Bubble_Correct ():
    assert main.Bubble([3, 1, 2, 4, 7, 6, 5]) == [1, 2, 3, 4, 5, 6, 7]
def test_Bubble_InCorrect ():
    assert main.Bubble([3, 1, 2, 4, 7, 6, 5]) == [1, 3, 2, 4, 5, 6, 7]
def test_Calc_Correct1 ():
    assert main.Calc(2, 3, '+') == 5
def test_Calc_Correct2 ():
    assert main.Calc(2, 3, '-') == -1
def test_Calc_Correct3 ():
    assert main.Calc(2, 3, '*') == 6
def test_Calc_InCorrect ():
    assert main.Calc(2, 3, '*') == 7
    
