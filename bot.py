from instapy import InstaPy

session = InstaPy(username='', password='',want_check_browser=False)
session.login()
session.set_do_like(enabled=False, percentage=70) # 70 % постів буде лайкнуто в лєнті
session.set_do_follow(enabled=False, percentage=25, times=1) # Зробить фолов 25% аккаунтів яких побачить
# session.set_comments(comments=['Найс відео'], media='Video') Коментар для відео
# session.set_comments(comments=['Nice shot!'], media='Photo') Коментар для фото

# Follow user based on hashtags (without liking the image)
session.follow_by_tags(['bratislava', 'tag2'], amount=10)

# Встановлення тегів по яким буде лайкнуто фото
session.set_smart_hashtags(['bratislava', 'slovensko', ''], limit=3, sort='top', log_tags=True)
session.like_by_tags(amount=10, use_smart_hashtags=True)

# По локації буде лайкати(example :204517928/chicago-illinois)
session.set_smart_location_hashtags(['213682323/bratislava-slovakia/', ''], radius=15, limit=5)
session.like_by_tags(amount=10, use_smart_location_hashtags=True)


# include media entities from top posts section
session.like_by_locations(['213682323'], amount=2, skip_top_posts=False)

# Менеджер сесії щоб не перевищувати ліміти і не видати бота
session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=19,
                              peak_likes_daily=311,
                               peak_comments_hourly=0,
                               peak_comments_daily=0,
                                peak_follows_hourly=16,
                                peak_follows_daily=None,
                                 peak_unfollows_hourly=0,
                                 peak_unfollows_daily=0,
                                  peak_server_calls_hourly=None,
                                  peak_server_calls_daily=4215)

#Пропуск приватних акк
"""session.set_skip_users(skip_private=True,
                       private_percentage=100,
                       skip_no_profile_pic=False,
                       no_profile_pic_percentage=100,
                       skip_business=False,
                       skip_non_business=False,
                       business_percentage=100,
                       skip_business_categories=[],
                       dont_skip_business_categories=[],
                       skip_bio_keyword=[],
                       mandatory_bio_keywords=[])"""

# Кастомна зупинка бота
"""session.set_action_delays(enabled=True,
                           like=3,
                           comment=5,
                           follow=4.17,
                           unfollow=28,
                           story=10)"""

session.end(threaded_session=True)