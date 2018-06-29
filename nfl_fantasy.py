import csv
import sys
import urllib2
import subprocess
from bs4 import BeautifulSoup
from datetime import datetime
import csv

url = ('https://www.pro-football-reference.com/years/2017/fantasy.htm')

page = urllib2.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')
tbody = soup.find('tbody')
fantasytable = soup.find(id="all_fantasy")
#fantasy_rankings = [h2.text for h2 in fantasytable.find_all('h2')]
name = [td.text for td in tbody.find_all('td', attrs={"data-stat": "player"})]
position_ranking = [td.text for td in tbody.find_all('td', attrs={"data-stat": "fantasy_rank_pos"})]
overall_ranking = [td.text for td in tbody.find_all('td', attrs={"data-stat": "fantasy_rank_overall"})]
team = [td.text for td in tbody.find_all('td', attrs={"data-stat": "team"})]
position = [td.text for td in tbody.find_all('td', attrs={"data-stat": "fantasy_pos"})]
age = [td.text for td in tbody.find_all('td', attrs={"data-stat": "age"})]
games_played = [td.text for td in tbody.find_all('td', attrs={"data-stat": "g"})]
games_started = [td.text for td in tbody.find_all('td', attrs={"data-stat": "gs"})]
passes_completed = [td.text for td in tbody.find_all('td', attrs={"data-stat": "pass_cmp"})]
passes_attempted = [td.text for td in tbody.find_all('td', attrs={"data-stat": "pass_att"})]
passing_yards = [td.text for td in tbody.find_all('td', attrs={"data-stat": "pass_yds"})]
passing_touchdowns = [td.text for td in tbody.find_all('td', attrs={"data-stat": "pass_td"})]
interceptions = [td.text for td in tbody.find_all('td', attrs={"data-stat": "pass_int"})]
rushing_attempts = [td.text for td in tbody.find_all('td', attrs={"data-stat": "rush_att"})]
rushing_yards = [td.text for td in tbody.find_all('td', attrs={"data-stat": "rush_yds"})]
rushing_touchdowns = [td.text for td in tbody.find_all('td', attrs={"data-stat": "rush_td"})]
pass_targets = [td.text for td in tbody.find_all('td', attrs={"data-stat": "targets"})]
receptions = [td.text for td in tbody.find_all('td', attrs={"data-stat": "rec"})]
receiving_yards = [td.text for td in tbody.find_all('td', attrs={"data-stat": "rec_yds"})]
receiving_touchdowns = [td.text for td in tbody.find_all('td', attrs={"data-stat": "rec_td"})]
fantasy_points = [td.text for td in tbody.find_all('td', attrs={"data-stat": "fantasy_points"})]
draftkings_points = [td.text for td in tbody.find_all('td', attrs={"data-stat": "draftkings_points"})]
fanduel_points = [td.text for td in tbody.find_all('td', attrs={"data-stat": "fanduel_points"})]
player = "Player"
blank = " "

# print date
# print players fantasy stats

row1 = zip(player,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank)
rows = zip(name,position_ranking,overall_ranking,team,position,age,games_played,games_started,passes_completed,passes_attempted,passing_yards,passing_touchdowns,interceptions,rushing_attempts,rushing_yards,rushing_touchdowns,pass_targets,receptions,receiving_yards,receiving_touchdowns,fantasy_points,draftkings_points,fanduel_points)

with open('nfl_fantasy.csv', 'wb') as f:
	writer = csv.writer(f)
	for row in row1:
		writer.writerow(row)
	for row in rows:
		writer.writerow(row)

def git_add(file):
    subprocess.call(["git", "add", file])

def git_commit(message):
    subprocess.call(["git", "commit", "-m", "nfl fantasy stats"])

def git_push():
    subprocess.call(["git", "push", "origin", "master"])

if __name__ == "__main__":
    start = datetime.now()

today = datetime.strftime(datetime.now(), '%Y-%m-%d \t %H:%M')

total = datetime.now() - start
with open("log.txt", 'a') as f:
	f.write(today + " - " + str(total) + "\n")

git_add("log.txt")
git_add("nfl_fantasy.csv")
git_add("nfl_fantasy.py")
git_commit("nfl_fantasy")
git_push()

sys.exit(0)