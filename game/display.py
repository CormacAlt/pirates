import sys
the_display = None

class Display ():
    pass

def announce(announcement, end='\n', pause = True , types = ""):
    #if(the_display != None):
    #   display stuff
    #else:
    color = sys.stdout.shell
    if(pause):
        end = ''
        color.write(announcement, types)
        input ()
        #input (announcement)
    else:
        color.write(announcement + end, types)

def menu(options):
    #if(the_display != None):
    #   display stuff
    #else:
    chosen = -1
    while chosen < 0 or chosen >= len(options):
        menuletters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(options)):
            if i >= len(menuletters):
                print ("too many options :(")
                break
            print (menuletters[i] + " - " + options[i])
        o = input("Choose: ")
        chosen = menuletters.find(o)
    return chosen
