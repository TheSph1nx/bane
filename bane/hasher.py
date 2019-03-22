import hashlib,base64
def md5(w):
 '''
   function to return md5 encrypted string
 '''
 return hashlib.md5(w.encode("utf-8")).hexdigest()
def sha1(w): 
 '''
   function to return sha1 encrypted string
 '''
 return hashlib.sha1(w.encode("utf-8")).hexdigest()
def sha256(w):
 '''
   function to return sha256 encrypted string
 '''
 return hashlib.sha256(w.encode("utf-8")).hexdigest()
def base64encode(w):
 '''
   function to return base64 encoded string
 '''
 return base64.b64encode(w)
def base64decode(w):
 '''
   function to return base64 decoded string
 '''
 return base64.b64decode(w)
def sha224(w):
 '''
   function to return sha224 encrypted string
 '''
 return hashlib.sha224(w.encode("utf-8")).hexdigest()
def sha384(w):
 '''
   function to return sha384 encrypted string
 '''
 return hashlib.sha384(w.encode("utf-8")).hexdigest()
def sha512(w):
 '''
   function to return sha512 encrypted string
 '''
 return hashlib.sha512(w.encode("utf-8")).hexdigest()
'''
  the following functions are taking a file path and return ecrypted content of  the file with the defined encryption method in the function's
  name.

  usage:

  >>>import bane
  >>>bane.md5fl('ala.txt')
  '66eab7dfd5c98ca5fbbbda6f7d7b36c3'
'''
def md5fl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= md5(w)
  return s
def sha1fl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= sha1(w)
  return s
def sha224fl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= sha224(w)
  return s
def sha256fl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= sha256(w)
  return s
def sha384fl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= sha384(w)
  return s
def sha512fl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= sha512(w)
  return s
def base64encodefl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= base64encode(w)
  return s
def base64decodefl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= base64decode(w)
  return s
'''
  the following functions are recommanded to be used in bruteforce attacks to crack the hashed passwords.

  they take 2 arguments:

  the first one is a word to encrypt it and compare it to the second argument that takes the hash that you are trying to crack.

  if it returns:
  0 => the hashes didn't match
  1 => the hashes has matched

  example:

  >>>hash='e88e6128e26eeff4daf1f5db07372784'
  >>>l=['admin','12345','user','ala','soul','vince']
  >>>fox word in l:
  ... print'[*]Trying:',word
      if bane.dmd5( word,hash)==1:
       print'[+]Found!!'
       break
      else:
       print'[-]failed'
'''
def dsha224(w,z):
 s=0
 w=hashlib.sha224(w.encode("utf-8")).hexdigest()
 if w==z:
   s+=1
 return s
def dsha384(w,z):
 s=0
 w=hashlib.sha384(w.encode("utf-8")).hexdigest()
 if w==z:
   s+=1
 return s
def dsha512(w,z):
 s=0
 w=hashlib.sha512(w.encode("utf-8")).hexdigest()
 if w==z:
   s+=1
 return s
def dsha256(w,z):
 s=0
 w=hashlib.sha256(w.encode("utf-8")).hexdigest()
 if w==z:
   s+=1
 return s
def dsha1(w,z):
 s=0
 w=hashlib.sha1(w.encode("utf-8")).hexdigest()
 if w==z:
   s+=1
 return s
def dmd5(w,z):
 s=0
 w=hashlib.md5(w.encode("utf-8")).hexdigest()
 if w==z:
   s+=1
 return s
'''
  function to do simple caesar encryption lol.
  
  it takes 2 arguments:

  the first one is the string to encrypt and the second is the second is the encryption key (integer between: 1 and 26)

  example:

  >>> bane.caesar('ala',5)
  'fqf'
'''
def caesar(w,k):
 a='abcdefghijklmnopqrstuvwxyz'
 b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 c=''
 for i in w:
  if (k>26) or (k<1) or (ord(i) not in range(32,127)):
   break
  if (i in a):
   c+=a[(a.index(i)+k)%26]
  elif i in b:
   c+=b[(b.index(i)+k)%26]
  elif ord(i) in range(32,127):
    c+=i
 return c
'''
  function to do simple caesar decryption lol.
  
  it takes 2 arguments:

  the first one is the string to decrypt and the second is the second is the decryption key (integer between: 1 and 26)

  example:

  >>> bane.dcaesar('fqf',5)
  'ala'
'''
def dcaesar(w,k):
 a='abcdefghijklmnopqrstuvwxyz'
 b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 c=''
 for i in w:
  if (k>26) or (k<1) or (ord(i) not in range(32,128)):
   break
  if (i in a):
   c+=a[(a.index(i)-k)%26]
  elif i in b:
   c+=b[(b.index(i)-k)%26]
  elif ord(i) in range(32,128):
    c+=i
 return c