#Fibonacci

user = int(input("Números de termos da sequência de Fibonacci que você deseja printar: \nfn = "))

prevfn = 0
fn = 1
nextfn = 0
index = 0

while index < user:
    prevfn = fn
    fn = nextfn
    nextfn = (fn + (prevfn))
    print("f{} = {}".format(index, fn))
    index += 1
print("Fim.")
