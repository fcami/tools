#!/usr/bin/python

# Copyright (c) 2017 François Cami

# demonstrate how to launch a gnome-terminal monitored by gdbus
# best launched in dbus-run-session:
# $ dbus-run-session -- gt.py

import subprocess

from threading import Thread
import re

cmd1=['gdbus', 'monitor', '--session', '-d', 'org.gnome.Terminal']
cmd2=['gnome-terminal']


def launch(cmd):
  p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
  while True:
      output = p.stdout.readline()
      if output == '' and p.poll() is not None:
          break
      if output:
          matches = re.findall('The name org.gnome.Terminal does not have an owner', output, re.DOTALL)
          if len(matches) > 0:
		p.kill()
  rc = p.poll()



t1 = Thread(target=launch, args=(cmd1,))
t2 = Thread(target=launch, args=(cmd2,))

t1.start()
t2.start()

