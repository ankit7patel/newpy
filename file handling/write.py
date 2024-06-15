f = open ("n1.text", "w")    # write mode m hai add krega  value ko over write krta hai 
f.write("mt name is ankittt\n")


f = open ("n1.text", "a")    # appen mode m hai data ko last me add krta hai 
f.write("mt name is ankittt\n")

f = open ("n1.text", "a")  
f.write("--------This is python -------")


data=("myname is ankittt\n","my age 22\n")
f.writelines(data)
print(f.write())