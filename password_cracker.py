import hashlib


pwlist = open("top-10000-passwords.txt", "r").readlines()
salts = open("known-salts.txt", "r").readlines()

def crack_sha1_hash(hash, use_salts = False):


  if use_salts:
    for salt in salts:
      for toppw in pwlist:
        toppw_prepended_salt = str(salt).strip() + str(toppw).strip()
        topppw_appended_salt = str(toppw).strip() + str(salt).strip()

        hash_object_prepended_salt = hashlib.sha1(str(toppw_prepended_salt).strip().encode('utf-8'))
        hash_object_appended_salt = hashlib.sha1(str(topppw_appended_salt).strip().encode('utf-8'))

        pbHasht_prepended_salt = hash_object_prepended_salt.hexdigest()
        pbHash_appended_salt = hash_object_appended_salt.hexdigest()

        if pbHasht_prepended_salt == hash or pbHash_appended_salt == hash:
          return toppw.strip()



  else:
      for toppw in pwlist:
        hash_object = hashlib.sha1(str(toppw).strip().encode('utf-8'))
        pbHash = hash_object.hexdigest()
        
        if pbHash == hash:
          return toppw.strip()
  
  
  return "PASSWORD NOT IN DATABASE"
    