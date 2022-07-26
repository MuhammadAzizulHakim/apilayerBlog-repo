from profanity import profanity

# Basic example 
profanity.contains_profanity("You smell like shit.")
profanity.censor("You smell like shit.")

# Was it case-sensitive?
profanity.contains_profanity("You smell like shit.")
profanity.contains_profanity("You smell like SHIT.")
profanity.contains_profanity("You smell like ShIt.")
profanity.contains_profanity("You smell like sHiT.")

profanity.censor("You smell like shit.")
profanity.censor("You smell like SHIT.")
profanity.censor("You smell like ShIt.")
profanity.censor("You smell like sHiT.")