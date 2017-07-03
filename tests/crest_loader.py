#
#   crest_loader.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import os
import sys
from os.path import abspath, dirname, pardir

test_dir = dirname(abspath(__file__))
git_dir = abspath(os.path.join(test_dir, pardir))
if (git_dir not in sys.path):
    sys.path.append(git_dir)
