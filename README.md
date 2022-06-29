# kesho-telegram-bot 
## Music Player on the Remote Host

This is a python based Telegram Bot program (meant to run in the background) which is intended to run on a Remote Host machine connected to a music speaker system. This bot plays the requested title of the song from youtube (audio only).

Operation: 
1. User sends a string query (usually a song name, but it can be anything tbh!) to the Telegram Bot.
2. The user query is searched on Youtube platform and list of results (a.k.a. Youtube recommendations for the query) is obtained. 
3. The bot then selects the first youtube recommendation for the queried title.
4. The audio stream of that video is extracted and played on the host computer.
