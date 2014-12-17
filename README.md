bestbooks
=========

The main idea of this website was to search for external ratings data, aggregate it into an actually shrinkage estimated set of ratings (I used a Bayesian method a la imdb's top 250) movies, and then push it onto a table for viewers to see.  

Problems I ran into were the fact that in order to search goodreads to get the ratings, I needed a set of isbn numbers, instead of titles. So to convert from title to isbn, I used isbndb. However, isbndb a) doesn't have a one-to-one mapping of names to isbn (e.g., due to multiple editions and the ilk) and b) more importantly, doesn't seem to like many simultaneous queries using the API. I asked them about this but they weren't able to help me much, though of course it is a non-profit so that is totally understandable. 

I hope the python code for searching isbndb and/or goodreads will be helpful to somebody.
