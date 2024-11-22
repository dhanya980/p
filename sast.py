while True:
 print("\nHash operations 1.Insert 2.Search 3.Display 4.Quit") 
 ch=int(input("Enter your choice:"))
 if ch == 1:
   key=int(input("Enter key to be inserted:")) 
   hsh.insert(key)
 elif ch == 2:
    key=int(input("\nEnter key to be searched:")) 
    hsh.search(key)
 elif ch == 3: 
    hsh.display()
 else:
    break

