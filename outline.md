%title: Mocks 'n Stuff (Python Remix)
%author: Sam Mayer
%date: Thu 09 Apr 2020

-> Mocks 'n Stuff (Python Remix) <-
===

-> A basic introduction to Python's `unittest.mock` object

Included with python 3.3 or newer. Otherwise, `pip install mock`
[Documentation here](https://docs.python.org/3/library/unittest.mock.html)
[Inspired by Mahdi Yusuf](https://www.youtube.com/watch?v=GYkGguhdqw00)

---

-> What does it do? <-
===
> 
> "Replace parts of your SUT with mock objects and make assertions about their use."
> 

* Assert behavior of YOUR code
* Reduce external test-dependencies
* Bypass complex or "expensive" functions	
* API tests

---

-> Audience Assumptions <-
===

* Familiar with Python
* Installed course resources
* Understand value of TDD

---

-> Using Mock <-
===

Designing your mocks is usually harder than implementing them.

* `Mock` and `MagicMock` are class names, not test-doubles
* `MagicMock` implements magic methods
	- `__init__`
	- `__new__`
	- `__del__`
* Use `Mock` unless you know what you're doing

---

-> Test Doubles <- 
===

* *Dummy* - Ensure never used ( `side_effect` ) 
* *Stub* - Read only ( `return_value` )
* *Spy* - Write only ( `called_with` )
* *Fake* - Stub + Spy
* *Mock* - Self-verifying spy ( `side_effect` )

---

-> SUT - Sam's Aquarium <-
===

* 60gal
* 25 fish
* Water changes = SLOW

---

-> Pitfalls of Mocking <-
===

* Mocking \!= Panacea (cure-all)
* Do not ignore integration tests
* Test pyramid still applies
	- (unit, integration, journey)

---

-> Additional Resources <-
===

* [Mock a function in Pythyon](https://fgimian.github.io/blog/2014/04/10/using-the-python-mock-library-to-fake-regular-functions-during-tests/)
* [Pivotal's Test-Double QuickRef](http://engineering.pivotal.io/post/the-test-double-rule-of-thumb/)
* [Mock vs MagicMock](https://stackoverflow.com/questions/17181687/mock-vs-magicmock)
* [Testing for exceptions](https://ongspxm.github.io/blog/2016/11/assertraises-testing-for-errors-in-unittest/)

