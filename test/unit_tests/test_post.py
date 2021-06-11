from module.post import Post
import os

def test_create():
    p = Post("fake_post", "some date", "post_text")
    assert isinstance(p, Post)

def test_write():
    try:
        filename = "test_file_name.txt"
        p = Post("abcde", "1234", "qwert")
        p.print_to_file(filename)

        with open(filename, 'r') as file:
            file_contnt = file.readlines()
            assert "abcde\n" in file_contnt
            assert "1234\n" in file_contnt
            assert "qwert\n" in file_contnt
    finally:
        os.remove(filename)
