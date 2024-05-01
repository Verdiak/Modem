'''
when bulb pressed

sadKeywords = ['sad','groggy','bored','depressed']
angryKeywords = ['angry','annoyed','irritable']
selfConciousKeywords = ['conscious','body','face','weight','fat','eating','ate','food','ugly']
conflictKeywords = ['told','said','hurt','fought','think','want']
lonelyKeywords = ['lonely','alone','friends']

sadSuggestions = ['clean','listen to music','pick the easiest thing on your to do list and tick it off','go outside','shower']
angrySuggestions = ['you could just be hungry','punch a pillow','go somewhere you can scream']
selfConciousSuggestions = ['go for a run','do a workout','plan healthy meals for the rest of the day','wear something comfortable']
conflictSuggestions = ['give them space and let time heal','try to see it from their perspective','tell them how it made you feel']
lonelySuggestions = []

relevantSuggestions = []

for keyword in sadKeywords:
    print(keyword)
    if keyword in rant.lower():
        relevantSuggestions += sadSuggestions
    break

for keyword in angryKeywords:
    print(keyword)
    if keyword in rant.lower():
        relevantSuggestions += angrySuggestions
    break

for keyword in selfConciousKeywords:
    print(keyword)
    if keyword in rant.lower():
        relevantSuggestions += selfConciousSuggestions
    break

for keyword in conflictKeywords:
    print(keyword)
    if keyword in rant.lower():
        relevantSuggestions += conflictSuggestions
    break

for keyword in lonelyKeywords:
    print(keyword)
    if keyword in rant.lower():
        relevantSuggestions += lonelySuggestions
    break
	
if not relevantSuggestions:
    relevantSuggestions += sadSuggestions + angrySuggestions + selfConciousSuggestions + conflictSuggestions + lonelySuggestions

#print a random one in darkGreen
#if they don't let them leave or save without writing what they're gonna do
'''    