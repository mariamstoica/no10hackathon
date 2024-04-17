import pickle
import numpy as np
from constants import age_ranges, sexes, regions

max_number_polls = 3

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

with open('polling_data.pickle', 'rb') as handle:
    csv_dict = pickle.load(handle)

def get_relevant_polling(age_range, region, topic):
    output_dict = {}

    if topic == 'policing':
        topic = 'police'

    for file in csv_dict:
        for question in csv_dict[file]:
            if topic in question and 'Summary' not in question:
                output_dict[question] = {}
                output_dict[question][age_range] = {}
                output_dict[question][region] = {}
                keys = [csv_dict[file][question].keys()]
                for key in csv_dict[file][question]:
                    values = list(csv_dict[file][question][key].values())[1:]
                    try:
                        mean = np.mean(values)
                        std = np.std(values)
                        if key != "Don't know":
                            if age_range in csv_dict[file][question][key]:
                                val = csv_dict[file][question][key][age_range]
                                color.GREEN + 'Hello, World!' + color.END
                                if val > mean + std:
                                    output_dict[question][age_range][key] = color.GREEN + str(val) + color.END
                                elif val < mean - std:
                                    output_dict[question][age_range][key] = color.RED + str(val) + color.END
                                else:
                                    output_dict[question][age_range][key] = val
                            if region in csv_dict[file][question][key]:
                                val = csv_dict[file][question][key][region]
                                if val > mean + std:
                                    output_dict[question][region][key] = color.GREEN + str(val) + color.END
                                elif val < mean - std:
                                    output_dict[question][region][key] = color.RED + str(val) + color.END
                                else:
                                    output_dict[question][region][key] = val
                    except:
                        continue


    polling_output = {}
    num = 0
    for question in output_dict:
        num += 1
        polling_output[question] = {}
        polling_output[question][age_range] = output_dict[question][age_range]
        polling_output[question][region] = output_dict[question][region]
        if num >= max_number_polls:
            break

    return polling_output
            
    

