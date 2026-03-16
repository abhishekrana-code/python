# print("hello world");
# print("hello\"world\"");
# print("hello'world'");
# c="hello";
# t=c.upper();
# print(t.isupper());
# print(t.lower().isupper()  );
# print(len(t));#length of string
# print(t[0]);    #indexing
# print(t[0:3]);  #slicing
# print(t.index("L")); #index of first occurrence of L
a=5;
print("The value of a is",a);#comma separated values
print("The value of a is "+str(a));#string concatenation
print(f"The value of a is {a}");#f-string

name=input("Enter your name: ");#input function takes input from user and returns it as string
print(f"Hello {name}");