# Baseball-Standings-App-using-MongoDB
Rows in teams.dat contain team name, team location, and team code, whereas rows in games.dat contain game date, visiting team code, home team code, visiting team score, and home team score.

Two Python programs (loadTeams.py and loadGames.py) load teams and games details into a MongoDB database. The files are accepted as command line parameter (sys.argv[1]). Two collections (named teams and games) are created within a database named baseballDB in mongoDB. The following two constraints are satisfied while inserting documents into mongodb collections:

1. The team code serves as a primary key for the teams collection. So,no duplicate team codes are inserted into the teams collection.
2. Since the team code is used in the the games data,  while inserting into the games collection that both the teams involved are present in the teams collection.

baseball.py is a REST API program that implements the following two 'GET' endpoints. baseball.html is the front end and baseball.js has the corresponding ajax calls in jquery.
