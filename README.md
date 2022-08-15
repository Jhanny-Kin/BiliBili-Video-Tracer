# BIliBIli-video-tracer

pip install bs4, requests

The tracer will get the numbers of comments, bullet screen, views, likes, coins, and shares of a video. Because this is a Chinese based website, it is inevitable to involve a few Chinese terms in the scripts.

There are going to be two versions for different senarios. Auto version is meant to run on a server, so that you can trace the video for a long time. It relies on crontab for an accurate timing. The data it obtains will be stored in files which can be used for data analysis or machine learning. The manual version only pulls information once, meaning that nothing is going to be stored. However, it provides you with some extra information with a simple interface, although they are generally useless. 

The demo version is only for me to test features and for you to see what's in it.
I will release the official versions ASAP.
