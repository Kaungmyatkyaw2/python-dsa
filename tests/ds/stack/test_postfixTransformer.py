import pytest
from main.ds.stack.PostfixTransformer import PostfixTransformer


def testBaseCase():
    converter = PostfixTransformer()
    assert converter.transform("a+b") == "ab+"


def testStepThreePointOne():
    converter = PostfixTransformer()
    assert converter.transform("a+b*c") == "abc*+"


def testStepThreePointTwo():
    converter = PostfixTransformer()
    assert converter.transform("a*b+c") == "ab*c+"


def testStepThreePointThree():
    converter = PostfixTransformer()
    assert "ab-c+d+e-" == converter.transform("a-b+c+d-e")


def testParathesis():
    converter = PostfixTransformer()
    assert "ab+c*" == converter.transform("(a+b)*c")


def testParathesis():
    converter = PostfixTransformer()
    assert "ab+cd/*" == converter.transform("(a+b)*(c/d)")
    assert "abd/+cf/e+*" == converter.transform("(a+b/d)*(c/f+e)")
    assert "ab+d-cd*e/*" == converter.transform("(a+b-d)*(c*d/e)")
    assert "ab/d+cf-e+x+z-*" == converter.transform("(a/b+d)*(c-f+e+x-z)")
