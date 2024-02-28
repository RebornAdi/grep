def search_in_file(file_name, search_pattern,disp,invert):
    try:
        b=0
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, start=1):
                if (search_pattern in line): 
                    if (disp==2):
                        print(f"Found '{search_pattern}' in {file_name} at line {line_number}: {line.strip()}")
                    b+=1
                if(search_pattern not in line and invert==1):
                    print(f"Not found '{search_pattern}' in {file_name} at line {line_number}: {line.strip()}")
            if(disp==1):
                print(f"Number of lines text exists in is : {b}")
        if(b==0):
            print("None.")
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except Exception as e:
        print(f"An error occurred while processing {file_name}: {str(e)}")

search_pattern=input("Enter the search text : ")
repeat=int(input("Enter the number of files the text to be searched in : "))
i=0
while(i<repeat):
    file_name=input(f"Enter the file{i+1} name : ")
    case_sen=int(input("Case sensitive or not (1 for yes 2 for no): "))
    disp=int(input("Enter 1 for displaying just count of lines or 2 for both count and lines : "))
    invert=int(input("Input 1 for invert match else 2 : "))
    if(case_sen==2):
        search_pattern=search_pattern.casefold()
    search_in_file(file_name,search_pattern,disp,invert)
    i+=1
