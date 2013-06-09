#!/usr/bin/python

# http://www.freebsd.org/cgi/cvsweb.cgi/src/share/dict/web2?rev=1.12;content-type=text%2Fplain

from random import Random
import argparse
import sys
import os

os.chdir(sys.path[0])

VERSION = 0.1

parser = argparse.ArgumentParser(description='Argaprse boilerplate example')
# -v, --version - show version and dictionary stats.
parser.add_argument('-v', '--version', action='store_true', help="Show version and dictionary stats.")
parser.add_argument('num_words', metavar="NUM_WORDS", nargs='?', type=int, default=4, help='Number of words to pick.')
group = parser.add_mutually_exclusive_group()
group.add_argument('--simple', action='store_true', default=True, help="Use Wiktionary's General Service List (~2000 words)")
group.add_argument('--full', action='store_true',                 help="Use Wiktionary full word list (~1.6 million words)")
args = parser.parse_args()

filename='wiktionary_english_full' if args.full else 'wiktionary_english_most_common'

words=[w.strip() for w in open(filename).readlines()]
r=Random()

if args.version:
	print "Version %3.2f, %d words." % (VERSION, len(words))
	sys.exit(0)
else:
	print ' '.join([r.choice(words) for i in range(args.num_words)])
