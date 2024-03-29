import pytest
from main.ds.stack.DelimiterMatcher import DelimiterMatch


def testSimplePositiveCase():
    algo = DelimiterMatch("c[a]")
    assert algo.isValid() == True


def testSimpleNegativeCase1():
    algo = DelimiterMatch("c[a")
    assert algo.isValid() == False


def testSimpleNegativeCase2():
    algo = DelimiterMatch("ca]")
    assert algo.isValid() == False


def testComplexCase1():
    algo = DelimiterMatch("a{b[c]d}e")
    assert algo.isValid() == True

def testComplexCase2():
    algo = DelimiterMatch("a{b(c]d}e")
    assert algo.isValid() == False

def testComplexCase3():
    algo = DelimiterMatch("a[b{c}d]e}")
    assert algo.isValid() == False


def testComplexCase1():
    algo = DelimiterMatch("{a[(b<c>)d]e}")
    assert algo.isValid() == True
