"""
Each Part has consecutive set of Processes to be executed
Each Process requires Resource

Simulation Components follow the naming convention below.

[6Factor Concept]   [Class Object]
Part                Job
Process             Operation
Resource            Machine, Worker, Factory, Line, Transporter, etc.
Source              Source
Sink                Sink
Monitor             Monitor

Revised in 2023. 11. 15.
"""
import sys
import os
# from config import *
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
from environment.Process import *
from environment.Source import Source
from environment.Sink import Sink
from environment.Resource import Machine
from environment.Monitor import Monitor
from postprocessing.PostProcessing import *
from visualization.Gantt import *
from visualization.GUI import GUI
import simpy
from data import *
from cfg_local import Configure

env = simpy.Environment()
cfg = Configure()
monitor = Monitor(cfg.filepath)
model = dict()

for i, q in enumerate(abz5_machine_list):
    model[q] = Machine(env, i, q)
for j, p in enumerate(abz5_process_list):
    model[p] = Process(cfg, env, p, model, monitor)

for i, j in enumerate(abz5_process):
    model['Source' + str(i + 1)] = Source(cfg, env, 'J' + str(i + 1), model, monitor,
                                          job_type=job_list[i], IAT=cfg.IAT, num_parts=1)

model['Sink'] = Sink(cfg, env, monitor)

env.run(5000)
monitor.save_event()

# In case of the situation where termination of the simulation greatly affects the machine utilization time,
# it is necessary to terminate all the process at (SIMUL_TIME -1) and add up the process time to all machines

machine_log = read_machine_log(cfg.filepath)
gantt = Gantt(cfg, machine_log, len(machine_log), printmode=True, writemode=True)
gui = GUI(gantt)
# print()



