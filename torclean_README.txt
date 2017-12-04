torclean.py V 0.1.6 README
==========================
MadTed 2017

- Issue Dez 2017: Logging functionality is not working. Has to be fixed. But the work is done.

"""
    Python program for cleaning up the tor working directory [/var/lib/tor/].
    coming along with a logger including log file-rotation and extra error-log
	
		usage: sudo ./torclean.py torclean_config.ini

"""

On my RasPi2 with Debian stretch I have installed the latest tor server 0.3.2.6-alpha
This is not stable overall. Sometimes the server didn't came up, dies and restart many
times without got the issue fixed. 
The /var/log/syslog or the /var/log/daemon.log tells something about ...
The /var/log/tor/notices.log (log-level notice) tells nothing about the problem, the
tor server simply starts again and again.

So I try to delete the files in the tor working dir. And it helps out! After doing this
the tor server starts normally. Fine!
So here is a python script (python 2.7+) that does the job.
The stats are never deleted.
In the config file the tor working directories are defined. Be sure to set the [WORKDIR]
with an absolute path (for heavens sake)!
Here is an example for the torclean_config.ini default:

# torclean_config.ini for torclean.py;
# Mad666Ted 2017
[TOR-workdir]
WORKDIR = /var/lib/tor/		# where tor is installed, including slash / at the end!
DIR1 = diff-cache/			# the first sub-directory
DIR2 = keys/				# the second sub-dir
