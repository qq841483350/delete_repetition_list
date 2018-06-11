#!/user/bin/env python
# coding:utf8
__author__ = 'liyatao'
'''
python删除列表中的重复元素
'''
def delete_repetition_list(list):
    list_delete_repetition={}.fromkeys(list).keys()#删除重复
    print list_delete_repetition
if __name__=="__main__":
    list=[1,2,3,4,5,6,7,8,9,10,10,10,9,8,7]
    delete_repetition_list(list)

