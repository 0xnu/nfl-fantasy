import csv
import sys
import urllib2
import subprocess
from datetime import datetime
from bs4 import BeautifulSoup

url = ('https://www.pro-football-reference.com/years/1995/fantasy.htm')

page = urllib2.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')
tbody = soup.find('tbody')
fantasytable = soup.find(id="all_fantasy")

# title
player = " "
posrank = [th.text for th in tbody.find_all('th', attrs={"data-stat": "fantasy_rank_pos"})]
ovrank = [th.text for th in tbody.find_all('th', attrs={"data-stat": "fantasy_rank_overall"})]
tm = [th.text for th in tbody.find_all('th', attrs={"data-stat": "team"})]
fantpos = [th.text for th in tbody.find_all('th', attrs={"data-stat": "fantasy_pos"})]
ages = [th.text for th in tbody.find_all('th', attrs={"data-stat": "age"})]
g = [th.text for th in tbody.find_all('th', attrs={"data-stat": "g"})]
gs = [th.text for th in tbody.find_all('th', attrs={"data-stat": "gs"})]
comp = [th.text for th in tbody.find_all('th', attrs={"data-stat": "pass_cmp"})]
att = [th.text for th in tbody.find_all('th', attrs={"data-stat": "pass_att"})]
yds = [th.text for th in tbody.find_all('th', attrs={"data-stat": "pass_yds"})]
td = [th.text for th in tbody.find_all('th', attrs={"data-stat": "pass_td"})]
intn = [th.text for th in tbody.find_all('th', attrs={"data-stat": "pass_int"})]
attn = [th.text for th in tbody.find_all('th', attrs={"data-stat": "rush_att"})]
ydsn = [th.text for th in tbody.find_all('th', attrs={"data-stat": "rush_yds"})]
rushtd = [th.text for th in tbody.find_all('th', attrs={"data-stat": "rush_td"})]
tgt = [th.text for th in tbody.find_all('th', attrs={"data-stat": "targets"})]
rect = [th.text for th in tbody.find_all('th', attrs={"data-stat": "rec"})]
rectyds = [th.text for th in tbody.find_all('th', attrs={"data-stat": "rec_yds"})]
rectdds = [th.text for th in tbody.find_all('th', attrs={"data-stat": "rec_td"})]
fantpt = [th.text for th in tbody.find_all('th', attrs={"data-stat": "fantasy_points"})]
dkpts = [th.text for th in tbody.find_all('th', attrs={"data-stat": "draftkings_points"})]
fdpts = [th.text for th in tbody.find_all('th', attrs={"data-stat": "fanduel_points"})]

# stats
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
blank = " "

# print title
# print players fantasy stats

row1 = zip(player,posrank,ovrank,tm,fantpos,ages,g,gs,comp,att,yds,td,intn,attn,ydsn,rushtd,tgt,rect,rectyds,rectdds,fantpt,dkpts,fdpts)
rows = zip(name,position_ranking,overall_ranking,team,position,age,games_played,games_started,passes_completed,passes_attempted,passing_yards,passing_touchdowns,interceptions,rushing_attempts,rushing_yards,rushing_touchdowns,pass_targets,receptions,receiving_yards,receiving_touchdowns,fantasy_points,draftkings_points,fanduel_points)

with open('./data/1995_nfl_fantasy.csv', 'wb') as f:
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
git_add("./data/1995_nfl_fantasy.csv")
git_add("nfl_fantasy.py")
git_commit("nfl_fantasy")
git_push()

sys.exit(0)