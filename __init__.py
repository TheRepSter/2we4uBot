from TwoWE4uBot.reply import reply, edit
from time import sleep
import praw

class Bot:
    def __init__(self, **kwargs) -> None:
        self.reddit = praw.Reddit(**kwargs)


    def _botAlreadyCommented(self, object):
        """
        Checks if the bot already commented on the object
        if true returns the object
        """
        comment = "t1_" in object.fullname
        replies = [reply for reply in object.replies] if comment else [reply for reply in object.comments]
        try:
            val = list(map(lambda reply: reply.author, replies)).index("2WE4uBot")
            return replies[val]
        except ValueError:
            return False


    def _comproveNotFlairedReports(self) -> None:
        for reportedItem in self.reddit.subreddit("2westerneurope4u").mod.reports():
            for report in (reportedItem.user_reports + reportedItem.mod_reports):
                if report[0] == "User Flairs are required.":
                    break

            else: # if in the reports isn't the "User Flairs are required" then the bot will continue to other post/comment.
                continue

            if reportedItem.author_flair_template_id is None: # if user is unflaired then .author_flair_template_id is None.
                if botComment := (self._botAlreadyCommented(reportedItem)):
                    edit(botComment, "flairUp")
                    reportedItem.mod.remove()
                else:
                    reply(reportedItem, "flairUp")
                    reportedItem.mod.remove()


    def _comproveLastPostsNotFlaired(self) -> None:
        for post in self.reddit.subreddit("2westerneurope4u").new(limit=100):
            if post.author_flair_template_id is None and post.banned_by is None: # if user is unflaired then .author_flair_template_id is None.
                if botComment := (self._botAlreadyCommented(post)):
                    edit(botComment, "flairUp")
                    post.mod.remove()
                else:
                    reply(post, "flairUp")
                    post.mod.remove()


    def _comproveLastCommentsNotFlaired(self) -> None:
        for comment in self.reddit.subreddit("2westerneurope4u").comments(limit=500):
            if comment.author_flair_template_id is None and comment.banned_by is None: # if user is unflaired then .author_flair_template_id is None.
                if botComment := (self._botAlreadyCommented(comment)):
                    edit(botComment, "flairUp")
                    comment.mod.remove()
                else:
                    reply(comment, "flairUp")
                    comment.mod.remove()


    def _comproveNewFlair(self) -> None:
        for botComment in self.reddit.redditor("2WE4uBot").comments.new(limit=500): 
            parentObject = botComment.parent()
            if parentObject.author_flair_template_id is None: # if user is unflaired then .author_flair_template_id is None.
                if "Finally" in botComment.body:
                    # if the bot commented, I don't need to call .__botAlreadyCommented because I already had the comment.
                    edit(botComment, "flairUp")

            elif "Finally" not in botComment.body: # The user is flaired!
                parentObject.mod.approve()
                edit(botComment, parentObject.author_flair_template_id) # edit the comment with the "Oh... So you're a...".


    def run(self) -> None:
        while True:
            self._comproveLastCommentsNotFlaired()
            self._comproveLastPostsNotFlaired()
            self._comproveNotFlairedReports()
            self._comproveNewFlair()
            sleep(60)