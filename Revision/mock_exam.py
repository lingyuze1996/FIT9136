from week6_abstract_data_types import MyQueue


# Q1
def bubble_sort(ip_list):
    ip_dict = {}
    for ip in ip_list:
        if ip in ip_dict.keys():
            ip_dict[ip] += 1
        else:
            ip_dict[ip] = 1

    ip_list = list(ip_dict.keys())
    n = len(ip_list)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if ip_dict[ip_list[j]] < ip_dict[ip_list[j + 1]]:
                temp = ip_list[j]
                ip_list[j] = ip_list[j + 1]
                ip_list[j + 1] = temp

    return ip_list






def find_frequency(char_list):
    result = {}
    for char in char_list:
        if char.isupper():
            if char.upper() in result.keys():
                result[char.upper()] += 1
            else:
                result[char.upper()] = 1

    return result




# Q3
def interweave_two_queues(first_queue, second_queue):
    result = MyQueue()
    while True:
        if first_queue.is_empty() and second_queue.is_empty():
            return result

        if first_queue.is_empty() or second_queue.is_empty():
            print("Cannot interweave queues")
            break

        result.append(first_queue.serve())
        result.append(second_queue.serve())

    return MyQueue()


def find_tuples(input_dic, threshold_value):
    tuple_list = []
    for key in input_dic.keys():
        if str(input_dic[key]) == input_dic[key]:
            continue
        if input_dic[key] >= threshold_value:
            tuple_list.append((key, input_dic[key]))
    return tuple_list

find_tuples({1: "a", 2: 3.1, 5: 7, "b": 10}, 4)
#write your code here








