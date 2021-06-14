import pandas
import genetic.test.genetic_tester as genetic_tester

input_file = "genetic/test/genetic_input.csv"
output_file = "genetic/test/genetic_output.csv"

df_in = pandas.read_csv(input_file)
df_out = pandas.DataFrame(
    columns=['id', 'max_sum', 'max_cash', 'elapsed_time'])

for index, row in df_in.iterrows():
    max_sum, max_cash, elapsed_time = genetic_tester.genetic_driver(
        config_path="config/conf3.json",
        number_of_tests=row['number_of_tests'],
        number_of_iterations=row['number_of_iterations'],
        population_count=row['population_count'],
        selection_type=row['selection_type'],
        selected_percent=row['selected_percent'],
        mutation_type=row['mutation_type'],
        mutation_p=row['mutation_p'],
        cross_p=row['cross_p'])

    df_out = df_out.append(pandas.DataFrame({
        'id': [row['id']],
        'max_sum': [max_sum],
        'max_cash': [max_cash],
        'elapsed_time': [elapsed_time]}),
        ignore_index=True)
    df_out.to_csv(output_file, index=False)
