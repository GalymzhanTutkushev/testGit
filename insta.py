from instapy import InstaPy

session = InstaPy(username="robotics_boraldai", password="rinEngan18")
session.login()
session.follow_user_following(['crystal.trc'], amount=10, randomize=False)
# session.like_by_tags(["bmw", "mercedes"], amount=5)
# session.set_dont_like(["naked", "nsfw"])
# session.set_do_follow(True, percentage=50) # подписка
# session.set_do_comment(True, percentage=50)
# session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"]) # комменты
# session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21) #предел
session.end()