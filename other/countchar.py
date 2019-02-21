def countchar(str):
    str = str.upper()
    output = [0] * 26
    for c in str:
    	if ord(c) >= 65 and ord(c) <= 90:
    		output[ord(c)-65]+=1
    return output

if __name__ == "__main__":
     str = input()
     print(countchar(str))