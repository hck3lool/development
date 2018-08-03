#!/usr/bin/env python

import sys
import os
import robot

sys.path.append("libraries")

def execute_robot():
	"""Execute Robot Framework. """

	sys.path.append(os.path.join(os.getcwd(), "libraries"))
	robot.run_cli(sys.argv[1:] + ["--outputdir", "output/results",
					"--debugfile", "debug.txt",
					"cases"])

if __name__ == "__main__":
	execute_robot()

