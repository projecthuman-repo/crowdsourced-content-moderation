# crowdsourced-content-moderation

This is a codebase for Crowdsourced Content Moderation/Review. 

Crowdsourcing can be done via Amazon Mechanical Turks or opensource Mturks such as PYBossa. 
It can be a great way for microvolunteering. 

Why Content Moderation is important

Moderating the content on social media websites is important, as now such platforms are used to promote the business, products and brands and such spam contents can disappoint other customers and discourage them to either stay away from such platforms or minimize the use of social media sites.

Functionality:

In this project we create tasks.csv which will have tasks that volunteers have to finish. You only need to tell the script where is the PDF file hosted, the URL, and which pages you want to convert as tasks.

You need to install the pybossa-pbs library first. Use of a virtual environment is recommended:

    $ virtualenv env
    $ source env/bin/activate

    $ pip install -r pybossa-pbs

Creating an account in a PyBossa server
    Create an account in your PyBossa server
    Copy your API-KEY (you can find it in your profile page).

Configure pybossa-pbs command line

        $ cd ~
    $ editorofyourchoice .pybossa.cfg

Create the Project

        $ pbs create_project

Adding tasks

Using a CSV or JSON file for adding tasks
This is very simple too. There's a sample tasks CSV file included here named 'tasks.csv'.

        $ pbs add_tasks --tasks-file tasks.csv

Finally, add the task presenter, tutorial and long description

        $ pbs update_project
