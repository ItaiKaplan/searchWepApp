# searchWepApp

**This is a very basic implementation of a search app, that connects to a given Confluence space, and searches its pages for a search input from the user.**

**Usage** <br />
Clone the repo <br />
Run the command pip install -r requirements.txt (preferably in a virtual environment) <br />
Install Redis (If you are using a Windows machine you will need to install and run it on a virtual machine. You can see [this](https://www.youtube.com/watch?v=_nFwPTHOMIY&t=539s) video to see how) <br />
Run app.py

**About the process:**

**App:** I created my app using the Python Flask web framework, I did so mainly because Flask is easy to use, and since time was an issue, I wanted to be able to build my app fast, while still having solid foundation. <br />
**DB:** My second decision was what type of database to use. I started building an SQL-based DAL, but realizing I only have one column in my table, and that I do need to keep a counter of all rows in it, I figured Redis is a much better choice in my case since I only need to store and retrieve simple search queries and count the number of searches.

With both those decisions being done. completing the first part was just a matter of implementing some simple code. You can see it on my ‘Part 1’ commit (sorry if it is a bit messy, remember it's still in progress).

When I started the sconed part, I decided I want to connect to Confluence and read from the given space (instead of reading locally from the doc files). This was actually the most challenging part of the task since most of the documentation I found was a bit vague and I had some connections and authorizations issues. I finally found the ‘atlassian-python-api’ library, which provides a set of tools and functions for interacting with various Atlassian products, including Confluence. After using it, connections were made and I could continue to the search part.

**Search Algorithm:** I implemented a very basic search algorithm, it does nothing too special but go through all pages and try to find a match with the input it was given. The only improvement I made was to use the Fuzzybuzzy library, which allows ‘fuzzy’ matching, which gives some space for errors from the user, so, for example, if the user enters ‘TGI’, instead of ‘TGI Friday's’, he would still know it's on the ‘Restaurants’ page. If I would have some more time I would use the strategy pattern to enable the client to choose which search algorithm he wants to use. 

**FrontEnd:** The frontend of the application is simple, using basic Bootstrap components. If I had more time, I would have made it prettier and less HTML-like by improving the alignments and overall design.

**What I would add:**

 **Dependency Injection** - I would add a dependency injection structure that would allow the client to inject Readers (for reading from other places other than Confluence alone) and Databases (so it could use different types of DBs) this can allow flexibility and can help create a mock object which will allow us to unit test the code. I started building the foundation for it, but it is still not done. <br />
**Error handling** - at the moment, the does not handle errors correctly, If an error occurs (e.g. the ConfluenceReader cannot connect to the Confluence server), the app will crash. Adding error handling to handle these situations would provide a better user experience. 

