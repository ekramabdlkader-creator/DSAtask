if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        command_line = input().split()
        
    
        command = command_line[0] 
        arguments = command_line[1:]
        
        if command == "insert":
            index = int(arguments[0])
            element = int(arguments[1])
            my_list.insert(index, element)
            
        elif command == "print":
            print(my_list)
            
        elif command == "remove":
            element = int(arguments[0])
            my_list.remove(element)  # FIX 4: Changed .append to .remove
            
        elif command == "append":    # ADDED: You need this block!
            element = int(arguments[0])
            my_list.append(element)
            
        elif command == "sort":
            my_list.sort()
            
        elif command == "pop":
            my_list.pop()
            
        elif command == "reverse":
            my_list.reverse()
