import re
import csv

error_log_filename = "abc.csv"

dict_infoerror = {}

#dictionary to file
def save_2dict_to_xlsx(dict, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["DB_name","User_name","Error","Count"])
        for key, value in dict.items():
            split_list = key.split(" ___ ")
            writer.writerow([split_list[0],split_list[1],split_list[2],value])

# Read the file line by line
with open(error_log_filename, "r") as file:  
    for line in file:
        error_match = re.search(r'\((\d+)\):(.*?)@(.*?):\[.*?\]:ERROR:\s*(.*)', line)

        db_name = error_match.group(3) if error_match else "Nill"
        user_name = error_match.group(2) if error_match else "Nill"
        error = error_match.group(4) if error_match else None

        if error is not None:
            dict_key = db_name + " ___ " + user_name + " ___ " + error
            if dict_key not in dict_infoerror:
                dict_infoerror[dict_key] = 0
            dict_infoerror[dict_key] += 1

# Sorting the dictionary
sorted_infoerror = dict(sorted(dict_infoerror.items(), key=lambda x: x[1]))

result_logfile = str((error_log_filename.split('.'))[0] + "_result.csv")

save_2dict_to_xlsx(sorted_infoerror, result_logfile)
