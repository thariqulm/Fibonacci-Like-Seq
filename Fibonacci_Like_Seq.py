from sympy import *
p=float(input("Enter two numbers p & q to generate the sequence as follow \n f(n)= p*f(n-1) + q*f(n-2) \n 3rd num in Seq = p x 2nd num in Seq + q x 1st num in Seq\n p = "))
q=float(input(" q = "))
n=int(input("\nEnter the no.of terms to be generated \n n = "))
f1=int(input("\nEnter the first two numbers in the sequence \n f(1) = "))
f2=int(input(" f(2) = "))
f0=(f2-f1*p)/q
z=(1/(p**2+4*q)**0.5)
Alpha=((p+(p**2+4*q)**0.5)/2)
print("\nThe following two ratios Alpha & Beta are obtained by the quadratic formula")
print("Alpha = %s"%Alpha)
Beta=((p-(p**2+4*q)**0.5)/2)
print("Beta = %s"%Beta)
print("\nThe first %s numbers of sequence created using the above ratios are "%n)
for i in range(1,n+1):
  num=z*((Alpha**i)*(f1-f0*Beta)+(Beta**i)*(f0*Alpha-f1))
  print("%s rounded off to "%num,end="")
  print(round(num))
print("\nThe above sequence is generated by the formula")
Alpha, Beta, f0, f1, n = symbols('(Alpha) (Beta) f(0) f(1) n', integer=True)
#pprint(Pow(sqrt(Pow(p,2)+4*q),-1)*(-Pow((p-sqrt(Pow(p,2)+4*q))/2,n)+Pow((p+sqrt(Pow(p,2)+4*q))/2,n)))
#print("\n      or      \n")
pprint((Pow(Alpha,n)*(f1-f0*Beta)+Pow(Beta,n)*(f0*Alpha-f1))/(Alpha-Beta))
print(" Where f(0)->Zeroth num in seq")