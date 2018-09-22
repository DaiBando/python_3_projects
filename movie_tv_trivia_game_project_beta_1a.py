import random
import string

class Quote():
    def __init__(self, question, answers):
        self.question=question
        self.answers = answers

    
def ask_question(quote):
    print('------------------------------')
    print(quote.question)
    order = random.sample(range(len(quote.answers)),len(quote.answers))
    right_answer = string.ascii_letters[order.index(0)]
    for i in range(len(quote.answers)):
        print(f'  ({string.ascii_letters[i]}) {quote.answers[order[i]]}')


name = input('Please enter your name:  ')

if name:
    print('Thank you for entering your name.\n')
    print('Hello ' + name + " and welcome to the TV/Movie Trivia Game! You'll be shown a famous quote from a movie or show and must choose the correct answer. Let us begin. Good luck!\n")
else:
    print('You did not enter a name as directed.')
    


        
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
    Quote("You yell, “Barracuda,” everybody says, “huh, what?” You yell “Shark,” we’ve got a panic on our hands on the Fourth of July. ",[
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


quotes_answers = [
     Quotes(quote_answers[0], "Gone with the Wind"),
     Quotes(quote_answers[1], "The Godfather"),
     Quotes(quote_answers[2], "The Princess Bride"),
     Quotes(quote_answers[3], "Friends"),
     Quotes(quote_answers[4], "Seinfeld"),
     Quotes(quote_answers[5], "Dirty Dancing"),
     Quotes(quote_answers[6], "Indiana Jones and the Last Crusade"),
     Quotes(quote_answers[7], "Cheers"),
     Quotes(quote_answers[8], "Ghost"),
     Quotes(quote_answers[9], "The Brady Bunch"),
     Quotes(quote_answers[10], "Jaws"),
     Quotes(quote_answers[11], "Charlie's Angels"),
     Quotes(quote_answers[12], "Happy Days"),
     Quotes(quote_answers[13], "Dragnet"),
     Quotes(quote_answers[14], "X-Files"),
     Quotes(quote_answers[15], "The Jack Benny Show"),
     Quotes(quote_answers[16], "Everyone Loves Raymond"),
     Quotes(quote_answers[17], "Hogan's Heroes"),
     Quotes(quote_answers[18], "The Waltons"),
     Quotes(quote_answers[19], "The Wizard of Oz"),
     Quotes(quote_answers[20], "Sudden Impact"),
     Quotes(quote_answers[21], "Star Wars"),
     Quotes(quote_answers[22], "Love Story"),
     Quotes(quote_answers[23], "Citizen Kane"),
     Quotes(quote_answers[24], "Casablanca"),  



   

quotes_in_quiz = random.sample(quotes, 8)


for quote in quotes_in_quiz:
    ask_question(quote)

def run_quiz(quotes):
     score = 0
     for quote in quotes:
          answer = input(quote.answers)
          if answer == quote.answers:
               score += 1
     print("Game completed " + name + "...you got", score, "out of", len(quotes), "correct.\n")

run_quiz(quotes)

answer = input("Do you want to end our game session " + name + "? (yes or no)\n")

if answer in ("yes", "y"):
     print("Awww, sorry to see you go. Thanks for playing " + name + ", please come back again!")

else:
     print("That's great " + name + ", let's restart the game again!\n")
     run_quiz(quotes)
