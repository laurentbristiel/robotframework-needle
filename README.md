robotframework-needle
=====================

CSS Automated tests library used with Robot Framework.
Quick demonstration of how Needle can be called from Robot Framework tests.

1) install Selenium and Needle library
See [needle documentation](http://needle.readthedocs.org/en/latest/)

2) install geckodriver
See [this Stack Overflow answer](https://stackoverflow.com/a/40314803/1826804)

3) launch test a first time to initialize baseline image
```
robot --test needle_visual_test_first_time test-example.robot
```
=> screenshot is created in screenshots/baseline

4) launch again a test to check visual regression
```
robot --test needle_visual_test_next_times test-example.robot
```