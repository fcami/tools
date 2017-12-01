#!/bin/sh

# Copyright (c) 2017 Red Hat, Inc.

exec dbus-run-session bash -c 'gnome-terminal >& /dev/null; gdbus monitor --session -d org.gnome.Terminal 2>&1 | while read line; do echo $line | grep -q "does not have an owner" && kill $$; done'


