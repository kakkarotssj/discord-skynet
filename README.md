# [Discord-skynet](https://discord.com/api/oauth2/authorize?client_id=747736525504118874&permissions=2048&scope=bot)
skynet is a bot program, deployed on heroku receiving message from discord server.
Add bot to your discord server by navigating to the link in header and authorizing

# Features
  - Conversation -- enter 'hi'
  - Google search -- enter '!google nodejs'
  - Search History -- enter '!recent nodejs'

### Tech
* [Python](https://www.python.org/download/releases/3.0/) - Powerful, interpreted, high-level, general-purpose programming language
* [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) - Beautiful web scraping framework
* [psycopg2](https://pypi.org/project/psycopg2/) - Most popular PostgreSQL database adapter for python

### DB Setup(Postgres 11.6)
```sh
CREATE USER skynet WITH PASSWORD 'skynet';
CREATE DATABASE skynet WITH OWNER=skynet;
CREATE TABLE search_history (user_id VARCHAR(255), keyword VARCHAR(255), PRIMARY KEY (user_id, keyword));
```