#Python Course repository

Guillermo Carrasco repository for the python course

## First assignment (session 1)
Create a repository for the course with the following structure:

    lastname/
        |__ setup.py
        |__ README.md
        |__ lastname/
                |__ __init__.py

Then, create a repository in the pythonkurs organization in GitHub. Name it as 
your lastname and push there the created structure.

## Second assignment (sesison 2)
Make a module and script which fetches the XML formatted for the status of escalators
in the NYC subway system at [this](http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml) URL.

Calculate the fraction of those outages which have the reason "Repair", and prints this fraction.
Information about the data can be found [here](http://www.grandcentral.org/developers/download.html).

The module and the script should be based on the repository we made for Session 1, which should have this structure:

    lastname/
        |__ setup.py
        |__ README.md
        |__ lastname/
        |       |__ __init__.py
        |__ scripts/
                |__ getting_data.py

Along with some other files.

The script should use the module, meaning all code that actually gets the data, 
and calculates things with it, should be located in the [lastname]/__init__.py file,
while the script is what should actually be called to run the functions from the module.
This means in the script there should be a line like:

    from lastname import some_function

Where some_function will be used in the script. This should be installable by 

    python setup.py install

This means that in setup.py, you need to add the scripts to the call of the setup function.
For details, refer to [here](http://peak.telecommunity.com/DevCenter/setuptools#basic-use).

##Third assignment (session 3)
* Make a new file in your module called session2.py, and move the code from __init__.py in to it.
* Change your getting_data.py to import in this fashion: from lastname.session2 import ...
* Make a context manager which changes the current directory for the python script using it, and changes back to where you came from upon exit.

Implement a class CourseRepo which takes a "surname" string in the constructor.

The class should have an attribute "required" which is a list of these strings:

* ".git"
* "setup.py"
* "README.md"
* "scripts/getting_data.py"
* "scripts/check_repo.py"
* "lastname/__init__.py"
* "lastname/session3.py"

Where "lastname" is the "surname" string you gave to the constructor. Surname should be a 
property, such that when it is set, the required attribute changes to reflect the new surname.

Example:

    repo = CourseRepo("a")
    print(repo.required[-1])
    # prints a/session3.py

    repo.surname = "b"
    print(repo.required[-1])
    # prints b/session3.py

The class should have a method check() which shall return True if all the strings
in that list are existing files or directories.

The context manager and class should be implemented in a file session3.py in your lastname module.
Then make a script, scripts/check_repo.py, which imports the context manager for 
changing current directory as well as the CourseRepo class from the module. Like this:

    from lastname.session3 import CourseRepo, repo_dir

This script should take an argument which is the absolute path to a repository.

The script should change directory to this given directory using the context manager.
It should make an instance of CourseRepo using the final part of the absolute path,
and call the check() method. If check() returns True the script shall print "PASS",
otherwise the script should print "FAIL".
Example: If I call the script like

    $ check_repo.py /Home/user/a

it should make a CourseRepo instance like in the example above (with "a").

Like the other script, this script should also be installed when running python setup.py install.

__Note: If your repo has a structure this script is not expecting, fixing it should be rather smooth using git mv for renaming/moving files and directories.__