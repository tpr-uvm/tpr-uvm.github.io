#!/Desktop/tprInfo
echo Set Path
python site.py
python cmds.py
echo Python ran
git add --all
git commit -m "Update"
git push -u origin master
echo Git pushed
