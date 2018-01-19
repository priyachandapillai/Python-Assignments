#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 09:03:34 2017

@author: PriyaChandapillai
"""
a="hello world"
print(a.capitalize())#makes first alphabet uppercase
print(a.center(20,"*"))#center
print(a.ljust(20,"*"))#ljust
print(a.rjust(20,"*"))#rjust
print(a.count("o"))#count
print(a.count("o",5,10))
print(a.count("sf"))
print(a.encode("UTF-8",errors="strict"))#encode
print(a.encode("UTF-32",errors="strict"))
b=a.encode("UTF-32",errors="strict")
print(b)
print(b.decode("UTF-32",errors="strcit"))#decode
print(a.endswith("world"))
print(a.startswith("hello"))
print(a.startswith("llo"))
#expandtab
str="hey \t python"
print(str.expandtabs(20))

#find
print(a.find("r"))
print(a.find("r",5,10))
print(a.find("re"))

#index
print(a.index("re"))
print(a.index("re",5,10))

#isalnum
b="pass123"# true
print(b.isalnum())
b="pass123@" #false because of special char
print(b.isalnum())
b="123" #true
print(b.isalnum())

#isalpha
b="pass123"
print(b.isalpha())
b="pass"
print(b.isalpha())

#islower
b="hello"
print(b.islower)

#isdigit
a="123"
print(a.isdigit())

a="abg123"
print(a.isdigit())

#isnumeric
a="12344"
print(a.isnumeric())

#join
a=["hello","world","python"]
b="-"
b.join(a)

a=["hello","world","python"]
c="hello world and python"
b="-"
b.join(c)
len(c)
c="  hello"
print(c.strip())
c="  hello"
print(c.rstrip())

#encrypt
secret_key="abcdefghijklmnopqrstuvwxyz"
encrypt="!@#$%^&*()_+1234567890}{><"
a="abc"
encrypted_table="".maketrans(secret_key,encrypt)
enc_text=a.translate(encrypted_table)
print(enc_text)
#decryption
decrypted_table="".maketrans(encrypt,secret_key)
decrypted_str=enc_text.translate(decrypted_table)
print(decrypted_str)

#max
print(max("hello","python","world"))
print(min("hello","python","world"))

#replace
a="hello python"
a=a.replace("python","world")
print(a)

a="hello python python"
a=a.replace("python","world",1)#overriding therefore a=a.replace i.e string is immutable
print(a)

a="hello python"
a=a.replace("python","world")
print(a.swapcase())

a="hello python"
a=a.replace("python","world")
print(a.title())


