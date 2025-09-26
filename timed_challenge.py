# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
'''
Group 2: Fast Lookup / Uniqueness
5. Unique Word Count
Count how many distinct words are in the collection.
Input: "one fish two fish red fish blue fish"
Output: 5
'''
string = "one fish two fish red fish blue fish green"
def count_distict_words(string):
    string2 = set(string.split())
    return len(string2)




total = count_distict_words(string)

print(total)

'''
reflection (200 to 300 words) that answers the following:
    - What structure you chose and why
    - How the time limit shaped your decision 
    - What trade-offs or compromises you made under time pressure

I chose to use a set to solve this problem because it ask for uniqueness. Using a set seamed like the easiest and msot straight foward way
to go about solving this problem. At first I tried to use a differnet data structure. I thought about using a dictionary for fast look ups to look up 
each word to see if was unique. Then I decided that was the long way and a set was much easier since they already ignore duplicate values.
This way we can split the string by the empty spaces and turn it into a set. All we have to do is count the length of the set and that should be the number of unique elements. 





'''