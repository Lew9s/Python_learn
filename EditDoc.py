def insert_line(lines):
    lines.insert(0,'Blowing in the wind\n')
    lines.insert(1,'Bob Dylan\n')
    lines.append('1962 by Warner Bros.lnc.')
    return''.join(lines)
with open('d:\\Python\\try\\Blowing in the wind.txt','r+') as f:
    lines = f.readlines()
    string = insert_line(lines)
    print(string)
    f.seek(0)
    f.write(string)
    
