import sys, random
import argparse
from os import path


class Roll(object):

	def check_ranges(self, dicetype, dicecount):
		if dicecount < 21 and dicetype in (6, 12, 10, 20):
			pass
		elif dicecount or dicetype:
			raise(ValueError("Incorrect Values: --help for more details"))

	def dice_roll(self, dicetype, dicecount, total, drm):
		if total:
			 print("TOTAL: %s" % (dicetype*dicecount))
			 if drm:
			 	print("TOTAL & DRM: %s" % (dicetype*dicecount+drm))
			 return

		if dicetype in (6, 12):
			st = 1
			for dc in range(dicecount):
				roll_it = random.randint(st, dicetype)
				if drm:
					roll_it = (roll_it+drm)
					print("ROLLED: %s with DRM: %s" % \
						(roll_it, drm))
				print("ROLLED: %s") % roll_it
				return
		elif dicetype in (10, 20):
			st = 0
			for dc in range(dicecount):
				roll_it = random.randint(st, dicetype)
				if drm:
					print("ROLLED: %s with DRM: %s:" % \
						(roll_it, drm))
					roll_it = (roll_it+drm)
				print("ROLLED: %s") % roll_it
				return


	def __init__(self, dicecount, dicetype, total, drm):
		self.dicetype = int(dicetype)
		self.dicecount = int(dicecount)
		self.drm = drm
		self.total = total
		self.check_ranges(dicecount, dicetype)
		self.dice_roll(dicecount, dicetype, total, drm)
	
		
def main(argv):
	parser = argparse.ArgumentParser(
		description='Roll the Dice 1-20:D6,12,10,20'
		)
	parser.add_argument('-d', '--dicetype',
		required=True, type=int,
		help='Your Options are D6, D12, D10, D20'
		)
	parser.add_argument('-c', '--dicecount',
		required=True,
		type=int,
		help='Max dice count: 1-20'
		)
	parser.add_argument('-t','--total',
		required=False, 
		action='store_true'
		)
	parser.add_argument('--drm',
		required=False, 
		type=int,
		help='Dice Roll Modifier'
		)

	args = parser.parse_args(argv)

	if args.total:
		total = args.total
	if args.drm:		
		drm = args.drm

	dicecount = args.dicecount
	dicetype = args.dicetype
	r = Roll(
		args.dicetype,
		args.dicecount,
		args.total,
		args.drm
		)


if __name__ == '__main__':
	main(sys.argv[1:])



