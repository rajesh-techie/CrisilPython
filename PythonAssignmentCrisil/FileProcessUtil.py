## This program would read a text file passed as argument and would extract each word
## in the file and would convert to uppercase and check the number of repetitions of the word
import sys
import os

def main():
    inp_file = sys.argv[1]
    out_file = inp_file.split(".")[0]+"_out.csv"
    exitStat=0
    if not os.path.isfile(inp_file):
        print("File{} doesnt exist. ".format(inp_file))
        sys.exit()

    bucket = {}
    with open(inp_file) as f:
        cnt = 0
        for line in f:
            # print("line {} contents {}".format(cnt+1, line))
            word_list=line.strip().split(' ')
            # calling word_count to check the occurence of each word, pass dummy list to store the word and count
            word_count(word_list, bucket)
            cnt += 1
            # open csv file for writing
        with open(out_file,'w') as csvfile:
            csvfile.write("Words,Count\n")
            for k,v in bucket.items():
                #write header to csv and followed by Word and its count
                print("Word %s : Count  %s " % (k, v))
                newline = str(k)+","+str(v)+""+"\n"
                csvfile.write(newline)
    print("Output file%s created"% out_file)

def word_count(words, bucket):
    for word in words:
        if word != '':
            if word.upper() in bucket:
                bucket[word.upper()] += 1
            else:
                bucket[word.upper()] = 1


if __name__ == '__main__':
    main()