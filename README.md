# Driver algorithm

Algorithms that tries to determine the best route, where the driver will earn as much as possible on shipments while not spending too much on fuel. Two algorithms were used: genetic algorithm and ant colony optimization (ACO) algorithm.

## Running the app

Configurations of cities, connections, packages and parameters are in json files in `config` directory.

To run the genetic algorithm execute:
```bash
python genetic_main.py
```

To run ant colony optimization (ACO) algorithm execute:
```bash
python ants_main.py
```

To run tests on genetic algorithm, you can modify file `genetic/test/genetic_input.csv` as you want and then execute command below. Output will be saved to `genetic/test/genetic_output.csv`
```bash
python genetic_test.py
```

To run tests on ant colony optimization (ACO) algorithm, you can modify file `ants/test/ants_input.csv` as you want and then execute command below. Output will be saved to `ants/test/ants_output.csv`
```bash
python ants_test.py
```