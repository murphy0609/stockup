from datacollector.views import circual_run_get_individual_data, get_all_china_individual_data
from utils.thread import add_thread_func

# add_thread_func(circual_run_get_individual_data)
if __name__=='__main__':
    get_all_china_individual_data()
