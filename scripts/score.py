import notify2
import time
from pycricbuzz import Cricbuzz
from pprint import pprint 

ICON = '/home/dell/Downloads/beautiful-fantasy-cricket-bat-and-ball-hd-free-wallpapers-640x360.jpg'

cric = Cricbuzz()
matches = cric.matches()
scores = []
flag = 0

notify2.init('Cricket updates')
notif = notify2.Notification(None, icon = ICON)
notif.set_urgency(notify2.URGENCY_NORMAL)
notif.set_timeout(100000)

for match in matches:
	if match['mchstate'] == 'inprogress' or match['mchstate'] == 'Result' or match['mchstate'] == 'complete':
		try:
			scores.append(cric.livescore(match['id']))
		except KeyError:
			if match['mchstate'] == 'Result' or match['mchstate'] == 'complete':
				notif.update(match['srs'] + ', ' + match['mnum'], match['mchdesc'] + '\n' + match['status'])
				notif.show()
				time.sleep(5)	
	elif match['mchstate'] == 'stump':
		notif.update(match['srs'], '\nAt stumps: ' + match['status'])
		notif.show()
		time.sleep(5)
	elif match['mchstate'] == 'tea':
		notif.update(match['srs'], '\nAt tea: ' + match['status'])
		notif.show()
		time.sleep(5)
	elif match['mchstate'] == 'lunch':
		notif.update(match['srs'], '\nAt lunch: ' + match['status'])
		notif.show()
		time.sleep(5)
	elif match['mchstate'] == 'dinner':
		notif.update(match['srs'], '\nAt dinner: ' + match['status'])
		notif.show()
		time.sleep(5)
	elif match['mchstate'] == 'innings break':
		notif.update(match['srs'], match['mnum']+ '\n' + '\nInnings break: ' + match['status'])
		notif.show()
		time.sleep(5)
	elif match['mchstate'] == 'rain' or match['mchstate'] == 'badlight':
		notif.update(match['srs'], match['status'] + '\n' + 'Play stopped due to rain/badlight.')
		notif.show()
		time.sleep(5)
	elif match['mchstate'] == 'preview' or match['mchstate'] == 'nextlive' and flag == 0:
		notif.update('Up next ' + match['srs'], match['mnum'] + '\n' + match['status'])
		notif.show()
		flag = 1
		time.sleep(5)

for score in scores:
	batting = score['batting']['score']
	batting_dets = batting[0]
	batting_team = score['batting']['team']
	bowling = score['bowling']['team']
	notif.update(score['matchinfo']['srs'], score['matchinfo']['mnum'] + '\n' + batting_team + ' ' + batting_dets['desc'] + '  ' + 'Score: ' + batting_dets['runs'] + '/' + batting_dets['wickets'] + '	' + bowling + '  ' + 'Overs: ' + batting_dets['overs'] + '\n' + score['matchinfo']['status'])	
	notif.show()
	time.sleep(5)
notif.close()
