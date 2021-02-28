# Job-Scrapper
Just a small Web-Scrapper that plays with bs4 and html.

Changes: 26/02/21 19:18hs

///Deleted Job-ViewerObs.html
Obsolete

///modified: PageF/JSON.txt
This file is a placeholder of "Job-Scrapper.py"'s results. Once i integrate the
code right in Flask it will be deleted.

///added: PageF/templates/placeholder.html
This text was first inside "Job-Viewer.html", was moved to be inside an iframe.

///modified: PageF/routes.py 
Added "placeholder.html" to routes.

///modified: PageF/templates/Job-Viewer.html.
Made several changes that make the page more functional, now being fully able to open links inside JSON. Sidebar hasbeen improved
Sidebars now are almost fully responsive, just need to add max-height to sublists. 
Now every link makes an iframe.
Things to take care:
-Fix Sidebar Scroll of items adding max-height, add style and design.
-Add a link as an alternative to the i frame. 

Changes: 27/02/21 20:55hs

///modified PageF/static/style.css 
Finished adding all the option so page doesnt look horrendous.

///modified PageF/templates/Job-Viewer.html 
-Made lists functional.
-Added alternative so links can be opened on browser
-Changed functionality of opening and closing tabs. Now opening a tab closes all the others. 

