import random
import sys
from ngram_score import ngram_score
#参数初始化
ciphertext ='UNGLCKVVPGTLVDKBPNEWNLMGVMTTLTAZXKIMJMBBANTLCMOMVTNAAMILVTMCGTHMKQTLBMVCMXPIAMTLBMVGLTCKAUILEDMGPVLDHGOMIZWNLMGBZLGKSMAZBMKOMKTWNLMGBZKTLCKAMHMIMDMVGBZLXBLCSAZTBMMOMTVPGMOMVKJLTQPXCBPNEJLBBLUILVDKJKZ'
parentkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#只是用来声明key是个字典
key = {'A':'A'}
#读取quadgram statistics
fitness = ngram_score('quadgrams.txt')
parentscore = -99e9
maxscore = -99e9
'''
print('---------------------------start---------------------------')
j=0
while 1:
    j=j+1
    #随机打乱key中的元素
    random.shuffle(parentkey)
    #将密钥做成字典
    #密文:明文
    for i in range(len(parentkey)):
        key[parentkey[i]] = chr(ord('A')+i)
    #用字典一一映射解密
    decipher = ciphertext
    for i in range(len(decipher)):
        decipher = decipher[:i]+key[decipher[i]]+decipher[i+1:]
    parentscore = fitness.score(decipher)#计算适应度
    #在当前密钥下随机交换两个密钥的元素从而寻找是否有更优的解
    count = 0
    while count < 2000:
        a = random.randint(0,25)
        b = random.randint(0,25)
        #随机交换父密钥中的两个元素生成子密钥，并用其进行解密
        parentkey[a],parentkey[b]= parentkey[b],parentkey[a]
        key[parentkey[a]],key[parentkey[b]] = key[parentkey[b]],key[parentkey[a]]
        decipher = ciphertext
        for i in range(len(decipher)):
            decipher = decipher[:i]+key[decipher[i]]+decipher[i+1:]
        score = fitness.score(decipher)
        #此子密钥代替其对应的父密钥，提高明文适应度
        if score > parentscore:
            parentscore = score
            count=0
        else:
            #还原
            parentkey[a],parentkey[b]=parentkey[b],parentkey[a]
            key[parentkey[a]],key[parentkey[b]]=key[parentkey[b]],key[parentkey[a]]
            count +=1
    #输出该key和明文
    if parentscore > maxscore:
        maxscore = parentscore
        print ('Currrent key: '+''.join(parentkey))
        print ('Iteration total:', j)
        decipher = ciphertext
        for i in range(len(decipher)):
            decipher = decipher[:i]+key[decipher[i]]+decipher[i+1:]
        print ('Plaintext: ', decipher.lower(),maxscore)
        sys.stdout.flush()
'''
#维吉尼亚密码加密示例
ciphertext ='YRAAHYHBIUWGRWBYCHCMHKXKUVRQNFSPWULNRMPQYHBMQDWKLNMBJCKUOEJENVLDYLPWCLDAYOUFQOXFAFVLCRMPVZQQQMNSDLCIPWPCHDLYJWKLPKMZQRQQMTAAVDMLYJQVWYVCOHRUDMUEZCWOPJPVVJSVJEZFYOCMQWWLRETAHFDNHYZSRGVMLAHFWRIJKJVLRSNAWKZSPJXSKHXXFKIJDXHWAOIV'
#将字母c减密钥m，变成明文
def sub(c,m):
    return chr((ord(c)-ord('A')-m)%26+ord('A'))
#假设维吉尼亚密码密钥长度为k
k=7
#解密密钥初始为[0,1,2,3,4,5,6]
# key=list(range(k))
key = [0,0,0,0,0,0,0]
#更改初试密钥为[1,1,2,3,4,5,6]
# key[0]=1
#解密
decipher = ciphertext
'''
for i in range(len(decipher)):
    decipher = decipher[:i]+sub(decipher[i],key[i%k])+decipher[i+1:]
'''
score = 0
j = 0
'''
while 1:
    j+=1
    for i in range(7):
        key[i] = random.randint(0,25)

    for i in range(len(decipher)):
        decipher = decipher[:i]+sub(decipher[i],key[i%k])+decipher[i+1:]

    score = fitness.score(decipher)
    if score>=maxscore:
        maxscore = score
        print ('Currrent key: ', (key))
        print('TEXT: '+ decipher)
        print ('Iteration total:', j)
        decipher = ciphertext
'''

for num in range(7):
    key[num] = 0
    score_list = []
    while key[num]<=25:
        decipher = ciphertext
        for i in range(len(decipher)):
            decipher = decipher[:i]+sub(decipher[i],key[i%k])+decipher[i+1:]
        score_list.append(fitness.score(decipher))
        key[num] += 1

    key[num] = score_list.index(max(score_list))

decipher = ciphertext

