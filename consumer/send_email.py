#!/usr/bin/env python
#

import smtplib
import os


def sendEmail(body):
	server = smtplib.SMTP(os.environ['SMTP_SERVER'], 587)

	server.starttls()
	#Next, log in to the server
	server.login(os.environ['USER'], os.environ['PWD'])

	server.sendmail(os.environ['FROM'], os.environ['TO'], body)