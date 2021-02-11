__author__ = 'palaniraj.k'


import pandas as pd
import re
import random
import datetime


def generate_alpha_numeric_ids(sample , n):

    split_chars = re.split('(\d+)',sample)
    alpha = split_chars[0]
    incident_list = []
    for i in range(n):
        incident_list.append(alpha+str(int(split_chars[1])+i))

    return incident_list

def generate_incident_ci_id_name(sample , n):

    ci_id = list(sample.keys())

    ci_name_op_list = []
    ci_ids_op_list = []

    for i in range(n):
        e = random.choice(ci_id)
        ci_ids_op_list.append(e)

    for i in ci_ids_op_list:
        ci_name_op_list.append(sample[i])

    return ci_ids_op_list , ci_name_op_list


def generate_from_list(sample,n):
    op_list = []
    for i in range(n):
        e = random.choice(sample)
        op_list.append(e)

    return op_list


def generate_date_range(start , end , n):

    return pd.date_range(start, end, periods=n)


def generate_incident_dataset(n,cols):

    incident_id = generate_alpha_numeric_ids("INC0015927461" , n)
    ci_id , ci_name = generate_incident_ci_id_name(incident_ci_id_name,n)
    priority = generate_from_list(priority_list,n)
    Incident_state = generate_from_list(Incident_state_list,n)
    Incident_assi_grp = generate_from_list(Incident_assi_grp_list,n)
    Incident_assi_to = generate_from_list(Incident_assi_to_list,n)
    Incident_start_date_list = generate_date_range("2020-08-01" , "2021-02-05" , n)


    generated_df = pd.DataFrame(columns=cols)
    generated_df["Incident_ref_no"] = incident_id
    generated_df["Incident_ci_id"] = ci_id
    generated_df["Incident_ci_name"] = ci_name
    generated_df["Incident_priority"] = priority
    generated_df["Incident_state"] = Incident_state
    generated_df["Incident_assi_grp"] = Incident_assi_grp
    generated_df["Incident_assi_to"] = Incident_assi_to
    generated_df["Incident_start_date"] = Incident_start_date_list

     ## Adding end time
    end_time_list = []
    for i in generated_df["Incident_start_date"]:
        e = random.choice(random_mins)
        end_time_list.append(i+datetime.timedelta(minutes=e))

    generated_df["Incident_end_date"] = end_time_list


    print(generated_df.head())

    generated_df.to_csv("Incident_Data.csv")

    return generated_df




priority_list = ["Priority 3" , "Priority 2" , "Priority 1"]
Incident_state_list = ["Solved Proposed" , "Solved Confirmed" , "Inprogress Investigate"]
Incident_assi_grp_list = ["BCS SUPPORT LEVEL 3" , "BCS SUPPORT LEVEL 2" , "BCS SUPPORT LEVEL 1"]
Incident_assi_to_list = ["muni.kumargunda@db.com","palaniraj.kandasamy@db.com","rohit.ganju@db.com"]
incident_ci_id_name = {
    "35280-1" : "BCS-BPC, PAPM  Production",
    "35280-2" : "BCS-BPC, PAPM  Staging",
    "35280-3" : "BCS-BPC, PAPM  Development"
}
random_mins = [100,1440,2880]

columns = ["Incident_ref_no",
       "Incident_ci_id",
       "Incident_ci_name",
       "Incident_priority",
       "Incident_state",
       "Incident_start_date",
       "Incident_end_date",
       "Incident_assi_grp",
       "Incident_assi_to",
       "Work_notes"]

generate_incident_dataset(1000,columns)
#fgjfj