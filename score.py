import notify2
import time
from pycricbuzz import Cricbuzz

ICON = '/home/dell/Downloads/beautiful-fantasy-cricket-bat-and-ball-hd-free-wallpapers-640x360.jpg'

cric = Cricbuzz()
matches = cric.matches()
scores = []
notify2.init('Cricket updates')
notif = notify2.Notification(None, icon = ICON)
notif.set_urgency(notify2.URGENCY_NORMAL)
notif.set_timeout(10000)

for match in matches:
	if match['mchstate'] == 'inprogress' or match['mchstate'] == 'Result' or match['mchstate'] == 'complete':
		scores.append(cric.livescore(match['id']))
	elif match['mchstate'] == 'stump' or match['mchstate'] == 'stumps':
		notif.update(match['srs'], 'At stumps: ' + match['status'])
		notif.show()
	elif match['mchstate'] == 'lunch':
		notif.update(match['srs'], 'At lunch: ' + match['status'])
		notif.show()
	elif match['mchstate'] == 'dinner':
		notif.update(match['srs'], 'At dinner: ' + match['status'])
		notif.show()
	elif match['mchstate'] == 'tea':
		notif.update(match['srs'], 'At tea: ' + match['status'])
		notif.show()
		
for score in scores:
	batting = score['batting']['score']
	batting_dets = batting[0]
	batting_team = score['batting']['team']
	bowling = score['bowling']['team']
	if score['matchinfo']['mchstate'] == 'Result' or mat:
		notif.update(score['matchinfo']['mchdesc'], score['matchinfo']['status'])
	else:
		notif.update(score['matchinfo']['srs'] + '  ' + batting_team + '  ' + batting_dets['desc'] + '  ' + 'Score: ' + batting_dets['runs'] + '/' + batting_dets['wickets'] + '		' + bowling + '  ' + 'Overs: ' + batting_dets['overs'], score['matchinfo']['status'])	
	notif.show()
	notif.set_timeout(10000)
	time.sleep(5)
notif.close()
