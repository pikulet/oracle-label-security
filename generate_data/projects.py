# cols: proj_name, phone, position, dept, region

import helper
import labels
from itertools import product

proj_table_name = 'projects'
budget_table_name = 'project_budgets'

proj_table_cols = ['proj_name', 'description', 'eng_type', 'region']
budget_table_cols = ['proj_name', 'budget']

proj_stmt = helper.get_insert_statement(proj_table_name,
                                        helper.sql_columns_format(proj_table_cols))
budget_stmt = helper.get_insert_statement(budget_table_name,
                                          helper.sql_columns_format(budget_table_cols))

def gen_statements():
    results = []
    for elem in product(*labels.get('projects')):
        proj_name = helper.gen_random_alpha_str(10)
        description = helper.gen_random_alpha_str(30)
        level = elem[0]
        # TODO: insert the ols label using script
        eng_type = elem[1]
        pos = elem[2]
        region = elem[3]
        budget = helper.gen_random_numeric(30, 100) * 1000

        proj_table_vals_f = helper.sql_values_format([proj_name, description,
                                                      eng_type, region])
        budget_table_vals_f = helper.sql_values_format([proj_name, budget])
        results.append(helper.insert_vals(proj_stmt, proj_table_vals_f))
        results.append(helper.insert_vals(budget_stmt, budget_table_vals_f))

    return results

