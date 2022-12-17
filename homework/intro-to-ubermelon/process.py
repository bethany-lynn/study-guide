log_file = open("um-server-01.txt")
# accessing list in server

# creating a function - define as sales reports
# currently printing for tuesday - need to change to monday
def generate_sales_reports(log_file):
    
    for line in log_file: 
        # this goes through every line in the file
        
        line = line.rstrip()
        # this removes space
        
        day = line[0:3]
        # get first three characters in "line" -- thats where we get day of week from line
        # because all lines in this list are labeled with the days at the beginning of the
        # sentence. so the set first three characters were "TUE" and if we change to "MON"
        # then itll call monday
        
        if day == "Mon":
        #if first three characters are MON 
            print(line)


generate_sales_reports(log_file)
# passes argument through parameter
