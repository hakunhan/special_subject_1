# generate pair of key
import practies.week03.congruence

p = 179
q = 307
e = 5009

def cal_n():
    return p*q

def cal_z():
    return (p-1)*(q-1)

#d = s mod z
def cal_d():
    table = practies.week03.congruence.find_gcd_table(e,cal_z())
    r_s = practies.week03.congruence.get_r_s_calculation(table)

    d = int(r_s[len(r_s)-1][1]) % cal_z()
    return d

# generate public and private key
def generate_keys():
    public_key = [cal_n(), e]
    private_key = [cal_n(), cal_d()]

    return [public_key, private_key]

# convert decimal d to binary calculation
# e.g: d = 53 => d = 2^5 + 2^4 +2^2 + 2^0
def convert_binary_list(d):
    result = []
    bin_d = str(bin(d))

    for i in range(len(bin_d)):
        if (bin_d[i] == '1'):
            result.append(len(bin_d)-1-i)

    return result

# create signature key base on message and sender private key
# m^d mod n = c
def createSignature(message):
    m_list = list(message)
    ascii_m_list = []
    result = []
    for i in range(len(m_list)):
        ascii_m_list.append(ord(m_list[i]))

    for i in range(len(ascii_m_list)):
        encrypt = pow(ascii_m_list[i], generate_keys()[1][1]) % generate_keys()[1][0]
        result.append(encrypt)

    return result

# decrypt signature with sender public key
# c^e mod n = m
def decryptSigature(sig, public_key):
    result = []
    n = public_key[0]
    e = public_key[1]

    bin_list_e = convert_binary_list(e)

    for i in range(len(sig)):
        temp = 1
        for j in range(len(bin_list_e)):
            temp *= (pow(sig[i], pow(2,bin_list_e[j])) % n)
        temp %= n
        result.append(temp)

    return result

# encrypt message with public key of receiver
def encryptMessage(message, public_key):
    m_list = list(message)
    m_ascii_name = []
    n = public_key[0]
    e = public_key[1]

    result = []
    for i in range(len(m_list)):
        m_ascii_name.append(ord(m_list[i]))

    for i in range(len(m_ascii_name)):
        encrypt = pow(m_ascii_name[i], e) % n
        result.append(encrypt)

    return result

# decrypt message with receiver private key
def decryption(message, private_key):
    result = []
    n = private_key[0]
    d = private_key[1]

    bin_list_d = convert_binary_list(d)

    for i in range(len(message)):
        temp = 1
        for j in range(len(bin_list_d)):
            temp *= (pow(message[i], pow(2, bin_list_d[j])) % n) 
        temp %= n
        result.append(temp)

    return result

# revert message from ascii to text
def revert_message(message):
    result = ''
    for i in range (len(message)):
        result += chr(message[i])

    return result

message = [22756,21865,47813,47813,32264]
print(f"Public key: {generate_keys()[0]}, private key: {generate_keys()[1]}")
print(f"Message: {revert_message(decryption(message,generate_keys()[1]))}")
print(f"Encrypted message: {encryptMessage('Sup bro!',[1830497,3119])}")