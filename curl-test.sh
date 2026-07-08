#!/bin/bash

BASE_URL="http://127.0.0.1:5000/api/timeline_post"

# Generate somewhat random test data
RANDOM_ID=$RANDOM
NAME="TestUser$RANDOM_ID"
EMAIL="testuser$RANDOM_ID@example.com"
CONTENT="This is a random test post #$RANDOM_ID"

echo "== POSTing a new timeline post =="
POST_RESPONSE=$(curl -s --request POST "$BASE_URL" \
  -d "name=$NAME&email=$EMAIL&content=$CONTENT")
echo "$POST_RESPONSE"

# Extract the id from the response using grep + sed (no jq dependency)
POST_ID=$(echo "$POST_RESPONSE" | grep -o '"id":[0-9]*' | grep -o '[0-9]*')
echo "Created post with id: $POST_ID"

echo ""
echo "== GETting all timeline posts to verify it was added =="
GET_RESPONSE=$(curl -s "$BASE_URL")
echo "$GET_RESPONSE"

# Check whether the new post's content appears in the GET response
if echo "$GET_RESPONSE" | grep -q "$CONTENT"; then
    echo "SUCCESS: New post found in GET response."
else
    echo "FAILURE: New post NOT found in GET response."
fi

echo ""
echo "== DELETEing the test post to clean up =="
curl -s --request DELETE "$BASE_URL/$POST_ID"
echo ""
echo "Done."
