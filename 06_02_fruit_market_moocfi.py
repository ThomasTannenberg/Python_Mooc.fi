# write your solution here
def read_fruits():
#   opens an empty dictionary that can be written to and returned
    fruit_dictionary = {}

#   opens the csv file
    with open('fruits.csv') as csv_file:

#   goes through the file, line by line
        for line in csv_file:
            line = line.replace('\n', '')   # removes all line breaks

            #print('DEBUG: print lines: ', line)
            parts = line.split(';')         # creates a list: containing the strings from line that are seperated by ";"   

            #print('DEBUG: prints parts :', parts)     

            fruit_name = parts[0]           # extracts the first entry of the parts: list         
            fruit_price = parts[1]          # extracts the second entry of the parts: list

            fruit_dictionary[fruit_name] = float(fruit_price)       # creates the fruit dictionary containing the parts
    
    return fruit_dictionary                 # returns the dictionary so it can be printed



if __name__ == "__main__":
#    read_fruits()
    print(read_fruits())
