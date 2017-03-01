""" Contains functions used for interacting with MyPlex"""
import base64
import os
import platform
import re
import socket
import urllib
import uuid
from ConfigParser import SafeConfigParser
from urllib2 import Request, quote, urlopen

from logger import logger

PARSER = SafeConfigParser()
PARSER.read('user.ini')

MYPLEXSTATUS = PARSER.get('myplex', 'status')
MYPLEXUSERNAME = PARSER.get('myplex', 'username')
MYPLEXPASSWORD = PARSER.get('myplex', 'password')
MYPLEXSHARED = PARSER.get('myplex', 'shared')


def myplex_signin(username, password):
    """Attempts to signin to MyPlex and retrieve a token"""
    try:
        if os.path.isfile('token.txt'):
            with open('token.txt', 'r') as tokenfile:
                authtoken = tokenfile.readline()
            logger.info("Using cached myPlex token.")
            return authtoken
        elif username != '' and password != '':
            logger.info("Fetching myPlex authentication token.")
            headers = {}
            headers["Authorization"] = "Basic %s" % base64.encodestring(
                '%s:%s' % (username, password)).replace('\n', '')
            headers["X-Plex-Client-Identifier"] = quote(
                base64.encodestring(str(uuid.getnode())).replace('\n', ''))
            headers["X-Plex-Product"] = "Plex-Downloader"
            headers["X-Plex-Device"] = "Plex-Downloader"
            headers["X-Plex-Device-Name"] = socket.gethostname()
            headers["X-Plex-Platform"] = platform.system()
            headers["X-Plex-Client-Platform"] = platform.system()
            headers["X-Plex-Platform-Version"] = platform.version()
            headers["X-Plex-Provides"] = "controller"
            request = Request("https://plex.tv/users/sign_in.xml",
                              data="", headers=headers)
            request = urlopen(request)
            compiled = re.compile(
                r"<authentication-token>(.*)</authentication-token>", re.DOTALL)
            authtoken = compiled.search(request.read()).group(1).strip()
            if authtoken != None:
                tokenfile = open('token.txt', 'w+')
                tokenfile.write(authtoken)
                tokenfile.close()
                if MYPLEXSHARED == "enable":
                    link = "https://plex.tv/pms/system/library/sections?X-Plex-Token=" + authtoken
                    tokenfile = urllib.urlopen(link)
                    serverlist = tokenfile.read()
                    tokens = re.findall(r"accessToken=\"(.*?)\"", serverlist)
                    tokens = list(set(tokens))
                    tokens.remove(authtoken)
                    authtoken = tokens[0]
                    tokenfile = open('token.txt', 'w+')
                    tokenfile.write(authtoken)
                    tokenfile.close()
                    logger.info("Successfully grabbed shared myPlex Tokens!")
                    return authtoken
                else:
                    logger.info("Successfully authenticated with myPlex!")
                    return authtoken
            else:
                logger.error("Failed to login to myPlex!")
                return authtoken
        else:
            authtoken = ""

    except Exception, e:
        logger.error("Failed to login to myPlex: %s" % str(e))
