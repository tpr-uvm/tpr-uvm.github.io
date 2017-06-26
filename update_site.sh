#!/Desktop/tprInfo
echo path set
python site.py && echo main page updated
timeout 10 python cmds.py && echo commands page updated
status=$?
if test $status -eq 124
then
	echo commands page failed
fi
timeout 10 python users.py && echo users page updated
status=$?
if test $status -eq 124
then
	echo users page failed
fi
git add --all
echo git added
git commit -m "Update"
echo git committed
git push -u origin master
echo git pushed
echo end of script

