with open("in.txt","r",encoding='utf-8') as f:
    content = f.read().split("\n")
print("Reading file succeeded !!!")
content[0] = '## '+ content[0]
content[1:5] = '\n'
flag = False
flag2 = True
i = 1
while i < len(content):
    if (len(content[i]) >= 5 and ( content[i][:5] == 'input' or content[i][:5] == 'Input' )):
        if( 'Copy' in content[i]):
            content[i] = '## '+ content[i][:-4]
            if flag:
                content.insert(i,'```')
                content.insert(i+2,'```cpp')
                i += 2
            else:
                flag = True
                content.insert(i+1,'```cpp')
                i += 1
        else:
            content[i] = '## '+ content[i]
    elif (len(content[i]) >= 6 and ( content[i][:6] == 'output' or content[i][:6] == 'Output' )):
        if( 'Copy' in content[i]):
            content[i] = '## '+ content[i][:-4]
            content.insert(i,'```')
            content.insert(i+2,'```cpp')
            i += 2
        else:
            content[i] = '## '+ content[i]
    elif (len(content[i]) >= 8 and ( content[i][:8] == 'Examples' or content[i][:8] == 'examples' )):
        content[i] = '## '+ content[i]
    elif (len(content[i]) >= 4 and ( content[i][:4] == 'Note' or content[i][:4] == 'note')):
        flag2 = False
        content[i] = '## '+ content[i]
        content.insert(i,'```')
        i += 1
    i += 1
if flag2:  
    content.append('```')
content.append("\n")
content.append("\n")
content.append("## 解题思路：")
content.append("\n")
content.append("\n")
content.append("## AC代码：")
content.append("\n")
content.append('```cpp')
content.append("\n")
content.append("\n")
content.append('```')
content.append("\n")
with open("out.txt","w",encoding='utf-8') as f:
    for i in content:
        f.write(i)
        f.write('\n')
print("Writing file secceeded !!!")
print("Process ended ! ^_^ ~~")
tmp = input("Press any key to quit.")
