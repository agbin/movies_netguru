# movies_netguru

POST /movies:
        ​Request body should contain only movie title, and its presence should be validated.
        Based on passed title, other movie details should be fetched from http://www.omdbapi.com/ (or other similar, public movie database) - and saved to application database.
        Request response should include full movie object, along with all data fetched from external API.

GET /movies:

        ​Should fetch list of all movies already present in application database.
        Additional filtering, sorting is fully optional - but some implementation is a bonus.

POST /comments:

        ​Request body should contain ID of movie already present in database, and comment text body.
        Comment should be saved to application database and returned in request response.

GET /comments:

        ​Should fetch list of all comments present in application database.
        Should allow filtering comments by associated movie, by passing its ID.

GET /top:

        ​Should return top movies already present in the database ranking based on a number of comments added to the movie (as in the example) in the specified date range. The response should include the ID of the movie, position in rank and total number of comments (in the specified date range).
        Movies with the same number of comments should have the same position in the ranking.
        Should require specifying a date range for which statistics should be generated.


Application created for recruitment purposes. It was written using Python 3.7 and is compatible with 3.6.



URL: https://agbinmovie.herokuapp.com/


# What to install

    Install Python

    Fork or clone this repository

    git clone

    Install and activate virtualenv:

    virtualenv -p python3 virtenvdjango

    source venv/bin/activate

   Install:
      
    Django==2.2.1
    djangorestframework==3.9.4
    psycopg2==2.8.2
    requests==2.22.0
