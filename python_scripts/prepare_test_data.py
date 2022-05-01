import csv

# Import Data from Test file
with open('test_set.tsv', 'r', encoding='utf-8') as test_data:
    all_data_no_form = csv.reader(test_data, delimiter='\t')
    all_data = list(all_data_no_form)
    all_data.pop(0)
    test_essay_list = []
    for row_col in all_data:
        new_dict = {"essay_id": row_col[0], "essay_set": row_col[1], "essay": row_col[2],
                    "domain1_score_id": row_col[3], "domain2_score_id": row_col[4], "domain1_score": 0,
                    "domain2_score": 0, "avg_domain": 0}
        test_essay_list.append(new_dict)
    print(test_essay_list[0])

with open('test_set.csv', 'w', encoding='utf-8') as test_output:
    csv.writer(test_output)



#%%
