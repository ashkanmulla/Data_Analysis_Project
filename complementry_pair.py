def complementry_pair(sample_array_1,sample_array_2,k):
    print(sample_array_1)
    print(sample_array_2)
    try:
        pairs  =[]
        for i in sample_array_1:
            #print("i is",i)
            for j in sample_array_2:
                #print("j is,",j)
                x = i + j 
                #print("x is",x)
                if i!=j and x==k:
                   # print("in 3rd loop")
                    pairs.append({i,j})
                    #print(pairs)
                j+=1
            i+=1
        return pairs 
    except Exception as e:
        print(e)
sample_array_1_1= [7,8,4,2,6] 
sample_array_2_2= [5,6,4,9,10,6]

k_1= 12
pairs = complementry_pair(sample_array_1_1,sample_array_2_2,k_1)
print(pairs)
    
        
        
        
            
    


