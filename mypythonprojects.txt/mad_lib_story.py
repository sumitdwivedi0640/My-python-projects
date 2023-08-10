# Get user inputs for various parts of the story
animals_input = input("Enter an animal name: ")
profession_input = input("Enter a profession name: ")
cloth_input = input("Enter a piece of cloth name: ")
things_input = input("Enter a thing name: ")
name_input = input("Enter a name: ")
place_input = input("Enter a place name: ")
verb_input = input("Enter a verb in -ing form: ")
food_input = input("Enter a food name: ")

# Construct and display the personalized story
story = (
    "Say " + food_input + ", the photographer said as the camera flashed. "
    + name_input + " and I had gone to " + place_input + " to get our photos taken on my birthday. "
    "The first photo we really wanted was a picture of us dressed as " + animals_input +
    " pretending to be a " + profession_input + ". When we saw the second photo, it was exactly what I wanted. "
    "We both looked like " + things_input + " wearing " + cloth_input + " and " + verb_input + " --exactly what I had in mind."
)

print(story)
