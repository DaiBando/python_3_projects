class Quotes:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer



name = input('Please enter your name:  ')

if name:
    print('Thank you for entering your name.\n')
    print('Hello ' + name + " and welcome to the TV/Movie Trivia Game! You'll be shown a famous quote from a movie or show and must choose the correct answer. Let us begin. Good luck!\n")
else:
    print('You did not enter a name as directed.')
    

quote_prompts = [
     "'Frankly, my dear, I don't give a damn.' \n(a)Star Wars\n(b)Gone with the Wind\n(c)Patton\n",
     "'I'm going to make him an offer he can't refuse.' \n(a)Tremors\n(b)Patton\n(c)The Godfather\n",
     "'As you wish ' \n(a)The Princess Bride\n(b)Love Story\n(c)Dracula\n" ,
     "'Welcome to the real world. It sucks. You’re gonna love it! ' \n(a)M.A.S.H.\n(b)Twilight Zone\n(c)Friends\n ",
     "'You can’t eat this soup standing up. Your knees buckle. ' \n(a)Seinfeld\n(b)Murphy Brown\n(c)Star Trek\n",
     "'Nobody puts Baby in a corner. ' \n(a)True Grit\n(b)Dirty Dancing\n(c)Mermaids\n",
     "'Snakes. Why did it have to be snakes?' \n(a)Star Wars\n(b)Patton\n(c)Indiana Jones and the Last Crusade\n",
     "'Women. You can’t live with ’em. Pass the beernuts. ' \n(a)Cheers\n(b)S.W.A.T.\n(c)The Waltons\n",
     "'Ditto. ' \n(a)The Exorcist\n(b)Ghost\n(c)Halloween\n",
     "'Marsha, Marsha, Marsha! ' \n(a)Alice\n(b)Sanford and Son\n(c)The Brady Bunch\n",
     "'You yell, “Barracuda,” everybody says, “huh, what?” You yell “Shark,” we’ve got a panic on our hands on the Fourth of July. ' \n(a)Jaws\n(b)Transformers\n(c)Moby Dick\n",
     "'Good morning, Angels. ' \n(a)I Dream of Jeannie\n(b)HR Puffenstuff\n(c)Charlie's Angels\n",
     "'Heyyyyy! ' \n(a)Happy Days\n(b)Laverne and Shirley\n(c)Joanie Loves Chachi\n",
     "'This is the city ... ' \n(a)Adam 12\n(b)Police Story\n(c)Dragnet\n",
     "'The truth is out there' \n(a)X-Files\n(b)Outer Limits\n(c)The Night Stalker\n ",
     "'Now cut that out!' \n(a)Make Room For Daddy\n(b)The Jack Benny Show\n(c)Father Knows Best\n",
     "'Holy crap!' \n(a)Everyone Loves Raymond\n(b)The Lucy Show\n(c)60 Minutes\n",
     "'I know nothing!' \n(a)Happy Days\n(b)Hogan's Heroes\n(c)Barney Miller\n ",
     "'Good night, John Boy' \n(a)Star Trek\n(b)Starsky and Hutch\n(c)The Waltons\n ",
     "'Toto, I've got a feeling we're not in Kansas anymore.' \n(a)Snow White\n(b)The Wizard of Oz\n(c)The Godfather\n ",
     "'Go ahead, make my day' \n(a)Sudden Impact\n(b)How Green Was My Valley\n(c)Aliens\n ",
     "'May the Force be with you.' \n(a)Star Trek\n(b)Star Wars\n(c)Happy Gilmore\n ",
     "'Love means never having to say you're sorry' \n(a)The Exorcist\n(b)Jaws\n(c)Love Story\n ",
     "'Rosebud.' \n(a)Hackers\n(b)Citizen Kane\n(c)On The Waterfront\n ",
     "'Louis, I think this is the beginning of a beautiful friendship.' \n(a)The Big Heat\n(b)Casablanca\n(c)The Treasure of the Sierra Madre\n ",     
]

quotes = [
     Quotes(quote_prompts[0], "b"),
     Quotes(quote_prompts[1], "c"),
     Quotes(quote_prompts[2], "a"),
     Quotes(quote_prompts[3], "c"),
     Quotes(quote_prompts[4], "a"),
     Quotes(quote_prompts[5], "b"),
     Quotes(quote_prompts[6], "c"),
     Quotes(quote_prompts[7], "a"),
     Quotes(quote_prompts[8], "b"),
     Quotes(quote_prompts[9], "c"),
     Quotes(quote_prompts[10], "a"),
     Quotes(quote_prompts[11], "c"),
     Quotes(quote_prompts[12], "a"),
     Quotes(quote_prompts[13], "c"),
     Quotes(quote_prompts[14], "a"),
     Quotes(quote_prompts[15], "b"),
     Quotes(quote_prompts[16], "a"),
     Quotes(quote_prompts[17], "b"),
     Quotes(quote_prompts[18], "c"),
     Quotes(quote_prompts[19], "b"),
     Quotes(quote_prompts[20], "a"),
     Quotes(quote_prompts[21], "b"),
     Quotes(quote_prompts[22], "c"),
     Quotes(quote_prompts[23], "b"),
     Quotes(quote_prompts[24], "b"),     
]

def run_quiz(quotes):
     score = 0
     for quote in quotes:
          answer = input(quote.prompt)
          if answer == quote.answer:
               score += 1
     print("Game completed " + name + "...you got", score, "out of", len(quotes), "correct.\n")

run_quiz(quotes)

answer = input("Do you want to end our game session " + name + "? (yes or no)\n")

if answer ==("yes" or "y"):
     print("Awww, sorry to see you go. Thanks for playing " + name + ", please come back again!")

else:
     print("That's great " + name + ", let's restart the game again!\n")
     run_quiz(quotes)
