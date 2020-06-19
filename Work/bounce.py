# bounce.py
#
# Exercise 1.5
def bounce_hits(number_of_times):
    height = 100
    counter = 1
    bounced_proportion = 3/5
    while counter <= number_of_times:
        height *= bounced_proportion
        print(round(height,4))
        counter += 1

bounce_hits(10)
