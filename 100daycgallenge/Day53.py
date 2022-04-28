str1="Race"
str2='Cares'

str1=str1.lower()
str2=str2.lower()
if (len(str1)==len(str2)):

    sorted_srt1=sorted(str1)
    sorted_srt2=sorted(str2)

    if(sorted_srt1 == sorted_srt2):
        print(str1 +' and '+ str2 +  ' are  anagram')
    else:
        print(str1 + ' and '+ str2 + ' are not anagram')

else:
    print(str1 +' and ' + "are not anagram")

    