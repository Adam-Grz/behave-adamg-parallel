import matplotlib.pyplot as plt
import numpy

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
def steps_chart(green, blue, red, folder):
	labels = 'Passed', 'Skipped', 'Failed'
	sizes = numpy.array([green, blue, red])
	cols = ['green', 'blue', 'red']

	def absolute_value(val):
	    a  = numpy.round(val/100.*sizes.sum(), 0)
	    return int(a)

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, labels=labels, autopct=absolute_value, colors=cols)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

	plt.title("Steps:")
	plt.savefig(f'{folder}/images/steps_chart.png', bbox_inches='tight')

def scens_chart(green, blue, red, folder):
	labels = 'Passed', 'Skipped', 'Failed'
	sizes = numpy.array([green, blue, red])
	cols = ['green', 'blue', 'red']

	def absolute_value(val):
	    a  = numpy.round(val/100.*sizes.sum(), 0)
	    return int(a)

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, labels=labels, autopct=absolute_value, colors=cols)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

	plt.title("Scenarios:")
	plt.savefig(f'{folder}/images/scens_chart.png', bbox_inches='tight')

def feats_chart(green, blue, red, folder):
	labels = 'Passed', 'Skipped', 'Failed'
	sizes = numpy.array([green, blue, red])
	cols = ['green', 'blue', 'red']

	def absolute_value(val):
	    a  = numpy.round(val/100.*sizes.sum(), 0)
	    return int(a)

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, labels=labels, autopct=absolute_value, colors=cols)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

	plt.title("Features:")
	plt.savefig(f'{folder}/images/feats_chart.png', bbox_inches='tight')

