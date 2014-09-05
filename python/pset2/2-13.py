# Matasano Crypto
# 2-13

from mclib import *



key = '\x11\xa9D\x9ap\x86 h(a@\xd1\xc9\xeb7\x95'

attack_email = "6789ABCDEF" + pad16("admin")
#print attack_email

attack_prf = profile_for(attack_email)

admin_block = attack_prf[16:32]
#print admin_block
#print decrypt_ECB(admin_block, key)


attack_email = "ab@google.com"

attack_prf = profile_for(attack_email)

admin_ctext = attack_prf[:32] + admin_block

#print attack_prf
#print admin_ctext
print '%r' % admin_ctext
print unpad(decrypt_ECB(admin_ctext, key))

#print unpad(decrypt_ECB(attack_prf[0], attack_prf[1]))

