#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  vampire.py
#
#  Copyright 2015 medici castillo <castille@qq.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

try:
    import cPickle as pickle
except:
    import pickle

class MyClass():
    """ 班级档案管理系统 """

    def __init__ (self):
        """ with 读取pickle持久化存储文件 """
        with open('classfile','wb') as classfile:
            try:
                self.classinfo = pickle.load(classfile)
            except:
                self.classinfo = []

    def save (self):
        """ 保存 """
        with open('classfile','wb') as classfile:
            pickle.dump(self.classinfo,classfile,-1)

    def add (self):
        """ 添加学生 """
        num = raw_input('num:')
        name = raw_input('name:')
        sex = raw_input('sex:')
        age = input('age:')
        degree = input('degree:')
        self.classinfo.append((num,name,sex,age,degree))

    def rm (self):
        """ 删除学生 """
        num = raw_input('num:')
        self.classinfo = [i for i in self.classinfo if i[0] != num]

    def show (self):
        """ 显示所有学生的学号，姓名，性别，年龄，成绩 """
        for i in self.classinfo:
            print i

    def change (self):
        """ 修改学生信息 """
        print 'change student number'
        self.rm()
        print 'change info'
        self.add()

    def find (self):
        """ 查找 """
        findinfo = raw_input('number or name:')
        find = raw_input('info:')
        if findinfo in ('number','name') and findinfo == 'number':
            for i in [j for j in self.classinfo if j[0] == find]:
                print i
        elif findinfo in ('number','name') and findinfo == 'name':
            for i in [j for j in self.classinfo if j[0] == find]:
                print i
        else:
            print 'wrong info'

    def appinfo (self):
        """ 作者信息 """
        print 'made by castillo'

    def status (self):
        """ 统计信息 """
        agestatus = [i[3] for i in self.classinfo]
        degreestatus = [i[4] for i in self.classinfo]
        degreesort = [(degree , num , name , sex , age) for num , name , sex , age , degree in self.classinfo]
        print 'class student:%d\n max and min age:%f %f\n age:%f\n max and min degree:%f %f\n degree:%f\n sort by degree: ' % (len(self.classinfo), max(agestatus),min(agestatus), float(reduce(lambda x,y:x+y,agestatus)/len(self.classinfo), max(degreestatus),min(degreestatus), float(reduce(lambda x,y:x+y,degreestatus)/len(self.classinfo))))
        for i in sorted(degreesort):
            print i[1:]+i[0]

def main():
    myclass = MyClass()
    while True:
        a = raw_input('commend[add,appinfo,change,find,rm,save,show,status,exit]:')
        try:
            getattr(myclass,a)()
        except:
            if a == 'exit':
                break
            else:
                print 'wrong commend'
    return 0       

if __name__ == '__main__':
    main()
