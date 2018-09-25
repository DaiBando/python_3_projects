import random
import string

class Quote():
    def __init__(self, question, answers):
        self.question=question
        self.answers = answers
        
quotes = [
    Quote("Frankly, my dear, I don't give a damn.",[
        "Gone with the Wind",
        "Star Wars",
        "Patton"]),
    Quote("I'm going to make him an offer he can't refuse.",[
        "The Godfather",
        "Tremors",
        "Patton"]),
    Quote("As you wish ",[
        "The Princess Bride",
        "Love Story",
        "Dracula"]),
    Quote("Welcome to the real world. It sucks. You’re gonna love it! ",[
        "Friends",
        "M.A.S.H.",
        "Twilight Zone"]),
    Quote("You can’t eat this soup standing up. Your knees buckle. ",[
        "Seinfeld",
        "Murphy Brown",
        "Star Trek"]),
    Quote("Nobody puts Baby in a corner. ",[
        "Dirty Dancing",
        "True Grit",
        "Mermaids"]),
    Quote("Snakes. Why did it have to be snakes?",[
        "Indiana Jones and the Last Crusade",
        "Star Wars",
        "Patton"]),
    Quote("Women. You can’t live with ’em. Pass the beernuts. ",[
        "Cheers",
        "S.W.A.T.",
        "The Waltons"]),
    Quote("Ditto. ",[
        "Ghost",
        "The Exorcist",
        "Halloween"]),
    Quote("Marsha, Marsha, Marsha! ",[
        "The Brady Bunch",
        "Alice",
        "Sanford and Son"]),
    Quote("I think we're gonna need a bigger boat",[
        "Jaws",
        "Transformers",
        "Moby Dick"]),
    Quote("Good morning, Angels. ",[
        "Charlie's Angels",
        "I Dream of Jeannie",
        "HR Puffenstuff"]),
    Quote("Heyyyyy! ",[
        "Happy Days",
        "Laverne and Shirley",
        "Joanie Loves Chachi"]),
    Quote("This is the city ... ",[
        "Dragnet",
        "Adam 12",
        "Police Story"]),
    Quote("The truth is out there",[
        "X-Files",
        "Outer Limits",
        "The Night Stalker"]),
    Quote("Now cut that out!",[
        "The Jack Benny Show",
        "Make Room For Daddy",
        "Father Knows Best"]),
    Quote("Holy crap!",[
        "Everyone Loves Raymond",
        "The Lucy Show",
        "60 Minutes"]),
    Quote("I know nothing!",[
        "Hogan's Heroes",
        "Happy Days",
        "Barney Miller"]),
    Quote("Good night, John Boy",[
        "The Waltons",
        "Star Trek",
        "Starsky and Hutch"]),
    Quote("Toto, I've got a feeling we're not in Kansas anymore.",[
        "The Wizard of Oz",
        "Snow White",
        "The Godfather"]),
    Quote("Go ahead, make my day",[
        "Sudden Impact",
        "How Green Was My Valley",
        "Aliens"]),
    Quote("May the Force be with you.",[
        "Star Wars",
        "Star Trek",
        "Happy Gilmore"]),
    Quote("Love means never having to say you're sorry",[
        "Love Story",
        "The Exorcist",
        "Jaws"]),
    Quote("Rosebud.",[
        "Citizen Kane",
        "Hackers",
        "On The Waterfront"]),
    Quote("Louis, I think this is the beginning of a beautiful friendship.",[
        "Casablanca",
        "The Big Heat",
        "The Treasure of the Sierra Madre"]),
    ]
    
def run_quiz():
    quotes_in_quiz = random.sample(quotes, 7)
    
    score = 0
    for quote in quotes_in_quiz:
        print('------------------------------')
        print(quote.question)
        order = random.sample(range(len(quote.answers)),len(quote.answers))
        right_answer = string.ascii_letters[order.index(0)]
        for i in range(len(quote.answers)):
            print(f'  ({string.ascii_letters[i]}) {quote.answers[order[i]]}')
        answer = input('your answer?').lower()
        if answer == right_answer:
            print('right')
            score += 1
        else:
            print('wrong')
            
    print('your score is', score)

while True:
    name = input('Please enter your name:')

    if name:
        print('Thank you for entering your name.')
        print(f'Hello {name} and welcome to the TV/Movie Trivia Game. Given a famous quote from a movie or show, choose the correct answer.!')
        print('Let us begin. Good luck!')
        break
    else:
        print('You did not enter a name as directed.')
           
while True:
    run_quiz()
    answer = input(f"Do you want to end our game session {name}? (yes or no)").lower()

    if answer in ("yes", "y"):
        print(f"Awww, sorry to see you go. Thanks for playing {name}, please come back again!")
        break
    else:
        print(f"That's great {name}, let's restart the game")
