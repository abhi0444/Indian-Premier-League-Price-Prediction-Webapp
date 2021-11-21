from flask import Flask, render_template, url_for, request, redirect
from models import predict
from models.predict import predict_score
from models.predict import forest

app = Flask(__name__)
TEAM_CODE = [
				'Chennai Super Kings',
				'Delhi Capitals',
				'Kings XI Punjab',
				'Kolkata Knight Riders',
				'Mumbai Indians',
				'Rajasthan Royals',
				'Royal Challengers Bangalore',
				'Sunrisers Hyderabad'
			 ]

predicted_score = None

@app.route('/')
def index():
	return render_template('index.html', teams=TEAM_CODE, score=predicted_score)

@app.route('/predict', methods=['GET', 'POST'])
def prediction():
	global predicted_score
	if request.method == 'POST':
		req = request.form
		batting_team = req['batting_team']
		bowling_team = req['bowling_team']
		runs = int(req['runs'])
		overs = float(req['overs'])
		wickets = int(req['wickets'])
		runs_last_5 = int(req['runs_last_5'])
		wickets_last_5 = int(req['wickets_last_5'])
		predicted_score = str(predict_score(batting_team, bowling_team, runs, wickets, overs, runs_last_5, wickets_last_5, forest))
		return render_template('predict.html', score=predicted_score)
	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, port=8000)
