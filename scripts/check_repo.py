#!/usr/bin/env python

import os
import argparse
from carrasco.session3 import CourseRepo, repo_dir

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Takes as argument an absolute' +
                                     ' path to a repository and check the correctness' +
                                     ' of its file structure')
    #Positional arguments (mandatory)
    parser.add_argument('repo', help="Absolute path to the course repository")
    args = parser.parse_args()

    with repo_dir(args.repo):
        repo = CourseRepo(os.path.split(args.repo)[1])
        if not repo.check():
            print 'FAIL'
        else:
            print 'PASS'