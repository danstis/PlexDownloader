"""
Tests for myplex.py
"""
from mock import mock_open, patch, Mock

import myplex


@patch('myplex.os.path.isfile')
def test_reading_cached_token(mock_isfile):
    """ Test for reading token from token.txt file """
    mock_isfile.return_value = True
    with patch("__builtin__.open", mock_open(read_data="ExampleToken")):
        assert myplex.myplex_signin('aaa', 'aaa') == 'ExampleToken'

@patch('myplex.os.path.isfile')
def test_signin_with_no_username(mock_isfile):
    """ Test for no username being populated in the user.ini. """
    mock_isfile.return_value = False
    assert myplex.myplex_signin('', 'aaa') is None

@patch('myplex.os.path.isfile')
def test_singin_with_no_password(mock_isfile):
    """ Test for no password being populated in the user.ini. """
    mock_isfile.return_value = False
    assert myplex.myplex_signin('aaa', '') is None

@patch('myplex.os.path.isfile')
@patch('myplex.urlopen')
def test_generate_token_with_plexshared(mock_urlopen, mock_isfile):
    """ Test token generation using the credentials in user.ini. """
    mock_isfile.return_value = False
    with patch("__builtin__.open", mock_open(read_data="ExampleToken")):
        resp = Mock()
        resp.read.side_effect = [
            '<user><authentication-token>Dummy-Auth-Token</authentication-token></user>',
            '''<Directory type="movie" accessToken="Dummy-Auth-Token" sourceTitle="test"/>
            <Directory type="movie" accessToken="Dummy-Auth-Token2" sourceTitle="test2"/>''']
        mock_urlopen.return_value = resp
        myplex.MYPLEXSHARED = 'disable'
        assert myplex.myplex_signin('aaa', 'bbb') == 'Dummy-Auth-Token'

@patch('myplex.os.path.isfile')
@patch('myplex.urlopen')
def test_generate_token_without_plexshared(mock_urlopen, mock_isfile):
    """ Test token generation using the credentials in user.ini. """
    mock_isfile.return_value = False
    with patch("__builtin__.open", mock_open(read_data="ExampleToken")):
        resp = Mock()
        resp.read.side_effect = [
            '<user><authentication-token>Dummy-Auth-Token</authentication-token></user>',
            '''<Directory type="movie" accessToken="Dummy-Auth-Token" sourceTitle="test"/>
            <Directory type="movie" accessToken="Dummy-Auth-Token2" sourceTitle="test2"/>''']
        mock_urlopen.return_value = resp
        myplex.MYPLEXSHARED = 'enable'
        assert myplex.myplex_signin('aaa', 'bbb') == 'Dummy-Auth-Token2'
