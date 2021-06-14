import pandas
import ants.test.ants_tester as ants_tester

input_file = "ants/test/ants_input.csv"
output_file = "ants/test/ants_output.csv"

df_in = pandas.read_csv(input_file)
df_out = pandas.DataFrame(
    columns=['id', 'max_sum', 'max_cash', 'elapsed_time', 'trace_len'])

for index, row in df_in.iterrows():
    max_sum, max_cash, elapsed_time, trace_len = ants_tester.ants_driver(
        config_path="config/conf3.json",
        number_of_tests=row['number_of_tests'],
        number_of_iterations=row['number_of_iterations'],
        starting_population=row['starting_population'],
        alpha=float(row['alpha']),
        beta=float(row['beta']),
        ro=float(row['ro']))

    df_out = df_out.append(pandas.DataFrame({
        'id': row['id'],
        'max_sum': [max_sum],
        'max_cash': [max_cash],
        'elapsed_time': [elapsed_time],
        'trace_len': [trace_len]}),
        ignore_index=True)
    df_out.to_csv(output_file, index=False)
