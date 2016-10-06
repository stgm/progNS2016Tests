import checkpy.test as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

def before():
	lib.neutralizeFunctionFromImport(lib.module(_fileName), "show", "matplotlib.pyplot")

@t.test(0)
def correctTimeTillParachute(test):
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName).split("\n")[0], "12.2")
	test.description = lambda : "print de tijd die verstrijkt tot de parachute open moet (zonder luchtweerstand)"

@t.test(1)
def correctExtraTime(test):
	test.test = lambda : assertlib.match(lib.outputOf(_fileName).split("\n")[1], ".*5\.0[5-7].*")
	test.description = lambda : "print de tijd die er bij komt door de luchtweerstand"
