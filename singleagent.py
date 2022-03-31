import edge_server1

if __name__ == '__main__':
    max_resource = 200
    eps1 = 0.3
    max_time = 200
    init_queue_len = 200
    edge_server1._init(max_resource, eps1, init_queue_len)
    i = 0
    while i<200:
        edge_server1.FCFS()
        # edge_server1.closest_deadline()
        # edge_server.select_rand()

        edge_server1.update_timer(1)
        edge_server1.check_task()
        i += 1

    edge_server1.print_task_status()
    edge_server1.plot_tasknum()