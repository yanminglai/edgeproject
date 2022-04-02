import edge_server1
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    max_resource = 200
    max_time = 400
    init_queue_len = 200
    task_avg = []
    for eps in np.arange(0, 1, 0.01):
        edge_server1._init(max_resource, eps, init_queue_len)
        record_runtask = []
        i = 0
        while i<200:
            edge_server1.eps_select()
            # edge_server1.closest_deadline()
            # edge_server.select_rand()

            edge_server1.update_timer(1)
            edge_server1.check_task()
            i += 1

            record_runtask.append(edge_server1.get_tasklen())
        task_avg.append(sum(record_runtask) / len(record_runtask))
        print("eps = {:.2}, avg_task = {}".format(eps, sum(record_runtask) / len(record_runtask)))

    plt.title("average task online with different eps")
    plt.plot(np.arange(0,1,0.01), task_avg, 'o-', color = 'g', label = "eps range from (0,1)")
    plt.xlabel("eps")
    plt.ylabel("average online task")
    plt.legend()
    plt.show()