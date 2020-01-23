## This program would read a text file passed as argument and would extract each word
## in the file and would convert to uppercase and check the number of repetitions of the word
#history
#date          version               particulars
#22-jan-20      1.0                  First
#23-jan-20      1.1                  Included try catch
import sys
import os
import datetime

def main():
    print(str(datetime.datetime.now())+":Initialising the variables")
    inp_file = sys.argv[1]
    out_file = inp_file.split(".")[0]+"_out.csv"
    exitStat=0
    if not os.path.isfile(inp_file):
        print(str(datetime.datetime.now())+":File{} doesnt exist. ".format(inp_file))
        sys.exit()

    bucket = {}
    print(str(datetime.datetime.now())+":Opening the file for reading")
    try:
        with open(inp_file) as f:
                cnt = 0
                for line in f:
                    word_list=line.strip().split(' ')
                    # calling word_count to check the occurence of each word, pass dummy list to store the word and count
                    word_count(word_list, bucket)
                    cnt += 1
        print(str(datetime.datetime.now())+":Read the contents and written to List")
    except:
        print(str(datetime.datetime.now())+":unable to open/read the file")
    # open output csv file for writing
    print(str(datetime.datetime.now())+":Writing the contents to output file")
    try:
        with open(out_file,'w') as csvfile:
                    csvfile.write("Words,Count\n")
                    for k,v in bucket.items():
                        #write header to csv and followed by Word and its count
                        print("Word %s : Count  %s " % (k, v))
                        newline = str(k)+","+str(v)+""+"\n"
                        csvfile.write(newline)
        print(str(datetime.datetime.now())+":Output file%s created"% out_file)
    except:
        print(str(datetime.datetime.now())+":unable to write the output file")

def word_count(words, bucket):
    try:
        for word in words:
            if word != '':
                if word.upper() in bucket:
                    bucket[word.upper()] += 1
                else:
                    bucket[word.upper()] = 1
    except:
        print(str(datetime.datetime.now())+":unable to add the words to the bucket")

if __name__ == '__main__':
    print(str(datetime.datetime.now()) + ":The program started")
    main()
    print(str(datetime.datetime.now()) + ":The program ended successfully")
