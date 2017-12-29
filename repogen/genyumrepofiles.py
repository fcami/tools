#!/usr/bin/python
# -*- coding: UTF-8 -*-

# author: François Cami
# license: MIT

repo_dir='/var/www/html/repos'
yum_conf_dir='/var/www/html/yum/'
yum_conf_templ='/usr/share/repomgmt/yum.repo.tmpl'

from mako.template import Template 
import os,socket

def main():

	mylist = next(os.walk(repo_dir))[1]

	if not os.path.exists(yum_conf_dir):
		os.makedirs(yum_conf_dir)

	for i in mylist:
		mytemplate = Template(filename=yum_conf_templ)
		file = mytemplate.render(name=i,hostname=socket.gethostname())
		f = open("".join([yum_conf_dir,i,".repo"]), "w+")
		f.writelines(file)
		f.flush()
		os.fsync(f.fileno())
		f.close()

	d = os.open(yum_conf_dir, os.O_RDONLY)
	os.fsync(d)
	os.close(d)

if __name__ == "__main__":
    main()
