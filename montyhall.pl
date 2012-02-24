#!/usr/bin/perl -w
# $Id: montyhall.pl,v 1.3 2011/10/24 11:00:04 oraz Exp $
# Monty Hall problem sampling

use strict;

my $samples = 100000;
$samples = $ARGV[0] if defined $ARGV[0];
my @score = (0,0);
while($samples-- > 0)
{
	# select doors
	my @doors = (0,0,0);
	my $car = int(rand(3));
	# put car behind car door
	$doors[$car] = 1;
	my $opened = -1;
	my $rest = -1;
	# choose door1
	my $door1 = int(rand(3));
	# remove first free goat
	for(my $i = 0; $i < 3; $i++)
	{
		next if($i == $door1);
		next if($doors[$i] > 0);
		# open door
		$opened = $i; last;
	}
	die "no doors opened!" if $opened < 0;
	# find rest door;
	for(my $i = 0; $i < 3; $i++)
	{
		next if($i == $door1);
		next if($i == $opened);
		$rest = $i; last;
	}
	die "no doors remain!" if $rest < 0;
	if($doors[$door1] > 0) {
		$score[0]++;
	} else {
		$score[1]++;
	}
}
print"Final score:\n\tif keeps door => $score[0]\n\tif changes door => $score[1]\n"

