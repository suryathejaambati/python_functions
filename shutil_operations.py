import shutil

#'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree'

src="/home/ec2-user/Python-3.7.7"
dest="/home/ec2-user/sury/python37"
#shutil.copyfile(src,dest)
#shutil.copy(src,dest)
#shutil.copy2(src,dest)
#shutil.copymode(src,dest)
#shutil.copyfileobj(src,dest)
#shutil.copytree(src,dest)
shutil.rmtree(dest)
