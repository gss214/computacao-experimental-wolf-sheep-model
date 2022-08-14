from datetime import datetime
import pandas as pd
from wolf_sheep.model import WolfSheep
from mesa import batch_run
import numpy as np

params =  {"width": 20, "height": 20, "initial_sheep":100,
        "initial_wolves":50, "probability_of_disease": np.arange(0, 1, 0.2)}

experiments_per_parameter_configuration = 300
max_steps_per_simulation = 200

results = batch_run(
    WolfSheep,
    parameters=params,
    iterations=experiments_per_parameter_configuration,
    max_steps=max_steps_per_simulation,
    number_processes=1,
    data_collection_period=1,
    display_progress=True,
)

results_df = pd.DataFrame(results)
now = str(datetime.now()).replace(":","-").replace(" ","-")
file_name_sufix = ("_iter_"+str(experiments_per_parameter_configuration)+"_steps_"+str(max_steps_per_simulation)+"_"+now)
results_df.to_csv("data/WolfSheepDesease_model_data"+file_name_sufix+".csv")