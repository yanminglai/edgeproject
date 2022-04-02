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

    # random generate version    
    # def initialize_queue(self):
    #     for task in range(self.init_queue_len):
    #         resource_this_task = random.randint(1,10)
    #         eta_this_task = random.randint(1,20)
    #         deadline_this_task = eta_this_task + random.randint(20, 50)
    #         self.taskID.append(task)
    #         self.resource.append(resource_this_task)
    #         self.eta.append(eta_this_task)
    #         self.deadline_from_now.append(deadline_this_task)
    #     print("------------taskID list---------------\n", self.taskID)
    #     print("------------resource list---------------\n", self.resource)
    #     print("------------eta list---------------\n", self.eta)
    #     print("------------deadline from now list---------------\n", self.deadline_from_now)
    #     # print("resource list", self.resource)

    # fixed version for comparing different eps values
    def initialize_queue(self):
        self.taskID = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199]
        self.resource = [9, 3, 5, 4, 8, 10, 4, 5, 7, 10, 3, 6, 8, 3, 8, 4, 2, 4, 10, 5, 10, 4, 5, 3, 2, 3, 6, 9, 7, 4, 2, 4, 2, 1, 4, 5, 3, 5, 10, 3, 10, 7, 10, 2, 2, 10, 9, 7, 8, 3, 9, 8, 4, 5, 7, 5, 5, 2, 3, 5, 10, 10, 10, 10, 9, 6, 6, 10, 1, 1, 4, 2, 3, 8, 8, 4, 4, 4, 1, 1, 6, 6, 4, 4, 5, 7, 1, 4, 1, 7, 2, 3, 10, 10, 5, 7, 8, 8, 3, 2, 1, 4, 8, 6, 3, 2, 10, 7, 10, 7, 1, 5, 4, 4, 7, 3, 5, 5, 6, 4, 10, 7, 1, 4, 2, 10, 7, 4, 4, 3, 6, 7, 2, 4, 4, 9, 8, 3, 4, 10, 7, 6, 2, 7, 9, 7, 3, 4, 2, 5, 1, 1, 5, 8, 8, 10, 3, 1, 1, 1, 3, 2, 7, 5, 4, 7, 10, 3, 1, 1, 7, 9, 1, 3, 8, 7, 7, 3, 4, 3, 3, 7, 4, 5, 5, 1, 9, 10, 6, 1, 4, 6, 10, 6, 6, 1, 5, 9, 7, 3]
        self.eta = [9, 20, 19, 9, 19, 3, 9, 2, 5, 14, 16, 3, 1, 16, 7, 17, 2, 4, 11, 16, 13, 9, 18, 11, 20, 2, 11, 8, 4, 15, 16, 13, 4, 8, 6, 3, 5, 19, 4, 19, 5, 15, 18, 3, 9, 16, 13, 18, 19, 2, 10, 7, 12, 11, 20, 17, 4, 8, 6, 8, 2, 3, 13, 9, 18, 6, 18, 5, 18, 2, 8, 1, 13, 14, 10, 14, 1, 8, 7, 5, 5, 16, 12, 11, 14, 8, 18, 20, 5, 7, 11, 15, 16, 9, 11, 8, 12, 11, 2, 20, 5, 5, 18, 18, 1, 16, 3, 13, 10, 12, 3, 2, 15, 12, 16, 8, 15, 1, 13, 3, 14, 20, 3, 16, 19, 7, 7, 19, 12, 6, 10, 6, 12, 13, 20, 4, 4, 11, 7, 13, 20, 3, 4, 1, 15, 18, 13, 15, 8, 20, 1, 19, 9, 15, 2, 12, 12, 3, 4, 8, 8, 11, 16, 18, 13, 13, 6, 20, 18, 3, 10, 6, 9, 15, 12, 7, 14, 16, 2, 13, 19, 5, 11, 5, 15, 1, 12, 18, 16, 10, 8, 8, 6, 3, 11, 17, 3, 7, 17, 4]
        self.deadline_from_now = [31, 42, 69, 36, 62, 52, 53, 42, 48, 41, 57, 25, 43, 60, 38, 37, 51, 26, 50, 66, 42, 47, 45, 33, 42, 42, 39, 48, 54, 50, 61, 40, 27, 48, 52, 48, 29, 60, 34, 54, 39, 49, 39, 48, 54, 39, 60, 60, 67, 36, 57, 27, 38, 38, 49, 66, 51, 40, 29, 53, 26, 49, 34, 31, 55, 39, 51, 45, 38, 47, 53, 33, 52, 63, 59, 55, 23, 29, 56, 27, 32, 58, 36, 37, 44, 57, 44, 67, 45, 37, 47, 53, 65, 41, 55, 40, 36, 46, 33, 67, 28, 39, 46, 45, 41, 58, 31, 56, 42, 35, 34, 24, 41, 51, 60, 37, 45, 
39, 34, 45, 38, 64, 45, 66, 50, 27, 38, 65, 57, 31, 57, 54, 41, 35, 46, 43, 48, 52, 36, 35, 45, 27, 44, 41, 41, 52, 42, 47, 43, 54, 45, 53, 58, 35, 50, 37, 60, 37, 34, 43, 57, 31, 43, 42, 60, 50, 30, 42, 53, 33, 39, 38, 53, 49, 42, 57, 37, 63, 37, 57, 62, 43, 59, 31, 45, 42, 54, 58, 37, 39, 57, 37, 33, 42, 47, 42, 53, 47, 62, 29]

    
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

        # print("current time:", self.timestamp)    
        # print("current running task:", len(self.cur_ID))
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