#! /bin/sh
cd /Users/twitchplaysrobotics/tpr_site/ && echo 'path set'
python site.py && echo 'main page updated'
python faqs.py && echo 'FAQ page updated'
gtimeout 15 python cmds.py && echo 'commands page updated'
status=$?
if test $status -eq 124
then
	echo 'commands page timed out'
elif test $status -gt 0
then
	echo 'commands page failed'
fi
gtimeout 15 python users.py && echo 'users page updated'
status=$?q
if test $status -eq 124
then
	echo 'users page timed out'
elif test $status -gt 0
then
	echo 'users page failed'
fi
git add -u && echo 'git added'
git reset -- Settings.py
git commit -m "Update" && echo 'git committed'
git push -u origin master && echo 'git pushed'
echo 'end of script'

