import random

def random_fixture_generator():
    player_list = []
    number_of_players = int(input("Enter number of players = "))
    for i in range(number_of_players):
        player_list.append(input("Enter name = "))
    random.shuffle(player_list)
    print(player_list)
    first = 0
    second = 1
    for i in range(1, number_of_players // 2 + 1):
        print("Pair", i, " - ", player_list[first], " vs ", player_list[second])
        first += 2
        second += 2


def start_scorecard():
    overs = int(input("Enter total Overs = "))
    ball = 0
    current_over = []
    total_score = 0
    wickets_fallen=0
    for i in range(overs):

        print("""
      dot=0
      single=1
      double=2
      triple=3
      four=4
      six=6
      wicket=w         
      negative=-2
      wide=wd
      remove last ball=undo            
      """)  # solvecase that if user wants to undo last ball of an over
            # solve case for all out
        while ball != 6:
            outcome = input("What Happened!?  ")
            if outcome != 'nb':
                match outcome:  # this block can be unidented
                    case '0':
                        current_over.append(0)
                        ball+=1
                    case '1':
                        current_over.append(1)
                        ball = ball + 1
                    case '2':
                        current_over.append(2)
                        ball += 1
                    case '3':
                        current_over.append(3)
                        ball += 1
                    case '4':
                        current_over.append(4)
                        ball += 1
                    case '6':
                        current_over.append(6)
                        ball += 1
                    case 'w':
                        current_over.append('w')
                        ball += 1
                        wickets_fallen+=1
                    case '-2':
                        current_over.append(-2)
                        ball += 1
                    case 'wd':
                        current_over.append('wd')
                    case 'undo':
                        if current_over != []:
                            ball -= 1
                            current_over.pop()
                        else:
                            print("over has not started yet")

            else:
                outcome_on_noball = input('what happened on no ball?')
                match outcome_on_noball:
                    case '0':
                        current_over.append('nb')
                    case '1':
                        current_over.append('nb+1')
                    case '2':
                        current_over.append('nb+2')
                    case '3':
                        current_over.append('nb+3')
                    case '4':
                        current_over.append('nb+4')
                    case '6':
                        current_over.append('nb+6')
                    case 'w':
                        current_over.append('nb')
                    case '-2':
                        current_over.append('nb')
                    case 'wd':
                        current_over.append('nb')
        print(current_over)
        total = 0
        for i in current_over:
            if type(i) is int:
                total += i
            if i == 'wd':
                total += 1
            if i == 'nb':
                total += 1
            if i in ['nb+1', 'nb+2', 'nb+3', 'nb+4', 'nb+6']:
                total += int(i[-1]) + 1

        print("total of over=", total)
        total_score += total
        current_over = []
        ball = 0
    print("total score = ", total_score)
    print("wickets fallen = ",wickets_fallen)

start_scorecard()
