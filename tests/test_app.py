import os
import unittest

os.environ.setdefault("TESTING", "true")

from app import app, mydb, TimelinePost

MODELS = [TimelinePost]


class TimelineApiTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.testing = True
        mydb.create_tables(MODELS)

    def tearDown(self):
        TimelinePost.delete().execute()

    # TODO 1: GET /api/timeline_post should return an empty list when
    # no posts have been created yet.
    def test_get_timeline_posts_empty(self):
        response = self.client.get("/api/timeline_post")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"timeline_posts": []})

    # TODO 2: POST /api/timeline_post should create a new post and
    # return it back to the caller.
    def test_create_timeline_post(self):
        response = self.client.post(
            "/api/timeline_post",
            data={
                "name": "Ada Lovelace",
                "email": "ada@example.com",
                "content": "Hello, world!",
            },
        )
        body = response.get_json()

        self.assertEqual(body["name"], "Ada Lovelace")
        self.assertEqual(body["email"], "ada@example.com")
        self.assertEqual(body["content"], "Hello, world!")

        get_response = self.client.get("/api/timeline_post")
        self.assertEqual(len(get_response.get_json()["timeline_posts"]), 1)

    # TODO 3: DELETE /api/timeline_post/<id> should remove an existing post.
    def test_delete_timeline_post(self):
        post = TimelinePost.create(
            name="Grace Hopper", email="grace@example.com", content="Bug found!"
        )

        response = self.client.delete(f"/api/timeline_post/{post.id}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"deleted": post.id})
        self.assertIsNone(TimelinePost.get_or_none(TimelinePost.id == post.id))

    # --- TDD: error / edge cases -------------------------------------
    # These describe behavior the application does not implement yet.
    # Run the suite to see them fail, then update app/__init__.py until
    # they pass.

    def test_create_timeline_post_missing_field_returns_400(self):
        response = self.client.post(
            "/api/timeline_post",
            data={"name": "Ada Lovelace", "email": "ada@example.com"},
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_create_timeline_post_returns_201(self):
        response = self.client.post(
            "/api/timeline_post",
            data={
                "name": "Ada Lovelace",
                "email": "ada@example.com",
                "content": "Hello, world!",
            },
        )

        self.assertEqual(response.status_code, 201)

    def test_delete_nonexistent_timeline_post_returns_404(self):
        response = self.client.delete("/api/timeline_post/999999")

        self.assertEqual(response.status_code, 404)
        self.assertIn("error", response.get_json())


if __name__ == "__main__":
    unittest.main()
