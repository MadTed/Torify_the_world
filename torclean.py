#!/usr/bin/python

####################
# --------------------------------------------------------------------------------
# for future compatibility for Python 3.2+
from __future__ import print_function
from __future__ import division
# --------------------------------------------------------------------------------
"""
    Python program for cleaning up the tor working directory [/var/lib/tor/].
    coming along with a logger including log file-rotation and extra error-log
		todo: using a config-file
	
		usage: sudo ./torclean.py torclean_config.ini

"""
# doc
# --------------------------------------------------------------------------------
# additional information about the file
## __todo__ adding the hq-version- and revision number
__author__ = "Mad Ted"
__copyright__ = "torclean.py Copyright 2017, The MadTed Project"
__credits__ = ["TedMcMad", "Ted Varg"]
__license__ = "GPL"
version= "0.1"
__version__ = version
revision= "6"
__revision__ = revision
__maintainer__ = "Mad Ted"
__email__ = "mad666ted@gmail.com"
__status__ = "Development"
# --------------------------------------------------------------------------------
import sys, os
import logging, logging.handlers
import configparser

script_name = os.path.basename( __file__ )
# --------------------------------------------------------------------------------
# implementing a logger. the goal is to log in two files, one for all and one only for errors,
# and last a stream to stdout.
# teds std-logger
# get logger and defining additional FATAL status = 60
logging.FATAL = 60
logging.addLevelName(logging.FATAL, 'FATAL')
log = logging.getLogger( __name__ )
log.fatal = lambda msg, *args: log._log(logging.FATAL, msg, args)
logformat = "[%(asctime)s] %(process)d [%(module)s] %(lineno)d [%(levelname)s]: %(message)s"
logformat_stream = "%(process)d [%(module)s] %(lineno)d [%(levelname)s]: %(message)s"
# basic logger, not used
logging.basicConfig(level= 10) # DEBUG
# get rid of the stdout logging from basic logger
logging.StreamHandler(stream=None)
# create basic file handler
fhbasic = logging.handlers.RotatingFileHandler(
			  "%s.log" % ( script_name ), maxBytes=1*1024*1024, backupCount=5)
# define the log-level
fhbasic.setLevel(logging.DEBUG)
# create file handler which logs only error messages and above
fherror = logging.handlers.RotatingFileHandler(
			  "%s_error.log" % ( script_name ), maxBytes=1*1024*1024, backupCount=5)
fherror.setLevel(logging.ERROR)
# create stream handler which logs only error messages to stdout
fhstream = logging.StreamHandler()
fhstream.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter(logformat)
fhbasic.setFormatter(formatter)
fherror.setFormatter(formatter)
formatter = logging.Formatter(logformat_stream)
fhstream.setFormatter(formatter)
log.addHandler(fhbasic)
log.addHandler(fherror)
log.addHandler(fhstream)
# --------------------------------------------------------------------------------	
# starting main
log.info("# --------------------------------------------------------------------------------")
log.info("STARTing program [%s] Version %s Rev. %s", script_name, version, revision)
# --------------------------------------------------------------------------------
# ###################
# # log tests
# a, b, c, d, e, f, g= 1,2,3,4,5,6
# for i in range(50):
   # log.debug("this is my %s DEBUG message ... [%s]", a, i)
   # log.info("this is my %s INFO message ... [%s]", b, i)
   # log.warn("this is my %s WARN message ... [%s]", c, i)
   # log.error("this is my %s ERROR message ... [%s]", d, i)
   # log.critical("this is my %s CRITICAL message ... [%s]", e, i)
   # log.fatal("this is my %s FATAL message ... [%s]", f, i)
# ###################

# exception handling
try:
        # loading config.ini
        config = configparser.ConfigParser()
        config.read(ARGV[0])
        path = config['TOR-workdir']['WORKDIR']
	path1 = config['TOR-workdir']['DIR1']
	path2 = config['TOR-workdir']['DIR2']
        
	# exists the standard tor directory?
	if os.path.exists( path ):
		log.info("standard tor working dir [%s]exists, good thing ...", path)
		# changing to tor working dir
		os.chdir( path )
		# removing working files
		# cached-certs cached-consensus cached-descriptors cached-descriptors.new cached-microdesc-consensus 
		# cached-microdescs fingerprint hashed-fingerprint state cached-microdescs.new
		file_names = [ 'cached-certs', 'cached-consensus', 'cached-descriptors', 'cached-descriptors.new', 'cached-microdesc-consensus',
						'cached-microdescs', 'fingerprint', 'hashed-fingerprint', 'state', 'cached-microdescs.new' ]
		for file in file_names:
			if os.path.exists(path + file):
				os.remove(path + file)
				log.info("deleted file [%s%s]", path, file)
				
			else:
				next
		
	else:
		log.error("the standard tor working dir [%s] doesn't exists!", path)
		
	path_next = path + path1
	if os.path.exists( path_next ):
		os.chdir( path_next )
		log.info("tor working dir [%s] exists", path_next)
		# reading only the filenames [2] from path
		for file in next(os.walk(path_next))[2]:
			os.remove(path_next + file)
			log.info("deleted file [%s%s]", path_next, file)
			
	else:
		log.warn("tor working dir [%s] does NOT exist!", path_next)
		
	path_next = path + path2
	if os.path.exists( path_next ):
		os.chdir( path_next )
		log.info("tor working dir [%s] exists", path_next)
		# reading only the filenames [2] from path
		for file in next(os.walk(path_next))[2]:
			os.remove(path_next + file)
			log.info("deleted file [%s%s]", path_next, file)
			
	else:
		log.warn("tor working dir [%s] does NOT exist!", path_next)

	log.info("done.")

# --------------------------------------------------------------------------------
# exception handling
except Exception as e:
    log.exception('Failed: ' + str(e))

finally:
        # end of program = end of logging
        log.info("# --------------------------------------------------------------------------------")
        log.info("ENDing programm")
        log.info("# --------------------------------------------------------------------------------")
        logging.shutdown()
        # exiting
        sys.exit

# --------------------------------------------------------------------------------
