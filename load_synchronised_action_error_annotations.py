import csv
import os

# set working directory (change below working directory)
tmp_current_working_directory_path = '/media/eve/DATA2/Young/Tent_Dataset/TENT_DATA/data'
os.chdir(tmp_current_working_directory_path)


Action_annotation = {0:'assemble support',   1:'insert stake',           2:'insert support',         3:'insert support tab',
                     4:'instruction',        5:'pickup/open stakebag',   6:'pickup/open supportbag', 7:'pickup/open tentbag',
                     8:'pickup/place ventcover', 9:'place guyline',      10:'spread tent',           11:'tie top'}
                            
Error_annotation = {0:'motor', 1:'misuse', 2:'order', 3:'failure', 4:'omit', 5:'search', 6:'correction', 7:'slow', 8:'repeat'}

file_path_action = tmp_current_working_directory_path + '/Synchronised_action_label.txt'
Action_label = []
with open(file_path_action) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    Action_labelDic_key_list = []
    for row in csv_reader:
        if line_count==0:
            for tmp_key in row:
                Action_labelDic_key_list.append(tmp_key)
            line_count+=1
        else:
            tmp_Dic = {}
            for i in range(0, len(row)):
                tmp_dic_key = Action_labelDic_key_list[i]
                tmp_Dic[tmp_dic_key] = row[i]
            Action_label.append(tmp_Dic)

file_path_error = tmp_current_working_directory_path + '/Synchronised_error_label.txt'
Error_label = []
with open(file_path_error) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    Error_labelDic_key_list = []
    for row in csv_reader:
        if line_count==0:
            for tmp_key in row:
                Error_labelDic_key_list.append(tmp_key)
            line_count+=1
        else:
            tmp_Dic = {}
            for i in range(0, len(row)):
                tmp_dic_key = Error_labelDic_key_list[i]
                tmp_Dic[tmp_dic_key] = row[i]
            Error_label.append(tmp_Dic)

print('Done')
