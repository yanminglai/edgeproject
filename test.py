import edge_server

if __name__ == '__main__':
    edge_server._init()
    edge_server.init_task_queue(200)
    i = 0
    while i<200:
        # edge_server.FCFS()
        edge_server.closest_deadline()
        # edge_server.select_rand()

        edge_server.update_timer(1)
        edge_server.check_task()
        i += 1

    edge_server.print_task_status()
    edge_server.plot_tasknum()