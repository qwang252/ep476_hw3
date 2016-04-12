def check_blank_comments(filename):
    try:
       f= open(filename)
    except FileNotFoundError:
       print('cannout find the file under the name of '+filename)
    except UnsupportedOperation:
       print('the file under the name of '+filename+' is not readable')
    standard_file = True

    i = 1
    for line in f:
    line = line.strip().split()
    # check blank line and comments line
        if len(line)==0:
           print('blank line on line '+str(i))
           standard_file = False
        elif line[0] == '#' or line[0] == '%':
           print('comments line on line '+str(i))
           standard_file = False
        i=i+1
     return standard_file 


