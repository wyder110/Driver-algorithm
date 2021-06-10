import pandas
import ants.test.ants_tester as ants_tester

input_file = 'ants/test/ants_input.csv'
output_file = "ants/test/ants_output.csv"

df = pandas.read_csv(input_file)
number_of_tests = df['id'].max()

df_out = pandas.DataFrame(
    columns=['id', 'max_sum', 'max_cash', 'elapsed_time', 'max_ants_count'])

for test in range(number_of_tests):
    current_id = test+1
    current_df = df[df['id'] == current_id]
    for row in range(len(current_df)):
        current_row = df.iloc[row]
        max_sum, max_cash, elapsed_time, max_ants_count = ants_tester.ants_driver(
            config_path="config/conf3.json",
            number_of_tests=current_row.loc['number_of_tests'],
            number_of_iterations=current_row.loc['number_of_iterations'],
            starting_population=current_row.loc['starting_population'],
            alpha=float(current_row.loc['alpha']),
            beta=float(current_row.loc['beta']),
            ro=float(current_row.loc['ro'])
        )
        df_out = df_out.append(pandas.DataFrame({
            'id': [current_id],
            'max_sum': [max_sum],
            'max_cash': [max_cash],
            'elapsed_time': [elapsed_time],
            'max_ants_count': [max_ants_count]}),
            ignore_index=True)
        df_out.to_csv(output_file, index=False)
