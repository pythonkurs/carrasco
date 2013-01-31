import os

class CourseRepo(object):
    """Represents the correct structure of a repository for python course.
    The function check() ensures the correctness of this structure.
    """

    def __init__(self, lastname):
        self.required = []
        self._edit_required(lastname)
        self._lastname = lastname

    @property
    def surname(self):
        return self._lastname

    @surname.setter
    def surname(self, lastname):
        self._edit_required(lastname)
        self._lastname = lastname

    def _edit_required(self, lastname):
        self.required = []
        self.required.append('.git')
        self.required.append('setup.py')
        self.required.append('README.md')
        self.required.append('scripts/getting_data.py')
        self.required.append('scripts/check_repo.py')
        self.required.append("{lastname}/__init__.py".format(lastname=lastname))
        self.required.append("{lastname}/session2.py".format(lastname=lastname))
        self.required.append("{lastname}/session3.py".format(lastname=lastname))

    def check(self):
        for f in self.required:
            if not os.path.exists(f):
                return False
        return True


class repo_dir(object):
    """Changes the current working directory to the one specified
    """
    
    def __init__(self, path):
        self.original_dir = os.getcwd()
        self.dir = path

    def __enter__(self):
        os.chdir(self.dir)

    def __exit__(self, type, value, tb):
        os.chdir(self.original_dir)