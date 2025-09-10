#list is a data structure which has multiple values
#array -> data structure which can hol multiple values of same type
list_of_clouds = ["aws","azure","gcp","digital ocean","oracle","utho"]#aws is at thw 0th inddex place
cloud = "gcp" #vriable
print(list_of_clouds)

#add a new cloud salesforce

list_of_clouds.append("salesforce")
list_of_clouds.append("amazon") #added to theend of list
print(list_of_clouds)

list_of_clouds.insert( 3,"alibaba")
print(list_of_clouds)

print(len(list_of_clouds))
#using loop for iteration

for clouds in list_of_clouds:
    print(" ") # for blank line after every word
    print (clouds)

    for i in range(0,10):
        print ("hello guys")#want to repeat the word as per ypur choice for how many times