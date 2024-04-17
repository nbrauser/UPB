# with open('write_test.txt', 'w') as file_obj:
#   file_obj.write('Writing)

with open('sample_text', 'r') as read_obj:
    with open('sample_text_copy', 'a') as write_obj:
        write_obj.write("\n" + 'Rewriting again and again and agian')
        #for line in read_obj:
        #    write_obj.write(line)
# csv. excel --> pandas