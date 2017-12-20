from subprocess import call
import os

dir = os.listdir("train_1")
for f in dir:
	print("******************************************")
	print(f)
	call(["sox","train_1/" + f, "-b", "16", "train_sox/" + f])
	call(["sox","train_1/" + f, "-n", "stat"])
	call(["sox","train_1/" + f, "train_sox/" + f, "-n", "stat"])
	print("******************************************")
