import random
import string
import argparse

def genKey():
    ran_int = random.randint(4,8)
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, ran_int))
    return ran_str

def genTestfile(file_out, num):
    li = []

    for i in range(num):
        op = random.randint(0,8)
        if((op >= 3 and op <= 6) or op == 8):
            if(len(li) == 0):
                continue
        if(op <= 2):
            value = random.randint(-100000,100000)
            key = genKey()
            if(li.count(key) == 0):
                li.append(key)
            file_out.write("set {} {}\n".format(key, value))
        elif(op <= 3):
            value = random.randint(-100000,100000)
            key = random.choice(li) 
            file_out.write("set {} {}\n".format(key, value))
        elif(op <= 6):
            value = random.randint(-100000,100000)
            key = random.choice(li) 
            file_out.write("get {} {}\n".format(key, value))   
        elif(op <= 7):
            value = random.randint(-100000,100000)
            key = genKey()
            file_out.write("get {} {}\n".format(key, value))
        else:
            value = random.randint(-100000,100000)
            key = random.choice(li) 
            li.remove(key)
            file_out.write("delete {}\n".format(key))
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser()  
    parser.add_argument("--output", type=str, default='./testcase/test.in',help="Output file")
    parser.add_argument("--num", type=str, default= '100000',help="Number of operations")
    args = parser.parse_args()
    with open("%s" % args.output, 'w', newline='') as file_out:
        genTestfile(file_out, int(args.num))
