from termcolor import colored
import time

print('''
                            ********WELCOME TO VOTING SESSION*********
''')
nominee_1 = input('Enter the nominee_1 Name : ')
nominee_2 = input('Enter the nominee_2 Name : ')

nom_one_vote = 0
nom_two_vote = 0

votes_id = [1, 2, 3, 4, 5]
num_of_votes = len(votes_id)

while True:
    if not votes_id:
        print('\nVoting Session has been over')
        time.sleep(5)
        if nom_one_vote > nom_two_vote:
            percentage = (nom_one_vote / num_of_votes) * 100
            print(nominee_1, 'won with', str(percentage)+'%', 'votes')
            break
        elif nom_two_vote > nom_one_vote:
            percentage = (nom_two_vote / num_of_votes) * 100
            print(nominee_2, 'won with', str(percentage)+'%', 'votes')
            break
        elif nom_two_vote == nom_one_vote:
            print(nominee_1,'and', nominee_2, 'both are get equal vote')
            break
    else:
        voter = int(input('\nEnter your voter ID number: '))
        if voter in votes_id:
            print(colored('You are a voter', 'yellow'))
            vote = int(input('Enter your voter 1 or 2: '))
            if vote == 1:
                nom_one_vote += 1
                votes_id.remove(voter)
                print(colored('Thank you for casting your vote', 'green'))
            elif vote == 2:
                nom_two_vote += 1
                votes_id.remove(voter)
                print(colored('Thank you for casting your vote', 'green'))
            else:
                print(colored('Your selected leader number not correct', 'red'))
                print(f'''
                   Nominee Available:
                        1. {nominee_1}
                        2. {nominee_2}
                ''')
        else:
            print(colored('You are not voter here or You have already voted. Thank You!!!!!', 'red'))
