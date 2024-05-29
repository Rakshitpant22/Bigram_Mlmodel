words=open("names.txt",'r').read().splitlines()  # read the contents of a file and split it into a list of lines
print(words[:10])

b={}
for w in words:
    chrs=['<S>']+ list(w) +['<E']
    for ch1,ch2 in zip(chrs,chrs[1:]):
        bigram=(ch1,ch2)
        b[bigram]=b.get(bigram,0)+1;
      #  print(ch1,ch2);

#print(b)  # it basicically give a dictionary of all bigrams and their freq

increasing=sorted(b.items(),key=lambda kv:kv[1]) #sorting done by 1st key but here we need on freq so lambdaq func is written
decreasing=sorted(b.items(),key=lambda kv:-kv[1])
print(decreasing)


# for storing this information in 2d array instead of dictionary
# for this we can use tenserflow or pytorch here doing with pytorch
import torch
N=torch.zeros((27,27),dtype=torch.int32)

chars= sorted(list(set(''.join(words))))
stoi = {s:i+1 for i,s in enumerate(chars)}  # mapping char to integer
stoi['.']=0

itos={i:s for s,i in stoi.items()} #reverse mapping

for w in words:
    chrs=['.']+ list(w) +['.']
    for ch1,ch2 in zip(chrs,chrs[1:]):
        ix1=stoi[ch1]
        ix2=stoi[ch2]
        N[ix1,ix2]+=1
#print(N)

import matplotlib.pyplot as plt
#matplotlib inline
plt.figure(figsize=(20,20))
plt.imshow(N,cmap='Reds')
for i in range(27):
    for j in range(27):
        chrs=itos[i]+itos[j]
        plt.text(j,i,chrs,ha="center",va="top",color="gray")
        plt.text(j,i,N[i,j].item(), ha="center",va="bottom", color="gray")
plt.axis('off')

#plt.show()

# we want to create freq into probabilities for 1st row
# p= N[0].float()
# p=p/p.sum()

# we now sample from the distribution from TORCH.MULTINOMIAL
# we have a list of probabilities corresponding to each name. These probabilities should sum to 1.
# For simplicity, we can generate random probabilities and normalize them.

p= N[0].float() #p is for 1st row bigram
#print("Random",p)   # without normalization
p= p/p.sum()   #normalized probabilities
#print("Normalised:",p)

g=torch.Generator().manual_seed(2147483647)
p=torch.rand(3,generator=g) # taking random 3 bigrams from N[0]
print(p)
x=torch.multinomial(p, num_samples=10, replacement=True, generator=g) # sampling using pytorch.multinomial function
print(x,"Sampling data on basis of normalised probability") # Index with most normalised prob will be seen more


index=torch.multinomial(p,num_samples=1,replacement=True,generator=g).item()
print(itos[index])dddere44




