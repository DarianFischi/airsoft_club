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

The project contains a login and a calendar. Create an account and look up upcoming events on the calendar.
Admins can add and remove calendar events. You can look at the details of an event when clicked on.



  



