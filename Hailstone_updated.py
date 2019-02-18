#!/usr/bin/env python
# coding: utf-8

# In[25]:


#outp = ['na']

non_converging = set()
def check_if_seq_increases_by_const_diff(l):
    diff = l[1] - l[0]
    for i in range(2, len(l)):
        if (l[i] - l[i-1]) != diff:
            return False
    return True

def hailstone(x_init, a, b):
    x = x_init
    count = 1
    cur = x
    loop_seq = []
    
    odd_seq = []
    even_seq = []
    while x>0:
        loop_seq.append(x)
        #print(loop_seq)
        # when x is 0 break
        if x == 1:
            if a == 0 and b == 0:
                print('the sequence converged')
                break
        if x == 0:
            print("the sequence converged:")
            break
        if x%2==0:
            x = x/2
            even_seq.append(x)
        else:
            x = a*x + b
            odd_seq.append(x)
        #if x in loop_seq:
            # this converged
            #loop_seq.append(x)
            #print("the sequence converged:")
            #print(loop_seq)
            #if loop_seq not in list_of_seq:
             #   list_of_seq.append(loop_seq)
            #break
        # this conveys that the further value is odd
        if (a%2 == 1 and x%2 == 1) and b%2 == 0:
            # this doesn't converge
            print ("Sequence will not converge")
            break
        if (a%2 == 0) and (b%2 == 1) :
            # this doesn't converge
            print ("Sequence will not converge")
            break
        if len(odd_seq) >= 10 and check_if_seq_increases_by_const_diff(odd_seq):
            # the sequence increases with a constant difference
            print ("Sequence will not converge")
            break
        if len(even_seq) >= 10 and check_if_seq_increases_by_const_diff(even_seq):
            # the sequence increases with a constant difference
            print ("Sequence will not converge")
            break
        if len(odd_seq) > 15 and all(x<y for x, y in zip(odd_seq, odd_seq[1:])):
            # the odd sequence has increased continuously 7 times
            print ("Sequence will not converge")
            break
        if len(even_seq) > 15 and all(x<y for x, y in zip(even_seq, even_seq[1:])):
            # the even sequence has increased continuously 7 times
            print ("Sequence will not converge")
            break   
        if count > 1000:
            print("Sequence will not converge")
            break
        count += 1
    print("No of cycles:" , count)
    outp.append(count)

for x_init in range(1,30):
    for a in range(0,11):
        for b in range(0, 11):
            print("for x:" + str(x_init) + ", for a:" + str(a) + ", and for b:" + str(b))
            hailstone(x_init, a, b)

#print("List of Unique Sequences", list_of_seq)            


# In[ ]:




