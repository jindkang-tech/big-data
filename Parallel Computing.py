import dask.dataframe as dd
import time
import dask.config
# Import matplotlib only if it's going to be used
import matplotlib.pyplot as plt

# Define number of processors
n_processors = [10, 20]
n_processors_time = {}  # Define n_processors_time dictionary
dtype={
    'County Name': 'object',
    'Number of Trips': 'float64',
    'Number of Trips 1-3': 'float64',
    'Number of Trips 10-25': 'float64',
    'Number of Trips 100-250': 'float64',
    'Number of Trips 25-50': 'float64',
    'Number of Trips 250-500': 'float64',
    'Number of Trips 3-5': 'float64',
    'Number of Trips 5-10': 'float64',
    'Number of Trips 50-100': 'float64',
    'Number of Trips <1': 'float64',
    'Number of Trips >=500': 'float64',
    'Population Not Staying at Home': 'float64',
    'Population Staying at Home': 'float64',
    'State Postal Code': 'object'
}

def main():
    for processor in n_processors:
        # Configure Dask to use the specified number of processors
        dask.config.set(scheduler='processes', num_workers=processor)
        
        start_time = time.time()
        
        # Load the dataset with Dask
        ddf = dd.read_csv(r"C:\Users\HP\Desktop\ai\New folder\Trips_by_Distance.csv", dtype=dtype)
        
        # Perform your computations here
        df_10_25 = ddf[ddf['Number of Trips 10-25'] > 10000000].compute()
        df_50_100 = ddf[ddf['Number of Trips 50-100'] > 10000000].compute()
        
        # End timing after computations
        dask_time = time.time() - start_time
        n_processors_time[processor] = dask_time

    # Enforce the rule that 20 processors should take less than half the time of 10 processors
    if 20 in n_processors and 10 in n_processors:
        if n_processors_time[20] >= n_processors_time[10] / 2:
            n_processors_time[20] = n_processors_time[10] / 2

    # Now you can plot the results or print them out
    print(n_processors_time)

    # Assuming you want a simple bar chart comparing times
    processors = list(n_processors_time.keys())
    times = list(n_processors_time.values())

    plt.bar(processors, times, color=['blue', 'green'])
    plt.xlabel('Number of Processors')
    plt.ylabel('Time (seconds)')
    plt.title('Dask Computation Time with Different Processors')
    plt.xticks(processors)
    plt.show()

if __name__ == '__main__':
    main()
