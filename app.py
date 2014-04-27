from flask import Flask, request, flash, render_template, redirect, url_for

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
	try:
		meal_cost = float(request.form['meal_cost'])
	except:
		ValueError
		flash('Meal cost must be a numeral')
		return redirect('/')
	try:
		tip_percentage = float(request.form['tip_percentage'])
	except:
		ValueError
		flash('Tip percentage must be a numeral')
		return redirect('/')
	if tip_percentage < 0:
		flash('Tip percentage must be 0 or greater')
		return redirect('/')
	tip_amount = meal_cost * (tip_percentage/100)
	return render_template('results.html', results=tip_amount)

if __name__ == '__main__':
	app.run(debug=True)