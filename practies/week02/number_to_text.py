#convert number to text in Vietnamese (maximum of hundred billion)
#e.g. 452341 -> "bốn trăm năm mươi hai ngàn ba trăm bốn mươi mốt

#dictionary for converting number to text
NUM_TO_TEXT = {
    '0' : 'không',
    '1' : 'một',
    '2' : 'hai',
    '3' : 'ba',
    '4' : 'bốn',
    '5' : 'năm',
    '6' : 'sáu',
    '7' : 'bảy',
    '8' : 'tám',
    '9' : 'chín'
}

VIETNAM_NUM_UNIT = ['tỉ', 'triệu', 'ngàn']

#convert input number to format 12 character numeric string
#e.g. 123 -> '000000000123'
def num_to_format_str(num):
    result = '{:0>12}'.format(num)
    return result

#get the valid number according to the number format
def getValidNumber():
    number = int(input("Enter number need to convert to text in Vietnamese"
                       "(maximum of hundred billion): "))
    if number >= 1000000000000 or number < 0:
        print("Invalid input!")
        getValidNumber()

    return number

#converting numeric string to Vietnamese text
def convert(num):
    result = ''
    isTy = False
    isTrieu = False
    isNgan = False
    isKhongTram = False

    for i in range(12 - len(num), 12):
        isTram = False
        isMuoi = False
        isLe = False
        isMot = False

        #if number in hundred is 0 and the number before and after is not 0
        #e.g. 202020 -> "hai trăm lẻ hai ngàn không trăm hai mươi"
        if(i in [3,6,9] and num[i] == '0' and (num[i-1] != '0' or num[i-2] != '0') and num[i+1] != '0'):
            isKhongTram = True

        #skip if current number is 0
        if (num[i] == '0'):
            continue

        #check if the number reach billion
        if(i>=0 and i<=2 and num[i] != '0'):
            isTy = True

        #check if the number reach million
        #and if the number reach billion
        #       add "tỷ" to the text
        if(i>=3 and i<=5 and num[i] != '0'):
            if(isTy):
                result += "tỷ" + " "
                isTy = False

            isTrieu = True

        # check if the number reach thousand
        # and if the number reach million
        #       add "triệu" to the text
        if(i>=6 and i<=8 and num[i] != '0'):
            if (isTrieu):
                result += "triệu" + " "
                isTrieu = False

            isNgan = True

        #if the number reach million
        #   add "ngàn" to the text
        if(i>=9 and i <=11 and num[i] != '0'):
            if(isNgan):
                result += "ngàn" + " "
                isNgan = False

        #if the in position 0,3,6,9 of the number != 0
        #   isTram = True
        #e.g. 100 -> "một trăm"
        if(i in [0,3,6,9] and num[i] != '0'):
            isTram = True

        #if current number is isKhongTram
        #   add "không trăm" to the text
        if (isKhongTram):
            result += "không trăm" + " "
            isKhongTram = False

        #if the in position 1,4,7,10 of the number != 0
        #   if current number = '1'
        #       add "mười" to the text and end this current iteration
        #       e.g. 10 -> "mười"
        #   else
        #       isMuoi = True
        if (i in [1, 4, 7, 10] and num[i] != '0'):
            if(num[i] == '1'):
                result += 'mười' + ' '
                continue

            else:
                isMuoi = True

        # if the in position 2,5,8,11 of the number != 0
        #   if the number before current number = 0 and the number before that number != 0
        #       isLe = True
        #   elif the number before current number != 0 and !=1
        #       isMot = True
        if (i in [2, 5, 8, 11] and num[i] != '0'):
            if((num[i-1] == '0') and (num[i-2] != '0' or num[i-3] != '0')):
                isLe = True
            elif(num[i-1] != '0' and num[i-1] != '1'):
                isMot = True

        #if isLe is True
        #   add "lẻ" to text
        if(isLe):
            result += "lẻ" + " "

        # if isMot is True
        #   add "mốt" to text
        if(isMot):
            result += "mốt" + " "
            continue

        #add number to text find in dictionary to the converting text
        result += NUM_TO_TEXT[num[i]] + " "

        # if isTram is True
        #   add "trăm" to text
        if(isTram):
            result += "trăm" + " "

        # if isMuoi is True
        #   add "mươi" to text
        if(isMuoi):
            result += "mươi" + " "

    #in case of all number following the number that != 0 are = 0
    #check if isTy, isTrieu, isNgan to add to the text
    if(isTy):
        result += "tỷ" + " "
        isTy = False
    if(isTrieu):
        result += "triệu" + " "
        isTrieu = False
    if(isNgan):
        result += "ngàn" + " "
        isNgan = False

    return result

def main():
    print(convert(num_to_format_str(getValidNumber())))

main()