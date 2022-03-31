import queue
import edge_server1
import edge_server2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    max_resource = 200
    eps1 = 0.3
    max_time = 200
    init_queue_len = 200
    record_ts = []
    record_runtask = []
    edge_server1._init(max_resource, eps1, init_queue_len)
    edge_server2._init(max_resource, eps1, init_queue_len)

    i = 0

    while i < max_time:
        # edge_server.FCFS()
        # edge_server1.closest_deadline()
        # edge_server.select_rand()
        edge_server1.eps_select()
        edge_server1.update_timer(1)
        edge_server1.check_task()
        edge_server2.eps_select()
        edge_server2.update_timer(1)
        edge_server2.check_task() 
               
        record_ts.append(i)
        record_runtask.append(edge_server1.get_tasklen() + edge_server2.get_tasklen())

        i += 1
#-------------------------------------------------------------------------------
    eps2 = 0.7
    record_ts2 = []
    record_runtask2 = []
    edge_server1._init(max_resource, eps2, init_queue_len)
    edge_server2._init(max_resource, eps2, init_queue_len)

    i = 0

    while i < max_time:
        # edge_server.FCFS()
        # edge_server1.closest_deadline()
        # edge_server.select_rand()
        edge_server1.eps_select()
        edge_server1.update_timer(1)
        edge_server1.check_task()
        edge_server2.eps_select()
        edge_server2.update_timer(1)
        edge_server2.check_task() 
               
        record_ts2.append(i)
        record_runtask2.append(edge_server1.get_tasklen() + edge_server2.get_tasklen())

        i += 1




    edge_server1.print_task_status()
    plt.title("multi-agent on different eps")
    plt.plot(record_ts, record_runtask, 'o-', color = 'g', label = "eps=0.5")
    plt.plot(record_ts2, record_runtask2, 'o-', color = 'r', label = "eps=0.7")
    plt.xlabel("time stamp")
    plt.ylabel("# of online task")
    plt.legend()
    plt.show()