from module.post import Post
import os

def test_create():
    """Creating an instance of object Post
    """
    p = Post("fake_post", "some date", "post_text", ["1", "2"], ["1", "2", "3"])
    assert isinstance(p, Post)

def test_txt():
    """Creating a .txt file with post data
    """
    try:
        filename = "test_file_name.txt"
        p = Post("abcde", "1234", "qwert", ["1", "2"], ["1", "2", "3"])
        p.print_to_text_file(filename)

        with open(filename, 'r') as file:
            file_content = file.readlines()
            assert "abcde\n" in file_content
            assert "1234\n" in file_content
            assert "qwert\n" in file_content
    finally:
        os.remove(filename)

def test_json():
    """Creating a .json file with post data
    """
    try:
        filename = "test_file_name.json"
        p = Post("abcde", "1234", "qwert", comments=None, first_paragraphs=["1", "2", "3"])
        json_obj = p.get_as_json_object()
        Post.print_to_json_file([json_obj], filename)
        
        with open(filename, 'r') as file:
            file_content = file.readlines()
            assert 'title_1' in str(file_content)
            assert 'abcde' in str(file_content)
            assert 'most_used_words' in str(file_content)
    finally:
        os.remove(filename)
