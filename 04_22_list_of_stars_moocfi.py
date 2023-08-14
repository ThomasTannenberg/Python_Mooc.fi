# Write your solution here
def list_of_stars(star_counts):
    for count in star_counts:
        print('*' * count)

if __name__ == "__main__":
    star_counts = [3, 7, 1, 1, 2]
    list_of_stars(star_counts)




