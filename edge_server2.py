import random
import numpy as np
import matplotlib.pyplot as plt

import random

class Edge_Node:
    def __init__(self, max_resource, eps, init_queue_len):
        self.max_resource = max_resource
        self.eps = eps
        self.remain_resource = max_resource
        self.init_queue_len = init_queue_len
        # for init task at beginning
        self.taskID = []
        self.resource = []
        self.eta = []
        # deadline from now
        self.deadline_from_now = [] 

        # for maintaining current task status
        self.cur_ID = []
        self.cur_eta = []
        self.cur_rs = []
        self.timestamp = 0

        # for ploting
        self.record_ts = []
        self.record_runtask = []
    def initialize_queue(self):
        for task in range(self.init_queue_len):
            resource_this_task = random.randint(1,10)
            eta_this_task = random.randint(1,20)
            deadline_this_task = eta_this_task + random.randint(20, 50)
            self.taskID.append(task)
            self.resource.append(resource_this_task)
            self.eta.append(eta_this_task)
            self.deadline_from_now.append(deadline_this_task)
        # print("resource list", self.resource)


    def eps_select(self):
        p = np.random.random()
        if p < self.eps:
            idx = random.randint(0, len(self.taskID)-1)
        else: 
            idx = 0

        # print("cur_rs", self.cur_rs)
        # print("cur_eta", self.cur_eta)
        # print("self.resource[0]", self.resource[idx])
        # print("self.remain_resource", self.remain_resource)       
        if not self.resource:
            print("all task completed")

        elif self.resource[idx] < self.remain_resource:
            self.cur_ID.append(self.taskID.pop(idx))
            self.cur_eta.append(self.eta.pop(idx) + self.timestamp)
            self.cur_rs.append(self.resource.pop(idx))
            # print("cur_eta", self.cur_eta)
        else:
            print("resource not enough, halt")

    def FCFS(self):
        p = np.random.random()
        # if p < self.eps:
        #     idx = random.randint(0, len(self.taskID))
        # else: 
        #     idx = 0
        idx = 0

        # print("cur_rs", self.cur_rs)
        # print("cur_eta", self.cur_eta)
        # print("self.resource[0]", self.resource[idx])
        # print("self.remain_resource", self.remain_resource)       
        if not self.resource:
            print("all task completed")

        elif self.resource[idx] < self.remain_resource:
            self.cur_ID.append(self.taskID.pop(idx))
            self.cur_eta.append(self.eta.pop(idx) + self.timestamp)
            self.cur_rs.append(self.resource.pop(idx))
            # print("cur_eta", self.cur_eta)
        else:
            print("resource not enough, halt")


    def closest_deadline(self):
        idx = self.eta.index(min(self.eta))

        if not self.resource:
            print("all task completed")

        elif self.resource[idx] < self.remain_resource:
            self.cur_ID.append(self.taskID.pop(idx))
            self.cur_eta.append(self.eta.pop(idx) + self.timestamp)
            self.cur_rs.append(self.resource.pop(idx))
            # print("cur_eta", self.cur_eta)
        else:
            print("resource not enough, halt")

    def select_rand(self):
        idx = random.randint(0, len(self.taskID) - 1)
 
        if not self.resource:
            print("all task completed")

        elif self.resource[idx] < self.remain_resource:
            self.cur_ID.append(self.taskID.pop(idx))
            self.cur_eta.append(self.eta.pop(idx) + self.timestamp)
            self.cur_rs.append(self.resource.pop(idx))
            # print("cur_eta", self.cur_eta)
        else:
            print("resource not enough, halt")


    def check_task(self):
        idx = 0

        # check if task expired
        while idx < len(self.cur_ID):
            if self.cur_eta[idx] < self.timestamp:
                self.cur_ID.pop(idx)
                self.cur_eta.pop(idx)
                self.cur_rs.pop(idx)
            idx += 1

        # update remaining resource
        self.remain_resource = self.max_resource - sum(self.cur_rs)

        print("current time:", self.timestamp)    
        print("current running task:", len(self.cur_ID))
        # save for plot
        self.record_ts.append(self.timestamp)
        self.record_runtask.append(len(self.cur_ID))

    def update_timer(self, value):
        self.timestamp += value

    def print_task(self):
        print("Node Remain Resource:", self.remain_resource)
        print("ID:", self.cur_ID)
        print("Resource:", self.cur_rs)
        print("ETA:", self.cur_eta)


    def plot_tasknum(self):
        # plt.scatter(self.record_ts, self.record_runtask)
        plt.title("select closest deadline")
        plt.plot(self.record_ts, self.record_runtask, 'o-', color = 'g', label = "FCFS")
        plt.xlabel("time stamp")
        plt.ylabel("# of online task")
        plt.show()






def _init(max_resource, eps, init_queue_len):
    global _edge_server
    _edge_server = Edge_Node(max_resource, eps, init_queue_len)
    _edge_server.initialize_queue()

def init_task_queue():
    return _edge_server.initialize_queue()

def eps_select():
    return _edge_server.eps_select()

def FCFS():
    return _edge_server.FCFS()

def closest_deadline():
    return _edge_server.closest_deadline()

def select_rand():
    return _edge_server.select_rand()

def check_task():
    return _edge_server.check_task()

def print_task_status():
    return _edge_server.print_task()

def update_timer(value):
    return _edge_server.update_timer(value)

def plot_tasknum():
    return _edge_server.plot_tasknum()

def get_tasklen():
    return len(_edge_server.cur_ID)