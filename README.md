# BIliBIli-video-tracer

Run [ pip install bs4 requests ] in terminal for module dependency

Overview: This short script help you gather six types of statistics about a video posted on BiliBili, specifically the numbers of views, bullet comments, likes, coins, collects, and shares. Please look at the scripts before running them for more instructions.

Auto version: You can use it for either tracing a video in crontab or running at the backend of you computer, and all information will be stored in an additional data.txt file in the same folder of the script.

Manual version: The script only pulls the video information once, but it includes a simple interface and some extra info as well. Nothing is going to be stored, so it's just for test before you use the auto version.

Trend: A very simple script to see the amount of increase per unit time, and store the trend data in trend.txt.

Note: The minimum time between two runs of the script is 75s as BiliBili refrash the data in this frequency. 