for i in range(len(decipher)):
    decipher = decipher[:i]+sub(decipher[i],key[i%k])+decipher[i+1:]

print(decipher.lower())



        
        

'''
#3*3hill密码加解密示例
ciphertext0 ='RYLLAFFSOJJEYVSBYWGDEEKCKUISULIEFVXVZKHBXMVPHMIBQJZSEIXTMNUUIOHPGVFFVYTSUNUWSGLJTVPMXSGWMDJJEZRZIEEBHLTJFDFFXVJOCOJGNQJZVOUGMXHEQBCTVWZBHLGGSTRCSKUGDEIJMWYGJWCFSVVWZJALXZRSVYHAFTDDYJUXNCNBUBZXFFVYTSTGATRPTMWHQCCAMTIZPEMPDZDWRZRZIEEBHLKPINJRSLUTBTSYINEKOJAFOERKILRENTCTFZWHIBDJWSRDOPFYVHFREQYOJAVUCXGLHAIXMIAQZVEOCBTDSAJRWYQIBPZFDQKZGTAOQGXAJCLLIVUZOHMJMYNOHBWGIEFJHIPEMPBGNTCBZXFFVYTSCOWYPPPEMLYYLJKMOMIEFQSNKSHVOHKNRXVJNBUBZXWQEBATQBTVXQCBYPGYHHTTKEXYKJGOSYIKPIPDHZRZIEETMTOAOQQXBSTXCJLUETMTOAOQQXWSRMSRJFWEQWZKHWZFNPVFPFWSSECRDFLETYSWXFIWVUZAGZGBYTTSHIAHFREQYXCJLUEBHLLLYBSWNXFMKUEQLZZUQIWSIHNDOPPEBRYMBGIEFCTKIGBBTOXNFWWBPDHXUAQYPHNVWSSRWWBHZJCGSUYHWMLZJPGYLCJMMBBZDVPHKDCLIQUPXWRWNXIHIAHUCNYMBSHIEFDTZTAOZJLJLZRHHXKOXGLHAIGOTNBHVXQMDWBPZUTGZMMXKWJGSHTWRGRBYARYLBXMJLZZQWHFXDITLRVWDGJTWMHWBVTWSGVSBZJLJLZVPHMPSBYEJLZXKOXGLHAIAUDIEFRKINTCCUEFGPCXSTAOVVLFSOMPSBZXQANLVIEGMTFBFSOSWXFIWPSKKAMTVZWGOHHEZESJGNYERWSRLCJGWYVPHJGSHTWRGRCRAXNCNISJVMJFKWESQDOGRABTXLAAXTMBZXCJYHIADWPWSXXYXJDIXNCNTCZOJXKOTWIDBVGOPWSRLJTYJGZTICXSWSRUPXMLOTMWNWWQGLFIHVBZNLIHFRURQWPEHFKVHZMWRBOKIZWSZLNGCTKKEOTZJYVJUDFFKVWHTLTHENMCTRIVKIKNPNMCTRIAPQNLIPDHXTFUTGQANLVIIWMKNP'
R = Zmod(26)
MR = MatrixSpace(R,3,3)
key = MR()
vcode=[0]*(len(ciphertext0)//3)
dic={}
'''
'''
#密文转化成数字
for i in range(len(ciphertext0)//3):
    vcode[i]=vector([R(ord(ciphertext0[3*i])-ord('A')),R(ord(ciphertext0[3*i+1])-ord('A')),R(ord(ciphertext0[3*i+2])-ord('A'))])

#数字转化成密文
for i in range(26):
    dic[R(i)]=chr(ord('A')+i)

#给密钥赋值
for i in range(3):
    for j in range(3):
        key[i,j]=R(randint(0,25))
#hill加密/解密
def hill(ciphertext):
    cipher=''
    for i in range(len(ciphertext)//3):
        v = vcode[i]*key
        cipher = cipher+dic[v[0]]+dic[v[1]]+dic[v[2]]
    return cipher

for i in range(26):
    dic[R(i)]=chr(ord('A')+i)

for i in range(len(ciphertext0)//3):
    vcode[i]=vector([R(ord(ciphertext0[3*i])-ord('A')),R(ord(ciphertext0[3*i+1])-ord('A')),R(ord(ciphertext0[3*i+2])-ord('A'))])

for i in range(3):
    for j in range(3):
        key[i,j]=R(randint(0,25))

for i in range(3):
    score_list = []
    set_list = []
    count = 0
    for j in range(3):
        for t in range(26):
            count += 1
            key[i, j] = t
            ciphertext = ciphertext0
            ciphertext = hill(ciphertext)
            score_list.append(fitness.score(ciphertext))
            set_list.append(key[i])

    key[i] = set_list.index(max(score_list))

ciphertext = ciphertext0
ciphertext = hill(ciphertext)
print(ciphertext)



        

# 6 23 22
# 18 8 17
# 11 5 4
'''