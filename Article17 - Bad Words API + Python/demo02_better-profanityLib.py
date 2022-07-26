from better_profanity import profanity

# Basic example 
if __name__ == "__main__":
    profanity.load_censor_words()
 
    text = "You p1ec3 of sHit."
    censored_text = profanity.censor(text)
    print(censored_text)
    
# Advanced example
## Censor doesn’t care about word dividers:
if __name__ == "__main__":
    text = "...sh1t...hello_dog_fuck,,,,123"
 
    censored_text = profanity.censor(text)
    print(censored_text)

## Censor swear words with custom characters: 
if __name__ == "__main__":
    text = "You p1ec3 of sHit."
 
    censored_text = profanity.censor(text, '-')
    print(censored_text)
    
# Limitation
## Bypassed string
profanity.censor('I just have sexx')
 
profanity.censor('jerkk off')