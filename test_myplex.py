"""
Tests for myplex.py
"""
import os

from mock import MagicMock

import myplex

def test_no_username():
    """ Test for no username being populated in the user.ini. """
    os.path.isfile = MagicMock(return_value=False)
    assert myplex.myplex_signin('', 'aaa') is None

def test_no_password():
    """ Test for no password being populated in the user.ini. """
    os.path.isfile = MagicMock(return_value=False)
    assert myplex.myplex_signin('aaa', '') is None

def test_generate_token():
    """ Test token generation using the credentials in user.ini. """
    if myplex.MYPLEXSTATUS == 'enable':
        os.path.isfile = MagicMock(return_value=False)
        assert myplex.myplex_signin(myplex.MYPLEXUSERNAME, myplex.MYPLEXPASSWORD) != ''
