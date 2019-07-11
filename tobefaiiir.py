import praw

QUESTIONS = ["to be fair"]
REPLY_TEMPLATE = "[to be faiiir](https://www.youtube.com/watch?v=cgprAH98lsA{})"


def main():
    reddit = praw.Reddit(
        user_agent="tobefairbot1 (by /u/tobefairbot1)",
        client_id="oZfJ2AJnjPiVcQ",
        client_secret="hQy0knntK5IwQVW1RWuZ_yfEwM8",
        username="tobefairbot1",
        password="xboxgame1238358",
    )

    subreddit = reddit.subreddit("all")
    for submission in subreddit.stream.submissions():
        process_submission(submission)


def process_submission(submission):
    # Ignore titles with more than 10 words as they probably are not simple
    # questions.
    if len(submission.title.split()) > 10:
        return

    normalized_title = submission.title.lower()
    for question_phrase in QUESTIONS:
        if question_phrase in normalized_title:
            url_title = quote_plus(submission.title)
            reply_text = REPLY_TEMPLATE.format(url_title)
            print("Replying to: {}".format(submission.title))
            submission.reply(reply_text)
            # A reply has been made so do not attempt to match other phrases.
            break