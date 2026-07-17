import os
import unittest

os.environ.setdefault("TESTING", "true")

from peewee import SqliteDatabase

from app import TimelinePost

MODELS = [TimelinePost]

# Use an in-memory SQLite database for tests, per the Peewee docs:
# https://docs.peewee-orm.com/en/latest/peewee/database.html#testing-peewee-applications
test_db = SqliteDatabase(":memory:")


class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_create_and_retrieve_timeline_post(self):
        TimelinePost.create(
            name="Ada Lovelace",
            email="ada@example.com",
            content="Hello, world!",
        )

        # TODO: retrieve the list of timeline posts, same as the
        # GET /api/timeline_post endpoint in app/__init__.py does.
        posts = list(TimelinePost.select().order_by(TimelinePost.created_at.desc()))

        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0].name, "Ada Lovelace")
        self.assertEqual(posts[0].email, "ada@example.com")
        self.assertEqual(posts[0].content, "Hello, world!")

    def test_retrieve_returns_empty_when_no_posts(self):
        posts = list(TimelinePost.select())
        self.assertEqual(posts, [])


if __name__ == "__main__":
    unittest.main()
