import unittest
from blog import Blog

class BlogTest(unittest.TestCase):

    def setUp(self):
        self.blog = Blog("TestBlog", "Testauthor")

    def test_blog__init__(self):
        self.assertEqual(self.blog.title, "TestBlog")
        self.assertEqual(self.blog.author, "Testauthor")
        self.assertListEqual(self.blog.posts, [])

    def test_blog__repr__(self):
        self.assertEqual(self.blog.__repr__(), "TestBlog by Testauthor (0 post)")

    def test_create_post(self):
        self.blog.create_post("TestPostTitle", "TestPostContent")

        post = [{"title" : "TestPostTitle", "content" : "TestPostContent"}]
        self.assertEqual(len(self.blog.posts), 1)
        self.assertListEqual(self.blog.posts, post)
        self.assertEqual(self.blog.__repr__(), "TestBlog by Testauthor (1 post)")


    def test_json(self):
        self.blog.create_post("TestPostTitle", "TestPostContent")

        data = {
            "title" : self.blog.title,
            "author" : self.blog.author,
            "posts": [{"title" : "TestPostTitle", "content" : "TestPostContent"}]
        }
        self.assertDictEqual(self.blog.json(), data)


if __name__ == "__main__":
    unittest.main()