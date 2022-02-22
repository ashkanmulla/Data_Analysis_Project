import os
path = r'C:\Users\aksha\Desktop\Data_Analyst\text_files'
def text_file_count(path):
    os.chdir(path)
    count = 0 
    try:
        for root,dirs,files in os.walk(path):
            for file in files:
                if file.endswith(".txt"):
                    # print("am in if")
                    count+=1
        #print(count)
        return count
    except Exception as e:
        print(e)
count=text_file_count(path)
print(count)
