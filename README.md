Hello everyone,

Let's setup our environment. We are using Github as the version control system. 
To get everything setup, make sure you have git installed and if you want to access
via SSH, give me your public keys and have your private keys in your .ssh file. 
Use an ssh agent to not be prompted any passcodes (https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

Using SSH agent (should come with linux). I'm not venturing into Windows or Mac.

After creating your new ssh key in the .ssh file, run commands

    eval "$(ssh-agent -s)"     /* This starts the ssh-agent in the background */
    ssh-add ~/.ssh/[name of private key]

Now give me your public key to give you access.

Now, authenticate your connection doing

    ssh -T git@github.com

You should see the response 

> Hi USERNAME! You've successfully authenticated, but GitHub does not
> provide shell access.

If you don't here is a link... https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection



Go to the directory where you want to keep this repository

    git clone [copied SSH link]

Basic uses of Git that I have only recently learned...

    $ git remote -v
    # Verify new remote
    > origin  https://github.com/OWNER/REPOSITORY.git (fetch)
    > origin  https://github.com/OWNER/REPOSITORY.git (push)


    $ git remote show origin
    * remote origin
      Fetch URL: git@github.com:dollarbar/airsoft_club
      Push  URL: git@github.com:dollarbar/airsoft_club
      HEAD branch: main
      Remote branch:
        main tracked
      Local branch configured for 'git pull':
        main merges with remote main
      Local ref configured for 'git push':
        main pushes to main (up to date)
    
      $ git status      /* should be on main branch */
      $ git log         /* shows commits */

Make sure your .git/config file in the root folder has url = git@github.com:dollarbar/airsoft_club
note: I had trouble with sources that told me to put git.github rather than git@gihub. 
Make sure it's a colon after github.com and not a slash

-------------------------------
Before coding, I am using venv as a virtual environment great with Python
https://docs.python.org/3/library/venv.html

Make a separate directory OUTSIDE of the root directory of this project. 
I call mine venvs because you can setup various virtual environments for different projects with different dependencies.
Within venvs create another directory - I called mine airsoft - and install venvs (do this with every other project)

     python -m venv /path/to/new/virtual/environment

Activate the virtual environment.

    $ source <venvs/airsoft>/bin/activate

Result should look like

    (airsoft) user@machine: ~$ 
    
Venvs will give you pip and a Python version to start with.

Now install Django. 

    (airsoft) ... $ python -m pip install Django

--------------------------------
To begin coding, go to root directory of the project. Command $ git status to make sure your contributions are version controlled and...

    $ git pull        /* fetches and merges the remote repository. May not be necessary right after cloning */
    $ git add .       /* adds all edits to be commited */
    $ git commit -m "your message"        /* commits */
    $ git push        /* pushes to remote location */


Feel free to update this with commentary, sources, dependencies, and directions for collaboration and 

--------------------------------------------

To make sure the project is running, 

    python manage.py runserver    /* This is a Django executable */

Open http://127.0.0.1:8000 in your browser. You should see some Django page.


----------------------------------------------------------

Developer Login Functionality

The first thing anyone going to this site will see is the login page.
The user will have a choice between registering, viewing the calendar, or logging in to edit the calendar. This is all done under the "authz" app in the root folder.

In the authz app, you will see the functional logic of logging in inside the 'views' file. There will be all the rendering of the login page, register page, and test pages to test the required login functionality. The views page incorporates many Django apis such as password validation and the built-in credential manager. If you wish to make a custom credential manager, you will have to create on yourself in models and forms pages and remove the library imports staring with django.contrib.auth.

All the html files will be located in templates and they load static css files from the static folder. This is the common approach to any app created in Django including the events app that manages events.

Redirecting urls upon button clicks can be done in the html, but if it is responding to a request, you will find the redirections done in the views page. The relative urls must be included in either the app's url file or the root url file. You can do both, which is exhibited in the authz app. 

The simple @login_required tag makes prohibits rendering a view if there is no user logged in recognized by Django's credential manager. Therefore, one must be logged in to view the editing page of the calendar. If not logged in, a user can still go into the calendar page without editing permissions.



This portion of the README provides instructions and an overview of the Airsoft Calendar web page (The Calendar Portion). The page uses FullCalendar (a JavaScript library) to display and interact with calendar events, including a modal popup to show event details.

This HTML page implements an interactive calendar for managing and viewing Airsoft events. Key features include:

Dynamic event loading from a Django backend.
Event details displayed in a modal popup when clicked.
Navigation options for switching between dates and views.
Customizable styles and event tooltips.

Key Technologies: 

HTML: Base structure of the page.
CSS: Custom and FullCalendar styles.
JavaScript/jQuery: Handles calendar rendering, modal interactions, and event loading.
FullCalendar: A JavaScript library for calendar functionality.
Moment.js: For date and time formatting.
Django: Backend framework providing event data via a JSON API.

Prerequisites:
-A Django project with an endpoint (/calendar/events/) that returns event data in JSON format.
-Internet connection for external library dependencies (e.g., FullCalendar, jQuery).

Event Data Format:
The /calendar/events/ endpoint should return data in the following format:

Title: (Name of the event)
Start: (Time the event starts)
End: (This is coded to expect 6 hour games)
Description: (Details about the event) 

How to run:
Add to Django Template: Place this HTML file in your Django project’s templates/ directory and reference it in your view.
return render(request, 'airsoft_calendar.html')

Include the Static Files: Ensure the calendar.css file is in the static directory and is referenced correctly in the <head> section:
<link rel="stylesheet" href="{% static 'calendar.css' %}">

Start Django Server: Run the Django server:

python manage.py runserver


Key Features
1. Event Display
Events are dynamically fetched from the /calendar/events/ endpoint.
Each event displays a title on the calendar grid.
2. Modal Popups
Clicking an event opens a modal showing detailed event information (e.g., title, description, start/end times).
The modal includes a close button and dismisses when clicking outside it.
3. Tooltip Customization
Hovering over events shows a tooltip with the event title.
4. Calendar Header
Navigation buttons (prev, next, today) and a centered title display the current month.
5. Editable Events
Events are draggable and editable.
Customization
Styles: Modify calendar.css or add custom styles in the <style> block.
Event Rendering: Customize how events are displayed using the eventRender function.
Modal: Adjust the modal structure and content within the <div id="eventModal"> block.


Customization Options to know: 
Styles: Modify calendar.css or add custom styles in the <style> block.
Event Rendering: Customize how events are displayed using the eventRender function.
Modal: Adjust the modal structure and content within the <div id="eventModal"> block.

Dependencies:
FullCalendar v3.2.0: Calendar library.
jQuery v3.6.0: Required for DOM manipulation.
Moment.js v2.29.1: Date and time manipulation.




  



