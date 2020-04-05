from cool_package.app import hello_world
from assertpy import assert_that


def test_hello_world_says_hello_world():
    assert_that(hello_world(), "Hello world message is printed").is_equal_to(
        "Hello World!")
