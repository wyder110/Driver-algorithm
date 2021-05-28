import pandas
import genetic.test.genetic_tester as genetic_tester

input_file = 'genetic/test/genetic_input.csv'
output_file = "genetic/test/genetic_output.csv"

df = pandas.read_csv(input_file)

number_of_tests = df['id'].max()

df_out = pandas.DataFrame(columns=['id', 'max_sum', 'max_cash', 'elapsed_time'])

for test in range(number_of_tests):
    current_id = test+1
    current_df = df[df['id'] == current_id]
    for row in range(len(current_df)):
        current_row = df.iloc[row]
        max_sum, max_cash, elapsed_time = genetic_tester.genetic_driver(
            config_path="config/conf3.json", 
            number_of_tests=current_row.loc['number_of_tests'], 
            number_of_iterations=current_row.loc['number_of_iterations'], 
            population_count=current_row.loc['population_count'], 
            selection_type=current_row.loc['selection_type'], 
            selected_percent=current_row.loc['selected_percent'], 
            mutation_type=current_row.loc['mutation_type'], 
            mutation_p=current_row.loc['mutation_p'], 
            cross_p=current_row.loc['cross_p'])
        df_out = df_out.append(pandas.DataFrame({'id': [current_id], 'max_sum': [max_sum], 'max_cash': [max_cash], 'elapsed_time':[elapsed_time]}), ignore_index=True)
    df_out.to_csv(output_file, index=False)

