 
import numpy as np
import matplotlib.pyplot as plt 
#import torch
import datetime

#time between keys for anayliss
# pytorch


def main():
    file = open('study/keyfile.txt','r')
    dict_logger = dict()
    time_dict = dict()
    list_of_times = []
    first_line = file.readline()# letters only on the first line
    list_of_chars_i_guess = []
    f_me = []
    for line in file:
        line_list = line.split()
        f_me.append(line_list)
    f_me = f_me[:-1]
    for line_list in f_me:
        #timestamp__  = line[0]
        print(line_list)
        char = line_list[0][0]
        
        the_3rd = line_list[1]
        
        dict_logger[char] =  dict_logger.get(char,0) +1
        #time_dict[timestamp__] = time_dict.get(timestamp__, 0) +1
        
        list_of_chars_i_guess.append(the_3rd)
        
        
    file.close()    
    #print("aaaa", list_of_chars_i_guess)
    
    #times = list(time_dict.keys())
    #counts_times = list(time_dict.values())
    
    keys = list(dict_logger.keys()) #mpl only works with lists
    n_values = list(dict_logger.values())#mpl only works with lists
    
    fig = plt.figure(figsize = (26, 30)) 
    
    plt.bar(keys, n_values, color ='maroon', width = 0.4)# letters 
    
    plt.xlabel("Keys")
    plt.ylabel("Number of Presses")
    plt.title("Frequency of Key Presses")
    plt.xticks(rotation=90)
    
    plt.show()

    #for timestapms -----<>------
    delta_list = []
    new_time_list = []
    for time__stamp in list_of_chars_i_guess:#gets timestamps form dict as a list
        
        time_now_2 = datetime.datetime.fromtimestamp(float(time__stamp))# I do not understand this
        readable_time = time_now_2.strftime("%H:%M:%S.%f")# I do not understand this
        new_time_list.append(str(readable_time))
        

    #print("New Time list: ",new_time_list)
    n_ber=0
    print("lengss", len(list_of_chars_i_guess))
    for time__stamp in list_of_chars_i_guess:
        n_ber += 1
        
        if n_ber < len(list_of_chars_i_guess):
            delta = float(list_of_chars_i_guess[n_ber]) - float(time__stamp) 
            delta_list.append(int(delta))
            
    delta_list.append(0)
    fig = plt.figure(figsize=(2^15, 30)) #times
    
    #print(len(new_time_list), "god",len(delta_list))
    plt.bar(new_time_list, delta_list, color='maroon', width=0.4)
    
    plt.xlabel("Time of Press")
    plt.ylabel("Lengeth of Time in Seconds")
    plt.title("Frequency of Key Presses Over Time")
    plt.xticks(rotation=90)  # Rotate 
    plt.tight_layout()  # Adjust layout, but idk
    plt.show()


    

if __name__ == "__main__":
    main()